"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import pilotage_app as router_pilotage_app
from app.routers import pilot as router_pilot
from app.routers import tug as router_tug
from app.routers import tide as router_tide
from app.routers import berth as router_berth
from app.routers import anchorage as router_anchorage
from app.routers import channel as router_channel
from app.routers import vts as router_vts
from app.routers import schedule as router_schedule
from app.routers import cargo as router_cargo
from app.routers import weather as router_weather
from app.routers import fee as router_fee
from app.routers import incident as router_incident
from app.routers import ais as router_ais
from app.routers import buoy as router_buoy
from app.routers import pilotlog as router_pilotlog

ROUTERS = [router_pilotage_app, router_pilot, router_tug, router_tide, router_berth, router_anchorage, router_channel, router_vts, router_schedule, router_cargo, router_weather, router_fee, router_incident, router_ais, router_buoy, router_pilotlog]
