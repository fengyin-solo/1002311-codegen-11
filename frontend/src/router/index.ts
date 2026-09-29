import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const PilotageApp = () => import('@/views/pilotage_app/index.vue')
const Pilot = () => import('@/views/pilot/index.vue')
const Tug = () => import('@/views/tug/index.vue')
const Tide = () => import('@/views/tide/index.vue')
const Berth = () => import('@/views/berth/index.vue')
const Anchorage = () => import('@/views/anchorage/index.vue')
const Channel = () => import('@/views/channel/index.vue')
const Vts = () => import('@/views/vts/index.vue')
const Schedule = () => import('@/views/schedule/index.vue')
const Cargo = () => import('@/views/cargo/index.vue')
const Weather = () => import('@/views/weather/index.vue')
const Fee = () => import('@/views/fee/index.vue')
const Incident = () => import('@/views/incident/index.vue')
const Ais = () => import('@/views/ais/index.vue')
const Buoy = () => import('@/views/buoy/index.vue')
const Pilotlog = () => import('@/views/pilotlog/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/pilotage_app', name: 'pilotage_app', component: PilotageApp },
    { path: '/pilot', name: 'pilot', component: Pilot },
    { path: '/tug', name: 'tug', component: Tug },
    { path: '/tide', name: 'tide', component: Tide },
    { path: '/berth', name: 'berth', component: Berth },
    { path: '/anchorage', name: 'anchorage', component: Anchorage },
    { path: '/channel', name: 'channel', component: Channel },
    { path: '/vts', name: 'vts', component: Vts },
    { path: '/schedule', name: 'schedule', component: Schedule },
    { path: '/cargo', name: 'cargo', component: Cargo },
    { path: '/weather', name: 'weather', component: Weather },
    { path: '/fee', name: 'fee', component: Fee },
    { path: '/incident', name: 'incident', component: Incident },
    { path: '/ais', name: 'ais', component: Ais },
    { path: '/buoy', name: 'buoy', component: Buoy },
    { path: '/pilotlog', name: 'pilotlog', component: Pilotlog },
  ],
})

export default router
