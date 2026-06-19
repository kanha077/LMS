<template>
  <div class="space-y-6">
    <!-- KPI Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid">
        <h3 class="text-[13px] font-medium text-ink-light dark:text-ink-mutedDark uppercase tracking-widest">Total Users</h3>
        <div class="mt-2 flex items-baseline gap-2">
          <p class="text-3xl font-bold text-ink-dark dark:text-surface-light">1,240</p>
          <span class="text-sm text-alert-success font-medium">+12%</span>
        </div>
      </div>
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid">
        <h3 class="text-[13px] font-medium text-ink-light dark:text-ink-mutedDark uppercase tracking-widest">Active Tenants</h3>
        <div class="mt-2 flex items-baseline gap-2">
          <p class="text-3xl font-bold text-ink-dark dark:text-surface-light">15</p>
          <span class="text-sm text-alert-success font-medium">+3</span>
        </div>
      </div>
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid">
        <h3 class="text-[13px] font-medium text-ink-light dark:text-ink-mutedDark uppercase tracking-widest">Courses Created</h3>
        <div class="mt-2 flex items-baseline gap-2">
          <p class="text-3xl font-bold text-ink-dark dark:text-surface-light">342</p>
          <span class="text-sm text-alert-success font-medium">+5%</span>
        </div>
      </div>
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid">
        <h3 class="text-[13px] font-medium text-ink-light dark:text-ink-mutedDark uppercase tracking-widest">System Health</h3>
        <div class="mt-2 flex items-baseline gap-2">
          <p class="text-3xl font-bold text-alert-success">99.9%</p>
        </div>
      </div>
    </div>

    <!-- Charts -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2 bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid">
        <h3 class="text-[15px] font-medium text-ink-dark dark:text-surface-light mb-4">User Signups (30 Days)</h3>
        <div class="h-64">
          <Line v-if="chartReady" :data="lineChartData" :options="lineOptions" />
        </div>
      </div>
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid">
        <h3 class="text-[15px] font-medium text-ink-dark dark:text-surface-light mb-4">Role Distribution</h3>
        <div class="h-64 flex items-center justify-center">
          <Doughnut v-if="chartReady" :data="donutChartData" :options="donutOptions" />
        </div>
      </div>
    </div>

    <!-- Audit Logs Preview -->
    <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid overflow-hidden">
      <div class="px-6 py-4 border-b border-ink-lightest dark:border-ink-mid bg-surface-offwhite dark:bg-surface-dark flex justify-between items-center">
        <h2 class="text-[18px] font-medium text-ink-dark dark:text-surface-light">Recent Audit Logs</h2>
        <BaseButton variant="outline" size="sm">View All</BaseButton>
      </div>
      <div class="p-0 overflow-x-auto">
        <table class="w-full text-left text-[13px]">
          <thead class="bg-surface-offwhite dark:bg-surface-dark text-ink-light dark:text-ink-mutedDark border-b border-ink-lightest dark:border-ink-mid">
            <tr>
              <th class="px-6 py-3 font-medium">Timestamp</th>
              <th class="px-6 py-3 font-medium">User</th>
              <th class="px-6 py-3 font-medium">Action</th>
              <th class="px-6 py-3 font-medium">IP Address</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-ink-lightest dark:divide-ink-mid text-ink-dark dark:text-surface-light">
            <tr class="hover:bg-surface-offwhite dark:hover:bg-ink-dark transition-colors">
              <td class="px-6 py-3">10 mins ago</td>
              <td class="px-6 py-3 font-medium">admin@test.com</td>
              <td class="px-6 py-3"><span class="px-2 py-1 rounded bg-brand-accent/10 text-brand-accent">Tenant Updated</span></td>
              <td class="px-6 py-3">192.168.1.1</td>
            </tr>
            <tr class="hover:bg-surface-offwhite dark:hover:bg-ink-dark transition-colors">
              <td class="px-6 py-3">1 hour ago</td>
              <td class="px-6 py-3 font-medium">teacher@gtu.edu</td>
              <td class="px-6 py-3"><span class="px-2 py-1 rounded bg-alert-info/10 text-alert-info">Course Created</span></td>
              <td class="px-6 py-3">10.0.0.5</td>
            </tr>
            <tr class="hover:bg-surface-offwhite dark:hover:bg-ink-dark transition-colors">
              <td class="px-6 py-3">2 hours ago</td>
              <td class="px-6 py-3 font-medium">student@gtu.edu</td>
              <td class="px-6 py-3"><span class="px-2 py-1 rounded bg-alert-success/10 text-alert-success">Quiz Passed</span></td>
              <td class="px-6 py-3">172.16.0.4</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend, ArcElement } from 'chart.js';
import { Line, Doughnut } from 'vue-chartjs';
import BaseButton from '../../components/ui/BaseButton.vue';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend, ArcElement);

const chartReady = ref(false);

onMounted(() => {
  chartReady.value = true;
});

const lineChartData = {
  labels: ['Jan 1', 'Jan 5', 'Jan 10', 'Jan 15', 'Jan 20', 'Jan 25', 'Jan 30'],
  datasets: [
    {
      label: 'New Signups',
      backgroundColor: '#1E3A5F',
      borderColor: '#1E3A5F',
      data: [12, 19, 15, 25, 22, 30, 45],
      tension: 0.3
    }
  ]
};

const lineOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { display: false }
  },
  scales: {
    y: { beginAtZero: true, grid: { color: '#E5E7EB' } },
    x: { grid: { display: false } }
  }
};

const donutChartData = {
  labels: ['Students', 'Teachers', 'Admins'],
  datasets: [
    {
      backgroundColor: ['#1E3A5F', '#9CA3AF', '#374151'],
      data: [85, 10, 5]
    }
  ]
};

const donutOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { position: 'bottom' }
  }
};
</script>
