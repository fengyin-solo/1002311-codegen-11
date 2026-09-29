# 船舶引航调度管理平台

面向引航申请、拖轮调度、潮汐监测、泊位分配、锚地管理与引航员排班的一体化船舶引航调度管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 引航申请 | `pilotage_app` | 引航申请单 | 申请编号、船名、船舶类型 |
| 引航员管理 | `pilot` | 引航员 | 引航员编号、姓名、资质等级 |
| 拖轮调度 | `tug` | 拖轮 | 拖轮编号、拖轮名称、马力匹数 |
| 潮汐监测 | `tide` | 潮汐记录 | 记录编号、监测站、观测日期 |
| 泊位管理 | `berth` | 泊位 | 泊位编号、泊位名称、泊位长度 |
| 锚地管理 | `anchorage` | 锚地 | 锚地编号、锚地名称、锚地面积 |
| 航道管理 | `channel` | 航道 | 航道编号、航道名称、航道等级 |
| 船舶动态 | `vts` | 船舶动态记录 | 记录编号、船名、当前航速 |
| 引航排班 | `schedule` | 排班表 | 班次编号、引航员、日期 |
| 危险品船舶管理 | `cargo` | 危险品船舶 | 申报编号、船名、危险品类别 |
| 气象预警 | `weather` | 气象预警信息 | 预警编号、预警类型、影响区域 |
| 引航费管理 | `fee` | 引航费账单 | 账单编号、船名、引航起止点 |
| 海事事件管理 | `incident` | 海事事件 | 事件编号、事件类型、涉事船舶 |
| AIS设备管理 | `ais` | AIS基站 | 基站编号、安装位置、基站型号 |
| 航标管理 | `buoy` | 航标 | 航标编号、航标名称、航标类型 |
| 引航日志 | `pilotlog` | 引航日志 | 日志编号、引航员、引航日期 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
