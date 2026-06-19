<template>
  <div class="bg-background text-text-primary font-body-main antialiased overflow-x-hidden">
    <!-- TopNavBar -->
    <nav class="sticky top-0 z-50 flex justify-between items-center px-lg py-md max-w-max-content-width mx-auto bg-surface border-b border-border-soft">
      <div class="flex items-center gap-base">
        <span class="font-display-hero text-headline-md text-primary">Sahayta</span>
      </div>
      <div class="hidden md:flex items-center gap-xl">
        <a class="font-nav-link text-nav-link text-on-surface-variant hover:text-secondary transition-colors duration-200" href="#features">Courses</a>
        <a class="font-nav-link text-nav-link text-on-surface-variant hover:text-secondary transition-colors duration-200" href="#">Institutions</a>
        <a class="font-nav-link text-nav-link text-on-surface-variant hover:text-secondary transition-colors duration-200" href="#">Solutions</a>
        <a class="font-nav-link text-nav-link text-on-surface-variant hover:text-secondary transition-colors duration-200" href="#">Pricing</a>
        <a class="font-nav-link text-nav-link text-on-surface-variant hover:text-secondary transition-colors duration-200" href="#">About</a>
      </div>
      <div class="flex items-center gap-md">
        <router-link to="/login" class="hidden sm:block font-button-text text-button-text px-md py-xs text-primary cursor-pointer active:scale-95 transition-all">Log In</router-link>
        <router-link to="/register" class="font-button-text text-button-text bg-saffron text-white px-lg py-xs rounded-full cursor-pointer hover:bg-accent-hover active:scale-95 transition-all">Get Started</router-link>
      </div>
    </nav>
    
    <!-- Hero Section -->
    <header class="hero-gradient relative overflow-hidden py-3xl lg:py-[120px]">
      <div class="absolute inset-0 opacity-20 pointer-events-none"></div>
      <div class="max-w-max-content-width mx-auto px-lg grid lg:grid-cols-2 gap-2xl items-center relative z-10">
        <div class="space-y-xl text-center lg:text-left">
          <h1 class="font-display-hero text-display-hero text-white max-w-xl">The Modern Operating System for Education</h1>
          <p class="font-body-main text-[18px] text-[#C4C2E8] leading-relaxed max-w-lg mx-auto lg:mx-0">
            Build courses, engage learners, and scale your impact — all from one beautifully simple platform.
          </p>
          <div class="flex flex-col sm:flex-row gap-md justify-center lg:justify-start pt-md">
            <button class="font-button-text text-button-text bg-saffron text-white px-3xl py-md rounded-full hover:bg-accent-hover active:scale-95 transition-all">Start for Free</button>
            <button class="font-button-text text-button-text border-2 border-white text-white px-3xl py-md rounded-full hover:bg-white/10 active:scale-95 transition-all">See a Demo</button>
          </div>
        </div>
        <div class="relative mt-xl lg:mt-0">
          <div class="bg-surface-container/10 backdrop-blur-md border border-white/10 rounded-xl p-base card-shadow overflow-hidden group">
            <img class="w-full h-auto rounded-lg shadow-2xl transform transition-transform duration-700 group-hover:scale-[1.02]" src="https://lh3.googleusercontent.com/aida-public/AB6AXuALtEvvudy67z2SG1z6B2zEaoKa-u0bfD_z5uoExr-jk-jdkCMzgwz0BzlcuHEeAhytUF2BiDQPoB1JAEBnQ3dUKiq86G2rSe7O34qBcjNkMHrjjKLDjeIn5HIHU7F2Hl6irVzS-ol--_t0RLTXH7T6OLJNHI3ceXDmYNRPJYcn0totHDdbFLkDo1k8wNKr0ZbUeohyrSVlRJcABwoNzOwWzPxaS_OGbiQlcAbAtpDnZiHHZWlcTnApphVt4w_Qv9gjwTBVHlD_tvM_" alt="Sahayta LMS Dashboard Mockup"/>
          </div>
          <!-- Ambient Glow Decoration -->
          <div class="absolute -top-10 -right-10 w-64 h-64 bg-saffron/20 rounded-full blur-[100px] -z-10 animate-pulse"></div>
          <div class="absolute -bottom-10 -left-10 w-64 h-64 bg-primary/40 rounded-full blur-[100px] -z-10"></div>
        </div>
      </div>
    </header>
    
    <!-- Stats Bar -->
    <section class="bg-surface border-b border-border-soft relative z-20">
      <div class="max-w-max-content-width mx-auto px-lg py-xl">
        <div class="flex flex-col md:flex-row justify-around items-center gap-xl md:gap-0">
          <div class="text-center px-lg animation-target">
            <div class="font-display-hero text-headline-lg text-primary">50,000+</div>
            <div class="font-label-caps text-label-caps text-outline uppercase tracking-wider mt-xs">Learners</div>
          </div>
          <div class="w-px h-12 bg-border-soft hidden md:block"></div>
          <div class="text-center px-lg animation-target">
            <div class="font-display-hero text-headline-lg text-primary">2,000+</div>
            <div class="font-label-caps text-label-caps text-outline uppercase tracking-wider mt-xs">Courses</div>
          </div>
          <div class="w-px h-12 bg-border-soft hidden md:block"></div>
          <div class="text-center px-lg animation-target">
            <div class="font-display-hero text-headline-lg text-primary">98%</div>
            <div class="font-label-caps text-label-caps text-outline uppercase tracking-wider mt-xs">Satisfaction</div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- Features Section -->
    <section class="py-3xl bg-surface-container-lowest" id="features">
      <div class="max-w-max-content-width mx-auto px-lg">
        <div class="text-center mb-2xl animation-target">
          <span class="font-label-caps text-label-caps text-saffron uppercase tracking-[0.2em] font-semibold">What We Offer</span>
          <h2 class="font-headline-lg text-headline-lg text-primary mt-sm">Everything educators need, nothing they don't</h2>
        </div>
        <div class="grid md:grid-cols-3 gap-xl">
          <!-- Feature Card 1 -->
          <div class="animation-target bg-white p-2xl rounded-lg border border-border-soft card-shadow hover:-translate-y-1 transition-all duration-300">
            <div class="w-12 h-12 bg-saffron/10 rounded-lg flex items-center justify-center mb-lg">
              <span class="material-icons-outlined text-saffron text-[28px]">extension</span>
            </div>
            <h3 class="font-title-card text-title-card text-primary mb-md">Drag-and-Drop Course Builder</h3>
            <p class="font-body-sm text-body-sm text-on-surface-variant leading-relaxed">
              Build comprehensive curriculums in minutes with our intuitive visual editor. No technical skills required.
            </p>
          </div>
          <!-- Feature Card 2 -->
          <div class="animation-target bg-white p-2xl rounded-lg border border-border-soft card-shadow hover:-translate-y-1 transition-all duration-300">
            <div class="w-12 h-12 bg-saffron/10 rounded-lg flex items-center justify-center mb-lg">
              <span class="material-icons-outlined text-saffron text-[28px]">analytics</span>
            </div>
            <h3 class="font-title-card text-title-card text-primary mb-md">Real-Time Analytics</h3>
            <p class="font-body-sm text-body-sm text-on-surface-variant leading-relaxed">
              Track student progress, completion rates, and grades in real-time. Gain deep insights into learning outcomes.
            </p>
          </div>
          <!-- Feature Card 3 -->
          <div class="animation-target bg-white p-2xl rounded-lg border border-border-soft card-shadow hover:-translate-y-1 transition-all duration-300">
            <div class="w-12 h-12 bg-saffron/10 rounded-lg flex items-center justify-center mb-lg">
              <span class="material-icons-outlined text-saffron text-[28px]">corporate_fare</span>
            </div>
            <h3 class="font-title-card text-title-card text-primary mb-md">Multi-Tenant Architecture</h3>
            <p class="font-body-sm text-body-sm text-on-surface-variant leading-relaxed">
              Manage multiple institutions, campuses, or departments from a single centralized dashboard seamlessly.
            </p>
          </div>
        </div>
      </div>
    </section>
    
    <!-- Social Proof / Testimonial -->
    <section class="bg-surface-muted py-3xl overflow-hidden relative">
      <div class="max-w-max-content-width mx-auto px-lg relative z-10 animation-target">
        <div class="max-w-3xl mx-auto text-center">
          <div class="mb-lg">
            <span class="material-icons-outlined text-border-soft text-[64px]" style="font-variation-settings: 'FILL' 1;">format_quote</span>
          </div>
          <blockquote class="font-display-hero text-headline-md italic text-primary leading-tight md:text-[36px] mb-xl">
            "Sahayta has completely transformed how our faculty delivers content. The focus on structured calm and high-performance tools makes it the most effective platform we've ever used."
          </blockquote>
          <div class="flex items-center justify-center gap-md">
            <div class="w-12 h-12 rounded-full overflow-hidden border-2 border-white shadow-md">
              <img class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCVX54eYoqA1H6TwsPbpsSWfH-666eTyQ-QpAsQP9uM5Bo_UMVFRqd6REGJCg3Ne97tk4MX8p5jX4_hg1sTFBvhU8GGXyjcsz58LS_LiTvRd2WkeQZkQpdF0Ei9zZUC_Iq46iRcYhKkzWFfDdBA0AZOOh-NCtofPiW2xybJeJvkSf5Yd3e9kBa_NUJll-e91vetlpIK8xzVx2dPEhu0sPlfLs9NbKtOsB9HBtA04C1h7fK7Z67cQI5Y-kQc2OkECr4mznhwYC0TCiPL" alt="Educator"/>
            </div>
            <div class="text-left">
              <p class="font-title-card text-body-main text-primary font-semibold">Dr. Ananya Sharma</p>
              <p class="font-body-sm text-body-sm text-outline">Dean of Innovation, Prestige Institute</p>
            </div>
          </div>
        </div>
      </div>
      <!-- Decorative Background Element -->
      <div class="absolute top-0 right-0 transform translate-x-1/2 -translate-y-1/2 opacity-5">
        <span class="material-icons-outlined text-[400px]">school</span>
      </div>
    </section>
    
    <!-- Final CTA Section -->
    <section class="hero-gradient py-3xl text-center relative overflow-hidden">
      <div class="absolute inset-0 opacity-10 pointer-events-none"></div>
      <div class="max-w-max-content-width mx-auto px-lg relative z-10 animation-target">
        <h2 class="font-display-hero text-display-hero-mobile md:text-display-hero text-white mb-xl">Ready to transform how you teach?</h2>
        <button class="font-button-text text-button-text bg-saffron text-white px-3xl py-md rounded-full hover:bg-accent-hover active:scale-95 transition-all shadow-xl shadow-saffron/20">Get Started Free</button>
        <p class="text-[#C4C2E8] font-body-sm mt-lg">No credit card required. Cancel anytime.</p>
      </div>
    </section>
    
    <!-- Footer -->
    <footer class="bg-primary text-on-primary w-full py-3xl px-lg flex flex-col md:flex-row justify-between items-start md:items-center gap-xl border-t border-white/5">
      <div class="space-y-md max-w-xs">
        <span class="font-display-hero text-headline-md text-on-primary">Sahayta</span>
        <p class="font-body-sm text-body-sm text-[#9896B8] leading-relaxed">
          © 2024 Sahayta LMS. Empowering Authority in Education. Built for institutions that demand excellence.
        </p>
      </div>
      <div class="grid grid-cols-2 sm:grid-cols-3 gap-xl">
        <div class="space-y-sm">
          <p class="font-label-caps text-label-caps text-white uppercase opacity-50">Platform</p>
          <ul class="space-y-xs">
            <li><a class="font-body-sm text-body-sm text-[#9896B8] hover:text-white transition-colors" href="#">Courses</a></li>
            <li><a class="font-body-sm text-body-sm text-[#9896B8] hover:text-white transition-colors" href="#">Analytics</a></li>
            <li><a class="font-body-sm text-body-sm text-[#9896B8] hover:text-white transition-colors" href="#">Security</a></li>
          </ul>
        </div>
        <div class="space-y-sm">
          <p class="font-label-caps text-label-caps text-white uppercase opacity-50">Legal</p>
          <ul class="space-y-xs">
            <li><a class="font-body-sm text-body-sm text-[#9896B8] hover:text-white transition-colors" href="#">Privacy Policy</a></li>
            <li><a class="font-body-sm text-body-sm text-[#9896B8] hover:text-white transition-colors" href="#">Terms of Service</a></li>
            <li><a class="font-body-sm text-body-sm text-[#9896B8] hover:text-white transition-colors" href="#">Cookie Policy</a></li>
          </ul>
        </div>
        <div class="space-y-sm">
          <p class="font-label-caps text-label-caps text-white uppercase opacity-50">Support</p>
          <ul class="space-y-xs">
            <li><a class="font-body-sm text-body-sm text-[#9896B8] hover:text-white transition-colors" href="#">Help Center</a></li>
            <li><a class="font-body-sm text-body-sm text-[#9896B8] hover:text-white transition-colors" href="#">Contact Support</a></li>
          </ul>
        </div>
      </div>
      <div class="flex gap-md self-start md:self-center">
        <a class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-saffron transition-all group" href="#">
          <span class="material-icons-outlined text-[#9896B8] group-hover:text-white">language</span>
        </a>
        <a class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-saffron transition-all group" href="#">
          <span class="material-icons-outlined text-[#9896B8] group-hover:text-white">mail</span>
        </a>
        <a class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-saffron transition-all group" href="#">
          <span class="material-icons-outlined text-[#9896B8] group-hover:text-white">share</span>
        </a>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  // Smooth scroll for nav links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault()
      const target = document.querySelector(this.getAttribute('href'))
      if(target) {
        target.scrollIntoView({
          behavior: 'smooth'
        })
      }
    })
  })

  // Simple visibility observer for scroll animations
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('opacity-100')
        entry.target.classList.remove('opacity-0', 'translate-y-10')
      }
    })
  }, { threshold: 0.1 })

  document.querySelectorAll('.animation-target').forEach(el => {
    el.classList.add('transition-all', 'duration-700', 'opacity-0', 'translate-y-10')
    observer.observe(el)
  })
})
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Icons+Outlined');

.hero-gradient {
  background: linear-gradient(135deg, #1E1B4B 0%, #070235 100%);
}
.card-shadow {
  box-shadow: 0 1px 4px rgba(30, 27, 75, 0.08);
}
</style>
