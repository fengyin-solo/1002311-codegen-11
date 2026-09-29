"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class PilotageAppEntry(BaseModel):
    """引航申请单明细结构。"""

    field_0: str | None = None  # 申请编号
    field_1: str | None = None  # 船名
    field_2: str | None = None  # 船舶类型
    field_3: str | None = None  # 总吨位
    field_4: str | None = None  # 吃水深度
    field_5: str | None = None  # 靠泊码头
    field_6: str | None = None  # 申请引航时间
    field_7: str | None = None  # 申请状态

class PilotEntry(BaseModel):
    """引航员明细结构。"""

    field_0: str | None = None  # 引航员编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 资质等级
    field_3: str | None = None  # 适航区域
    field_4: str | None = None  # 联系电话
    field_5: str | None = None  # 上次体检日期
    field_6: str | None = None  # 值班状态
    field_7: str | None = None  # 从业年限

class TugEntry(BaseModel):
    """拖轮明细结构。"""

    field_0: str | None = None  # 拖轮编号
    field_1: str | None = None  # 拖轮名称
    field_2: str | None = None  # 马力匹数
    field_3: str | None = None  # 船长
    field_4: str | None = None  # 船员人数
    field_5: str | None = None  # 上次维保日期
    field_6: str | None = None  # 靠泊基地
    field_7: str | None = None  # 拖轮状态

class TideEntry(BaseModel):
    """潮汐记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 监测站
    field_2: str | None = None  # 观测日期
    field_3: str | None = None  # 高潮时刻
    field_4: str | None = None  # 高潮水位
    field_5: str | None = None  # 低潮时刻
    field_6: str | None = None  # 低潮水位
    field_7: str | None = None  # 数据来源

class BerthEntry(BaseModel):
    """泊位明细结构。"""

    field_0: str | None = None  # 泊位编号
    field_1: str | None = None  # 泊位名称
    field_2: str | None = None  # 泊位长度
    field_3: str | None = None  # 前沿水深
    field_4: str | None = None  # 靠泊能力等级
    field_5: str | None = None  # 码头公司
    field_6: str | None = None  # 当前占用船名
    field_7: str | None = None  # 泊位状态

class AnchorageEntry(BaseModel):
    """锚地明细结构。"""

    field_0: str | None = None  # 锚地编号
    field_1: str | None = None  # 锚地名称
    field_2: str | None = None  # 锚地面积
    field_3: str | None = None  # 最大锚泊艘数
    field_4: str | None = None  # 底质类型
    field_5: str | None = None  # 水深范围
    field_6: str | None = None  # 当前锚泊数
    field_7: str | None = None  # 锚地状态

class ChannelEntry(BaseModel):
    """航道明细结构。"""

    field_0: str | None = None  # 航道编号
    field_1: str | None = None  # 航道名称
    field_2: str | None = None  # 航道等级
    field_3: str | None = None  # 通航净宽
    field_4: str | None = None  # 维护水深
    field_5: str | None = None  # 通航方向
    field_6: str | None = None  # 上次扫测日期
    field_7: str | None = None  # 航道状态

class VtsEntry(BaseModel):
    """船舶动态记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 船名
    field_2: str | None = None  # 当前航速
    field_3: str | None = None  # 当前航向
    field_4: str | None = None  # 船位纬度
    field_5: str | None = None  # 船位经度
    field_6: str | None = None  # 下一港
    field_7: str | None = None  # 动态类型

class ScheduleEntry(BaseModel):
    """排班表明细结构。"""

    field_0: str | None = None  # 班次编号
    field_1: str | None = None  # 引航员
    field_2: str | None = None  # 日期
    field_3: str | None = None  # 班次时段
    field_4: str | None = None  # 任务数量
    field_5: str | None = None  # 加班时长
    field_6: str | None = None  # 排班人
    field_7: str | None = None  # 班次状态

class CargoEntry(BaseModel):
    """危险品船舶明细结构。"""

    field_0: str | None = None  # 申报编号
    field_1: str | None = None  # 船名
    field_2: str | None = None  # 危险品类别
    field_3: str | None = None  # 危险品名称
    field_4: str | None = None  # 载运数量
    field_5: str | None = None  # 承运单位
    field_6: str | None = None  # 引航时间
    field_7: str | None = None  # 申报状态

class WeatherEntry(BaseModel):
    """气象预警信息明细结构。"""

    field_0: str | None = None  # 预警编号
    field_1: str | None = None  # 预警类型
    field_2: str | None = None  # 影响区域
    field_3: str | None = None  # 预警等级
    field_4: str | None = None  # 发布时间
    field_5: str | None = None  # 预计持续时长
    field_6: str | None = None  # 发布单位
    field_7: str | None = None  # 预警状态

class FeeEntry(BaseModel):
    """引航费账单明细结构。"""

    field_0: str | None = None  # 账单编号
    field_1: str | None = None  # 船名
    field_2: str | None = None  # 引航起止点
    field_3: str | None = None  # 引航里程
    field_4: str | None = None  # 计费吨
    field_5: str | None = None  # 应收金额
    field_6: str | None = None  # 缴费截止日
    field_7: str | None = None  # 缴费状态

class IncidentEntry(BaseModel):
    """海事事件明细结构。"""

    field_0: str | None = None  # 事件编号
    field_1: str | None = None  # 事件类型
    field_2: str | None = None  # 涉事船舶
    field_3: str | None = None  # 发生时间
    field_4: str | None = None  # 发生位置
    field_5: str | None = None  # 事件等级
    field_6: str | None = None  # 处理人
    field_7: str | None = None  # 事件状态

class AisEntry(BaseModel):
    """AIS基站明细结构。"""

    field_0: str | None = None  # 基站编号
    field_1: str | None = None  # 安装位置
    field_2: str | None = None  # 基站型号
    field_3: str | None = None  # 天线高度
    field_4: str | None = None  # 覆盖范围
    field_5: str | None = None  # 上次维护日期
    field_6: str | None = None  # 在线状态
    field_7: str | None = None  # 基站状态

class BuoyEntry(BaseModel):
    """航标明细结构。"""

    field_0: str | None = None  # 航标编号
    field_1: str | None = None  # 航标名称
    field_2: str | None = None  # 航标类型
    field_3: str | None = None  # 经纬度位置
    field_4: str | None = None  # 灯质规格
    field_5: str | None = None  # 上次巡检日期
    field_6: str | None = None  # 巡检人员
    field_7: str | None = None  # 航标状态

class PilotlogEntry(BaseModel):
    """引航日志明细结构。"""

    field_0: str | None = None  # 日志编号
    field_1: str | None = None  # 引航员
    field_2: str | None = None  # 引航日期
    field_3: str | None = None  # 引航船舶
    field_4: str | None = None  # 引航开始时间
    field_5: str | None = None  # 引航结束时间
    field_6: str | None = None  # 特殊情况
    field_7: str | None = None  # 日志状态
