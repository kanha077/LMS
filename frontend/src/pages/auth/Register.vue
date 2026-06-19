<template>
  <div>
    <main class="min-h-screen flex flex-col md:flex-row overflow-hidden">
      <!-- Left Side: Branding & Inspiration (40%) -->
      <section class="hidden md:flex md:w-[40%] bg-primary-container relative flex-col justify-between p-2xl overflow-hidden">
        <!-- Animated Background Gradient Layer -->
        <div class="absolute inset-0 glow-accent pointer-events-none opacity-40"></div>
        <!-- Logo Section -->
        <div class="relative z-10">
          <span class="font-display-hero text-headline-lg text-white">Sahayta</span>
        </div>
        <!-- Motivational Quote -->
        <div class="relative z-10 mb-3xl">
          <h1 class="font-display-hero text-headline-lg text-white leading-tight max-w-sm">
            Limitless education, effortless management.
          </h1>
          <div class="w-16 h-1 bg-secondary-container mt-lg rounded-full"></div>
        </div>
        <!-- Footer Branding Info -->
        <div class="relative z-10">
          <p class="text-on-primary-container font-body-sm opacity-60">
            Trusted by 500+ institutions worldwide.
          </p>
        </div>
        <!-- Background Decorative Image -->
        <div class="absolute bottom-0 right-0 w-full h-1/2 opacity-20 pointer-events-none">
          <div class="absolute inset-0 bg-gradient-to-t from-primary-container to-transparent z-20"></div>
          <div class="w-full h-full" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuAEBo4z-KkIM_mhFIgX_hIFxiJqSGV_fUCsaagJVBVIMl6ZD9DlxIzWFlyL8GRMVj2Rj3RTusLbJhtU6tflMfUAkuCxIX55Jxsi_GPsyt1MpvATGrEPldzI5cAXWaYeZiMY43KWdOLUeKhDfs5VbZCAg9_HVsSPNwCIF-HpJpYx2-aubIWPiM8MTzedB224qRVmir2kTT3-NfqyNyju19U1r6f0SGUcN3_K9os6jzAHTOCwRP77Di9PPi3Tmtw1BRCxsMYx5m2zG-lE')"></div>
        </div>
      </section>
      
      <!-- Right Side: Authentication Forms (60%) -->
      <section class="w-full md:w-[60%] bg-surface-container-lowest flex flex-col items-center justify-center p-md md:p-2xl min-h-screen">
        <div class="w-full max-w-md space-y-xl">
          <!-- Mobile Logo -->
          <div class="md:hidden flex justify-center mb-xl">
            <span class="font-display-hero text-headline-md text-primary">Sahayta</span>
          </div>
          <!-- Form Header -->
          <div class="text-center md:text-left space-y-xs">
            <h2 class="font-headline-md text-primary-container">
              {{ isLogin ? 'Welcome back to Sahayta' : 'Create your account' }}
            </h2>
            <p class="text-on-surface-variant font-body-sm">
              {{ isLogin ? 'Access your personalized learning authority.' : 'Join 500+ institutions worldwide.' }}
            </p>
          </div>
          
          <!-- Toggle Switch -->
          <div class="flex justify-center md:justify-start">
            <div class="bg-surface-container-low p-xs rounded-full flex items-center w-fit border border-border-soft relative">
              <button @click="isLogin = true" :class="[isLogin ? 'bg-secondary-container text-white shadow-sm' : 'text-on-surface-variant hover:text-primary', 'px-xl py-xs rounded-full font-button-text text-button-text transition-all duration-300 relative z-10']">
                Sign In
              </button>
              <button @click="isLogin = false" :class="[!isLogin ? 'bg-secondary-container text-white shadow-sm' : 'text-on-surface-variant hover:text-primary', 'px-xl py-xs rounded-full font-button-text text-button-text transition-all duration-300 relative z-10']">
                Create Account
              </button>
            </div>
          </div>
          
          <!-- Login Form -->
          <form class="space-y-lg" @submit.prevent>
            <div v-if="!isLogin" class="space-y-xs transition-all duration-300">
              <label class="font-label-caps text-label-caps text-on-surface-variant" for="name">FULL NAME</label>
              <input class="w-full h-[44px] px-md rounded-lg border border-border-soft bg-white text-body-main placeholder:text-outline/50 form-input-focus transition-all outline-none focus:border-secondary-container focus:ring-1 focus:ring-secondary-container" id="name" placeholder="Priya Sharma" type="text" />
            </div>
          
            <div class="space-y-xs">
              <label class="font-label-caps text-label-caps text-on-surface-variant" for="email">EMAIL ADDRESS</label>
              <input class="w-full h-[44px] px-md rounded-lg border border-border-soft bg-white text-body-main placeholder:text-outline/50 form-input-focus transition-all outline-none focus:border-secondary-container focus:ring-1 focus:ring-secondary-container" id="email" placeholder="name@institution.edu" type="email" />
            </div>
            
            <div class="space-y-xs">
              <div class="flex justify-between items-end">
                <label class="font-label-caps text-label-caps text-on-surface-variant" for="password">PASSWORD</label>
                <a v-if="isLogin" class="font-body-sm text-xs text-secondary hover:text-accent-hover transition-colors" href="#">Forgot password?</a>
              </div>
              <div class="relative">
                <input class="w-full h-[44px] px-md rounded-lg border border-border-soft bg-white text-body-main placeholder:text-outline/50 form-input-focus transition-all outline-none focus:border-secondary-container focus:ring-1 focus:ring-secondary-container" id="password" placeholder="••••••••" type="password" />
              </div>
            </div>
            
            <div class="flex items-center gap-xs">
              <input class="w-4 h-4 rounded border-border-soft text-secondary focus:ring-secondary custom-checkbox transition-all" id="remember" type="checkbox" />
              <label class="font-body-sm text-sm text-on-surface-variant cursor-pointer" for="remember">
                {{ isLogin ? 'Remember me for 30 days' : 'I agree to the Terms of Service' }}
              </label>
            </div>
            
            <button class="w-full h-[48px] bg-secondary-container text-white font-button-text text-button-text rounded-full hover:bg-accent-hover active:scale-[0.98] transition-all shadow-md" type="submit">
              {{ isLogin ? 'Sign In' : 'Create Account' }}
            </button>
          </form>
          
          <!-- Divider -->
          <div class="relative flex items-center py-sm">
            <div class="flex-grow border-t border-border-soft"></div>
            <span class="flex-shrink mx-md font-label-caps text-xs text-outline bg-surface-container-lowest px-xs">OR CONTINUE WITH</span>
            <div class="flex-grow border-t border-border-soft"></div>
          </div>
          
          <!-- Social Logins -->
          <div class="grid grid-cols-2 gap-md">
            <button class="flex items-center justify-center gap-xs h-[44px] rounded-full border border-border-soft bg-white hover:bg-surface-container-low transition-colors group">
              <svg class="w-5 h-5" viewbox="0 0 24 24">
                <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"></path>
                <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"></path>
                <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z" fill="#FBBC05"></path>
                <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"></path>
              </svg>
              <span class="font-button-text text-sm text-on-surface">Google</span>
            </button>
            <button class="flex items-center justify-center gap-xs h-[44px] rounded-full border border-border-soft bg-white hover:bg-surface-container-low transition-colors group">
              <svg class="w-5 h-5" viewbox="0 0 23 23">
                <path d="M0 0h23v23H0z" fill="#f3f3f3"></path><path d="M1 1h10v10H1z" fill="#f35325"></path><path d="M12 1h10v10H12z" fill="#81bc06"></path><path d="M1 12h10v10H1z" fill="#05a6f0"></path><path d="M12 12h10v10H12z" fill="#ffba08"></path>
              </svg>
              <span class="font-button-text text-sm text-on-surface">Microsoft</span>
            </button>
          </div>
          
          <!-- Footer Links -->
          <div class="pt-xl text-center">
            <p class="font-body-sm text-xs text-outline">
              By continuing, you agree to Sahayta's <a class="underline hover:text-primary" href="#">Terms of Service</a> and <a class="underline hover:text-primary" href="#">Privacy Policy</a>.
            </p>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';
const isLogin = ref(false); // Default to register for the signup page
</script>

<style scoped>
</style>
