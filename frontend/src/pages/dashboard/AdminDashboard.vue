<template>
  <div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100 hover:shadow-md transition-all duration-200 transform hover:-translate-y-1">
        <h3 class="text-xs font-medium text-gray-500 uppercase tracking-widest">Total Users</h3>
        <p class="mt-3 text-4xl font-bold text-gray-900">1,240</p>
      </div>
      <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100 hover:shadow-md transition-all duration-200 transform hover:-translate-y-1">
        <h3 class="text-xs font-medium text-gray-500 uppercase tracking-widest">Active Tenants</h3>
        <p class="mt-3 text-4xl font-bold text-gray-900">5</p>
      </div>
      <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100 hover:shadow-md transition-all duration-200 transform hover:-translate-y-1">
        <h3 class="text-xs font-medium text-gray-500 uppercase tracking-widest">System Health</h3>
        <p class="mt-3 text-4xl font-bold text-green-600">99.9%</p>
      </div>
    </div>
    <div class="mt-10 bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <div class="px-6 py-5 border-b border-gray-100 bg-gray-50/50 flex justify-between items-center">
        <h2 class="text-lg font-medium text-gray-900">System Audit Logs</h2>
        <button class="text-blue-600 hover:text-blue-800 text-sm font-medium">Export CSV</button>
      </div>
      <div class="p-6">
        <p class="text-gray-500 text-sm">System running normally. No warnings detected.</p>
      </div>
    </div>
  </div>
</template>
