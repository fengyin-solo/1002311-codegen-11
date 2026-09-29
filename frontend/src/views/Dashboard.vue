<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "引航申请", "created": 0, "pending": 0, "abnormal": 0}, {"name": "引航员管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "拖轮调度", "created": 0, "pending": 0, "abnormal": 0}, {"name": "潮汐监测", "created": 0, "pending": 0, "abnormal": 0}, {"name": "泊位管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "锚地管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "航道管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "船舶动态", "created": 0, "pending": 0, "abnormal": 0}, {"name": "引航排班", "created": 0, "pending": 0, "abnormal": 0}, {"name": "危险品船舶管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "气象预警", "created": 0, "pending": 0, "abnormal": 0}, {"name": "引航费管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "海事事件管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "AIS设备管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "航标管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "引航日志", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>
