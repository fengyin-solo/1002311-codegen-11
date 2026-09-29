<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">船舶引航调度管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向引航申请、拖轮调度、潮汐监测、泊位分配、锚地管理与引航员排班的一体化船舶引航调度管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "引航申请", path: "/pilotage_app" }, { label: "引航员管理", path: "/pilot" }, { label: "拖轮调度", path: "/tug" }, { label: "潮汐监测", path: "/tide" }, { label: "泊位管理", path: "/berth" }, { label: "锚地管理", path: "/anchorage" }, { label: "航道管理", path: "/channel" }, { label: "船舶动态", path: "/vts" }, { label: "引航排班", path: "/schedule" }, { label: "危险品船舶管理", path: "/cargo" }, { label: "气象预警", path: "/weather" }, { label: "引航费管理", path: "/fee" }, { label: "海事事件管理", path: "/incident" }, { label: "AIS设备管理", path: "/ais" }, { label: "航标管理", path: "/buoy" }, { label: "引航日志", path: "/pilotlog" }]
</script>
