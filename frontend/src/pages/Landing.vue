<template>
  <div class="min-h-screen bg-slate-950 flex flex-col font-sans relative overflow-hidden text-slate-200">
    
    <!-- Animated Gradient Background Orbs -->
    <div class="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-purple-600/30 rounded-full blur-[120px] mix-blend-screen pointer-events-none animate-pulse"></div>
    <div class="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-blue-600/20 rounded-full blur-[150px] mix-blend-screen pointer-events-none"></div>
    <div class="absolute top-[40%] left-[60%] w-[30%] h-[30%] bg-indigo-500/20 rounded-full blur-[100px] mix-blend-screen pointer-events-none"></div>

    <!-- Glassmorphic Navbar -->
    <nav class="w-full fixed top-0 z-50 bg-white/5 backdrop-blur-lg border-b border-white/10 px-6 py-4 flex justify-between items-center">
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 bg-gradient-to-br from-purple-500 to-blue-500 rounded-xl flex items-center justify-center shadow-lg shadow-purple-500/30">
          <span class="text-white font-bold text-xl">S</span>
        </div>
        <span class="text-2xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-purple-200 to-blue-200 tracking-tight">Sahayta</span>
      </div>
      <div class="space-x-6 flex items-center">
        <router-link to="/login" class="text-slate-300 hover:text-white font-medium transition-colors">Sign In</router-link>
        <router-link to="/register" class="relative group">
          <div class="absolute -inset-0.5 bg-gradient-to-r from-purple-500 to-blue-500 rounded-lg blur opacity-60 group-hover:opacity-100 transition duration-300"></div>
          <button class="relative bg-slate-900/80 backdrop-blur-sm border border-white/10 text-white px-6 py-2.5 rounded-lg text-sm font-semibold transition-all">
            Get Started
          </button>
        </router-link>
      </div>
    </nav>

    <!-- Hero Section -->
    <main class="flex-grow flex flex-col items-center justify-center text-center px-4 pt-40 pb-20 relative z-10">
      <div class="inline-block mb-6 px-4 py-1.5 rounded-full bg-white/5 border border-white/10 backdrop-blur-md">
        <span class="text-sm font-medium text-purple-300">✨ The next generation of learning</span>
      </div>
      
      <h1 class="text-5xl md:text-7xl font-extrabold mb-8 tracking-tight max-w-5xl leading-tight">
        Master your potential with <br />
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 via-fuchsia-400 to-blue-400 animate-gradient">limitless education.</span>
      </h1>
      
      <p class="text-lg md:text-xl text-slate-400 mb-12 max-w-2xl leading-relaxed">
        Sahayta delivers an immersive, high-performance ecosystem for educators and students. Build dynamic courses, track progress in real-time, and scale infinitely.
      </p>
      
      <div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-6">
        <router-link to="/register" class="relative group">
          <div class="absolute -inset-1 bg-gradient-to-r from-purple-600 to-blue-600 rounded-xl blur opacity-70 group-hover:opacity-100 transition duration-300"></div>
          <button class="relative bg-gradient-to-r from-purple-500 to-blue-500 text-white px-10 py-4 rounded-xl text-lg font-bold shadow-xl transition-all hover:scale-105">
            Start for Free
          </button>
        </router-link>
        <a href="#features" class="bg-white/5 backdrop-blur-md border border-white/10 text-white px-10 py-4 rounded-xl text-lg font-bold hover:bg-white/10 transition-all hover:scale-105">
          Explore Features
        </a>
      </div>
    </main>

    <!-- Features Section -->
    <section id="features" class="relative z-10 py-24 px-6 border-t border-white/10 bg-black/20">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-20">
          <h2 class="text-4xl md:text-5xl font-bold text-white tracking-tight">Built for the future.</h2>
          <p class="text-slate-400 mt-6 text-xl">Powerful tools wrapped in a beautiful, intuitive interface.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <div class="p-8 rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 hover:-translate-y-2 hover:shadow-[0_0_40px_rgba(168,85,247,0.15)] transition-all duration-300 group">
            <div class="w-14 h-14 bg-gradient-to-br from-purple-500/20 to-blue-500/20 border border-purple-500/30 rounded-xl flex items-center justify-center mb-6 text-purple-400 group-hover:scale-110 transition-transform">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-white mb-3">Dynamic Course Builder</h3>
            <p class="text-slate-400 leading-relaxed">Create comprehensive curriculums with drag-and-drop modules, lessons, and embedded rich media.</p>
          </div>

          <!-- Feature 2 -->
          <div class="p-8 rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 hover:-translate-y-2 hover:shadow-[0_0_40px_rgba(59,130,246,0.15)] transition-all duration-300 group">
            <div class="w-14 h-14 bg-gradient-to-br from-blue-500/20 to-cyan-500/20 border border-blue-500/30 rounded-xl flex items-center justify-center mb-6 text-blue-400 group-hover:scale-110 transition-transform">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-white mb-3">Real-time Analytics</h3>
            <p class="text-slate-400 leading-relaxed">Track student progress, grading distributions, and completion rates with beautiful, data-rich dashboards.</p>
          </div>

          <!-- Feature 3 -->
          <div class="p-8 rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 hover:-translate-y-2 hover:shadow-[0_0_40px_rgba(236,72,153,0.15)] transition-all duration-300 group">
            <div class="w-14 h-14 bg-gradient-to-br from-pink-500/20 to-rose-500/20 border border-pink-500/30 rounded-xl flex items-center justify-center mb-6 text-pink-400 group-hover:scale-110 transition-transform">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-white mb-3">Multi-Tenant Scalability</h3>
            <p class="text-slate-400 leading-relaxed">Manage multiple institutions or departments securely from a single centralized admin panel.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="relative z-10 bg-black/40 py-10 px-6 border-t border-white/10 backdrop-blur-md">
      <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center text-slate-500 text-sm">
        <div class="mb-4 md:mb-0 flex items-center space-x-2">
          <span class="font-bold text-slate-300">Sahayta</span>
          <span>&copy; 2026 All rights reserved.</span>
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
