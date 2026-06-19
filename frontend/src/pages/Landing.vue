<template>
  <div class="min-h-screen bg-slate-50 flex flex-col font-sans">
    
    <!-- Navbar -->
    <nav class="w-full bg-white border-b border-slate-200 px-6 py-4 flex justify-between items-center shadow-sm">
      <div class="flex items-center space-x-2">
        <div class="w-8 h-8 bg-[#1E3A5F] rounded flex items-center justify-center">
          <span class="text-white font-bold text-lg">S</span>
        </div>
        <span class="text-xl font-bold text-slate-800 tracking-tight">Sahayta</span>
      </div>
      <div class="space-x-4">
        <router-link to="/login" class="text-slate-600 hover:text-[#1E3A5F] font-medium transition-colors">Sign In</router-link>
        <router-link to="/register" class="bg-[#1E3A5F] text-white px-5 py-2.5 rounded text-sm font-semibold hover:bg-slate-700 transition-colors shadow-sm">Get Started</router-link>
      </div>
    </nav>

    <!-- Hero Section -->
    <main class="flex-grow flex flex-col items-center justify-center text-center px-4 py-20">
      <h1 class="text-5xl md:text-6xl font-extrabold text-slate-900 mb-6 tracking-tight max-w-4xl">
        The complete platform for <span class="text-[#1E3A5F]">modern learning.</span>
      </h1>
      <p class="text-lg md:text-xl text-slate-600 mb-10 max-w-2xl">
        Sahayta empowers educators and students with powerful course building tools, real-time analytics, and seamless tenant management in one clean, professional workspace.
      </p>
      
      <div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4">
        <router-link to="/register" class="bg-[#1E3A5F] text-white px-8 py-3.5 rounded-md text-lg font-semibold hover:bg-slate-700 transition-colors shadow-md">
          Start for Free
        </router-link>
        <a href="#features" class="bg-white text-[#1E3A5F] border border-slate-300 px-8 py-3.5 rounded-md text-lg font-semibold hover:bg-slate-50 transition-colors shadow-sm">
          Explore Features
        </a>
      </div>
    </main>

    <!-- Features Section -->
    <section id="features" class="bg-white border-t border-slate-200 py-20 px-6">
      <div class="max-w-6xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold text-slate-900 tracking-tight">Everything you need to succeed</h2>
          <p class="text-slate-500 mt-4 text-lg">Designed for scale, simplicity, and performance.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <div class="p-6 border border-slate-200 rounded bg-slate-50 hover:shadow-md transition-shadow">
            <div class="w-12 h-12 bg-white border border-slate-200 rounded flex items-center justify-center mb-4 text-[#1E3A5F]">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
            </div>
            <h3 class="text-xl font-bold text-slate-800 mb-2">Dynamic Course Builder</h3>
            <p class="text-slate-600">Create comprehensive curriculums with drag-and-drop modules, lessons, and embedded rich media.</p>
          </div>

          <!-- Feature 2 -->
          <div class="p-6 border border-slate-200 rounded bg-slate-50 hover:shadow-md transition-shadow">
            <div class="w-12 h-12 bg-white border border-slate-200 rounded flex items-center justify-center mb-4 text-[#1E3A5F]">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <h3 class="text-xl font-bold text-slate-800 mb-2">Real-time Analytics</h3>
            <p class="text-slate-600">Track student progress, grading distributions, and completion rates with beautiful, data-rich dashboards.</p>
          </div>

          <!-- Feature 3 -->
          <div class="p-6 border border-slate-200 rounded bg-slate-50 hover:shadow-md transition-shadow">
            <div class="w-12 h-12 bg-white border border-slate-200 rounded flex items-center justify-center mb-4 text-[#1E3A5F]">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
              </svg>
            </div>
            <h3 class="text-xl font-bold text-slate-800 mb-2">Multi-Tenant Architecture</h3>
            <p class="text-slate-600">Manage multiple institutions or departments securely from a single centralized admin panel.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-900 py-10 px-6 border-t border-slate-800">
      <div class="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-center text-slate-400 text-sm">
        <div class="mb-4 md:mb-0">
          &copy; 2026 Sahayta LMS. All rights reserved.
        </div>
        <div class="space-x-6">
          <a href="#" class="hover:text-white transition-colors">Privacy Policy</a>
          <a href="#" class="hover:text-white transition-colors">Terms of Service</a>
          <a href="#" class="hover:text-white transition-colors">Contact</a>
        </div>
      </div>
    </footer>

  </div>
</template>

<script setup>
// Landing page uses standard Tailwind utilities built into the project. No extra logic needed.
</script>
