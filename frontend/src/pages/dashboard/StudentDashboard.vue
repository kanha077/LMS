<template>
  <div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100 hover:shadow-md transition-all duration-200 transform hover:-translate-y-1">
        <h3 class="text-xs font-medium text-gray-500 uppercase tracking-widest">Enrolled Courses</h3>
        <p class="mt-3 text-4xl font-bold text-gray-900">4</p>
      </div>
      <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100 hover:shadow-md transition-all duration-200 transform hover:-translate-y-1">
        <h3 class="text-xs font-medium text-gray-500 uppercase tracking-widest">Pending Assignments</h3>
        <p class="mt-3 text-4xl font-bold text-gray-900">2</p>
      </div>
      <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100 hover:shadow-md transition-all duration-200 transform hover:-translate-y-1">
        <h3 class="text-xs font-medium text-gray-500 uppercase tracking-widest">Overall GPA</h3>
        <p class="mt-3 text-4xl font-bold text-green-600">3.8</p>
      </div>
    </div>
    <div class="mt-10 bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <div class="px-6 py-5 border-b border-gray-100 bg-gray-50/50">
        <h2 class="text-lg font-medium text-gray-900">Upcoming Deadlines</h2>
      </div>
      <div class="p-6">
        <div class="flex items-center text-sm text-gray-500">
          <svg class="w-5 h-5 mr-2 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          No upcoming deadlines. You're all caught up!
        </div>
      </div>
    </div>
  </div>
</template>
