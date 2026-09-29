"""锚地管理接口：维护锚地，覆盖开放锚地、饱和预警、关闭锚地等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.anchorage import AnchorageService

router = APIRouter(prefix="/api/anchorage", tags=["锚地管理"])

service = AnchorageService()

LIST_FIELDS = ["锚地编号", "锚地名称", "锚地面积", "最大锚泊艘数", "底质类型", "水深范围", "当前锚泊数", "锚地状态"]
STATUSES = ["开放使用", "已饱和", "临时关闭", "已禁用"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    keyword: str | None = Query(default=None, description="按锚地编号检索"),
    status: str | None = Query(default=None, description="开放使用、已饱和、临时关闭、已禁用"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按锚地编号与状态过滤锚地管理列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size)
    return PageResult(items=items, total=total, page=page, size=size)


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条锚地明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"锚地 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条锚地，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="锚地已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条锚地执行开放锚地、饱和预警、关闭锚地；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)


@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出锚地管理清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "anchorage", "total": total, "items": items}
