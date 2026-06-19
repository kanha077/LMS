<template>
  <div class="min-h-screen bg-slate-50 flex flex-col font-sans relative overflow-hidden text-slate-800">
    
    <!-- Animated Gradient Background Orbs -->
    <div class="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-orange-500/20 rounded-full blur-[120px] mix-blend-multiply pointer-events-none animate-pulse"></div>
    <div class="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-slate-300/40 rounded-full blur-[150px] mix-blend-multiply pointer-events-none"></div>
    <div class="absolute top-[40%] left-[60%] w-[30%] h-[30%] bg-orange-400/20 rounded-full blur-[100px] mix-blend-multiply pointer-events-none"></div>

    <!-- Glassmorphic Navbar -->
    <nav class="w-full fixed top-0 z-50 bg-white/70 backdrop-blur-lg border-b border-slate-200 px-6 py-4 flex justify-between items-center">
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 bg-gradient-to-br from-orange-500 to-orange-400 rounded-xl flex items-center justify-center shadow-lg shadow-orange-500/20">
          <span class="text-white font-bold text-xl">S</span>
        </div>
        <span class="text-2xl font-extrabold text-slate-900 tracking-tight">Sahayta</span>
      </div>
      <div class="space-x-6 flex items-center">
        <router-link to="/login" class="text-slate-600 hover:text-orange-500 font-medium transition-colors">Sign In</router-link>
        <router-link to="/register" class="relative group">
          <div class="absolute -inset-0.5 bg-orange-500 rounded-lg blur opacity-30 group-hover:opacity-70 transition duration-300"></div>
          <button class="relative bg-white backdrop-blur-sm border border-slate-200 text-slate-900 px-6 py-2.5 rounded-lg text-sm font-semibold transition-all hover:bg-slate-50">
            Get Started
          </button>
        </router-link>
      </div>
    </nav>

    <!-- Hero Section -->
    <main class="flex-grow flex flex-col items-center justify-center text-center px-4 pt-40 pb-20 relative z-10">
      <div class="inline-block mb-6 px-4 py-1.5 rounded-full bg-white/60 border border-slate-200 backdrop-blur-md shadow-sm">
        <span class="text-sm font-medium text-orange-600">✨ The next generation of learning</span>
      </div>
      
      <h1 class="text-5xl md:text-7xl font-extrabold mb-8 tracking-tight max-w-5xl leading-tight text-slate-900">
        Master your potential with <br />
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-orange-600 via-orange-400 to-slate-500 animate-gradient">limitless education.</span>
      </h1>
      
      <p class="text-lg md:text-xl text-slate-600 mb-12 max-w-2xl leading-relaxed">
        Sahayta delivers an immersive, high-performance ecosystem for educators and students. Build dynamic courses, track progress in real-time, and scale infinitely.
      </p>
      
      <div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-6">
        <router-link to="/register" class="relative group">
          <div class="absolute -inset-1 bg-orange-500 rounded-xl blur opacity-30 group-hover:opacity-60 transition duration-300"></div>
          <button class="relative bg-gradient-to-r from-orange-600 to-orange-500 text-white px-10 py-4 rounded-xl text-lg font-bold shadow-lg transition-all hover:scale-105">
            Start for Free
          </button>
        </router-link>
        <a href="#features" class="bg-white/80 backdrop-blur-md border border-slate-200 text-slate-800 px-10 py-4 rounded-xl text-lg font-bold hover:bg-white transition-all hover:scale-105 shadow-sm">
          Explore Features
        </a>
      </div>
    </main>

    <!-- Features Section -->
    <section id="features" class="relative z-10 py-24 px-6 border-t border-slate-200 bg-white/40">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-20">
          <h2 class="text-4xl md:text-5xl font-bold text-slate-900 tracking-tight">Built for the future.</h2>
          <p class="text-slate-600 mt-6 text-xl">Powerful tools wrapped in a beautiful, intuitive interface.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <div class="p-8 rounded-2xl bg-white/70 backdrop-blur-xl border border-slate-200 hover:-translate-y-2 hover:shadow-[0_15px_40px_rgba(249,115,22,0.15)] transition-all duration-300 group">
            <div class="w-14 h-14 bg-orange-50 border border-orange-100 rounded-xl flex items-center justify-center mb-6 text-orange-500 group-hover:scale-110 transition-transform shadow-sm">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-slate-800 mb-3">Dynamic Course Builder</h3>
            <p class="text-slate-600 leading-relaxed">Create comprehensive curriculums with drag-and-drop modules, lessons, and embedded rich media.</p>
          </div>

          <!-- Feature 2 -->
          <div class="p-8 rounded-2xl bg-white/70 backdrop-blur-xl border border-slate-200 hover:-translate-y-2 hover:shadow-[0_15px_40px_rgba(249,115,22,0.15)] transition-all duration-300 group">
            <div class="w-14 h-14 bg-orange-50 border border-orange-100 rounded-xl flex items-center justify-center mb-6 text-orange-500 group-hover:scale-110 transition-transform shadow-sm">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-slate-800 mb-3">Real-time Analytics</h3>
            <p class="text-slate-600 leading-relaxed">Track student progress, grading distributions, and completion rates with beautiful, data-rich dashboards.</p>
          </div>

          <!-- Feature 3 -->
          <div class="p-8 rounded-2xl bg-white/70 backdrop-blur-xl border border-slate-200 hover:-translate-y-2 hover:shadow-[0_15px_40px_rgba(100,116,139,0.15)] transition-all duration-300 group">
            <div class="w-14 h-14 bg-slate-100 border border-slate-200 rounded-xl flex items-center justify-center mb-6 text-slate-600 group-hover:scale-110 transition-transform shadow-sm">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-slate-800 mb-3">Multi-Tenant Scalability</h3>
            <p class="text-slate-600 leading-relaxed">Manage multiple institutions or departments securely from a single centralized admin panel.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="relative z-10 bg-white py-10 px-6 border-t border-slate-200">
      <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center text-slate-500 text-sm">
        <div class="mb-4 md:mb-0 flex items-center space-x-2">
          <span class="font-bold text-slate-800">Sahayta</span>
          <span>&copy; 2026 All rights reserved.</span>
        </div>
        <div class="space-x-6">
          <a href="#" class="hover:text-orange-500 transition-colors">Privacy Policy</a>
          <a href="#" class="hover:text-orange-500 transition-colors">Terms of Service</a>
          <a href="#" class="hover:text-orange-500 transition-colors">Contact</a>
        </div>
      </div>
    </footer>

  </div>
</template>

<script setup>
</script>

<style>
@keyframes gradient {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
.animate-gradient {
  background-size: 200% auto;
  animation: gradient 4s linear infinite;
}
</style>
