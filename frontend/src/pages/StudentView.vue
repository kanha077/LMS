<template>
  <div>
    
<!-- Top AppBar (Mobile Focused) -->
<header class="sticky top-0 z-40 bg-surface dark:bg-inverse-surface border-b border-border-soft dark:border-outline-variant flex justify-between items-center w-full px-md py-md h-20 shadow-sm">
<div class="flex items-center gap-2">
<button class="p-2 rounded-full hover:bg-surface-container transition-colors active:scale-95 duration-150">
<span class="material-symbols-outlined text-primary dark:text-primary-fixed-dim">arrow_back</span>
</button>
<div class="flex flex-col">
<span class="font-headline-md text-[14px] leading-tight text-outline truncate max-w-[150px]">Course Player</span>
<h1 class="font-headline-md text-[16px] font-bold text-primary dark:text-primary-fixed-dim truncate max-w-[180px]">Advanced Data Science 101</h1>
</div>
</div>
<button class="bg-secondary-container text-on-secondary-container px-4 py-2 rounded-full font-button-text text-button-text hover:bg-accent-hover transition-colors active:scale-95 duration-150 shadow-sm">
            Mark as Complete
        </button>
</header>
<!-- Main Content Area -->
<main class="w-full flex flex-col">
<!-- Video Player (16:9 Aspect Ratio) -->
<section class="w-full aspect-video bg-black relative overflow-hidden group">
<div class="absolute inset-0 flex items-center justify-center">
<!-- Video Thumbnail Placeholder -->
<div class="w-full h-full bg-cover bg-center opacity-80" data-alt="A cinematic, high-definition video frame showing a dark, futuristic lecture hall with glowing blue holographic neural network visualizations floating in the air. The lighting is dramatic, casting soft glows on high-tech surfaces. The overall aesthetic is professional, minimalist, and educational, with deep indigo and amber accents reflecting the Sahayta brand identity." style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuA5n_g8BS8Jt8SVCIqC9cFHV9J7eQkPFGIiWS0kXxb8OH6cjwI36pXK_Tw8wPgfbi4g7wzkLnX_-Ld61QtHuJY5_ZMwmE5Vh9NGxx-PyS4_RCmoUpnB3tTTBsIjBWAlSE_BLy2HhgmQa0lM3BzazxbeoJ9ikB5DjlzKdQu2Z8PYLRLTvK_UXuMIBUtOKPXF4D7sUVD_fb-rEKFxzRkOuQkV2nHFT4dESwmqVle2EHiQMtKpbFOxbRROX-ZuKx0Oh_7gmw0gHqGB-t_s')"></div>
<!-- Play Button -->
<button class="z-10 bg-white/20 backdrop-blur-md p-6 rounded-full border border-white/30 group-hover:scale-110 transition-transform duration-300">
<span class="material-symbols-outlined text-white text-4xl" style="font-variation-settings: 'FILL' 1;">play_arrow</span>
</button>
</div>
<!-- Video Controls Overlay (Simulated) -->
<div class="absolute bottom-0 left-0 w-full p-4 video-overlay-gradient flex flex-col gap-2">
<!-- Progress Bar -->
<div class="w-full h-1 bg-white/20 rounded-full cursor-pointer relative">
<div class="absolute top-0 left-0 h-full w-1/3 bg-secondary-container rounded-full"></div>
</div>
<div class="flex justify-between items-center text-white text-xs font-label-caps">
<div class="flex gap-4">
<span class="material-symbols-outlined text-sm">pause</span>
<span class="material-symbols-outlined text-sm">volume_up</span>
<span>04:12 / 12:45</span>
</div>
<div class="flex gap-4">
<span class="material-symbols-outlined text-sm">settings</span>
<span class="material-symbols-outlined text-sm">fullscreen</span>
</div>
</div>
</div>
</section>
<!-- Lesson Info -->
<section class="px-md py-lg">
<h2 class="text-[24px] font-bold text-primary-container mb-2 leading-tight">Introduction to Neural Networks</h2>
<div class="flex items-center gap-3 mb-6">
<span class="flex items-center gap-1 text-outline text-xs font-label-caps">
<span class="material-symbols-outlined text-[14px]">schedule</span>
                    12m 45s
                </span>
<span class="w-1 h-1 rounded-full bg-outline-variant"></span>
<span class="flex items-center gap-1 text-outline text-xs font-label-caps">
<span class="material-symbols-outlined text-[14px]">description</span>
                    Module 2
                </span>
</div>
<div class="prose prose-sm font-body-main text-on-surface-variant leading-relaxed mb-10">
<p>Neural networks are the backbone of modern artificial intelligence. In this lesson, we explore the fundamental structure of an artificial neuron, the concept of weights and biases, and how multiple layers combine to form a deep learning model. We'll also cover the activation functions that enable non-linearity in learning.</p>
</div>
<!-- Content Navigation -->
<div class="flex justify-between items-center gap-4 border-t border-border-soft pt-lg">
<button class="flex-1 border border-primary text-primary px-4 py-3 rounded-full font-button-text text-button-text flex items-center justify-center gap-2 hover:bg-surface-container transition-colors active:scale-95 duration-150">
<span class="material-symbols-outlined text-[18px]">arrow_back</span>
                    Previous
                </button>
<button class="flex-1 border border-primary text-primary px-4 py-3 rounded-full font-button-text text-button-text flex items-center justify-center gap-2 hover:bg-surface-container transition-colors active:scale-95 duration-150">
                    Next
                    <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
</button>
</div>
</section>
<!-- Related Resources / Notes Bento (Extra value) -->
<section class="px-md pb-xl">
<div class="grid grid-cols-2 gap-3">
<div class="bg-surface-container-low p-4 rounded-xl border border-border-soft flex flex-col gap-2">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">description</span>
<h3 class="font-title-card text-[15px] text-primary">Lecture Notes</h3>
<p class="text-[12px] text-on-surface-variant">PDF, 2.4 MB</p>
</div>
<div class="bg-surface-container-low p-4 rounded-xl border border-border-soft flex flex-col gap-2">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">code</span>
<h3 class="font-title-card text-[15px] text-primary">Exercise Files</h3>
<p class="text-[12px] text-on-surface-variant">ZIP, 15 MB</p>
</div>
</div>
</section>
</main>
<!-- Bottom Sidebar / Module List Drawer -->
<div class="fixed inset-0 bg-primary/20 backdrop-blur-sm z-40 hidden opacity-0 transition-opacity duration-300" id="module-drawer-overlay"></div>
<aside class="fixed bottom-0 left-0 w-full bg-surface z-50 rounded-t-3xl shadow-2xl border-t border-border-soft hidden-drawer flex flex-col max-h-[707px]" id="module-drawer">
<!-- Drawer Handle -->
<div class="w-full py-4 flex justify-center cursor-pointer" id="drawer-handle">
<div class="w-12 h-1.5 bg-outline-variant rounded-full"></div>
</div>
<div class="px-lg pb-md flex justify-between items-center border-b border-border-soft">
<h2 class="text-xl font-bold text-primary">Course Modules</h2>
<span class="text-xs font-label-caps text-secondary-fixed-dim bg-primary px-3 py-1 rounded-full">24% Complete</span>
</div>
<!-- Module List Scrollable Content -->
<div class="overflow-y-auto px-lg py-md space-y-6 flex-1">
<!-- Module 1 -->
<div>
<h3 class="font-label-caps text-outline mb-3 uppercase tracking-wider">Module 1: Data Foundations</h3>
<div class="space-y-1">
<div class="flex items-center justify-between p-3 rounded-lg hover:bg-surface-container-low transition-colors">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">check_circle</span>
<span class="text-sm font-medium text-on-surface-variant">What is Data Science?</span>
</div>
<span class="text-[10px] text-outline">05:20</span>
</div>
<div class="flex items-center justify-between p-3 rounded-lg hover:bg-surface-container-low transition-colors">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">check_circle</span>
<span class="text-sm font-medium text-on-surface-variant">Probability &amp; Statistics</span>
</div>
<span class="text-[10px] text-outline">15:45</span>
</div>
</div>
</div>
<!-- Module 2 -->
<div>
<h3 class="font-label-caps text-outline mb-3 uppercase tracking-wider">Module 2: Neural Architecture</h3>
<div class="space-y-1">
<!-- Current Lesson -->
<div class="flex items-center justify-between p-3 rounded-xl bg-primary-container/10 border border-primary/10">
<div class="flex items-center gap-3">
<div class="w-6 h-6 flex items-center justify-center rounded-full border-2 border-primary/20">
<div class="w-2.5 h-2.5 bg-primary rounded-full"></div>
</div>
<span class="text-sm font-bold text-primary">Introduction to Neural Networks</span>
</div>
<span class="text-[10px] font-bold text-primary">PLAYING</span>
</div>
<div class="flex items-center justify-between p-3 rounded-lg hover:bg-surface-container-low transition-colors opacity-60">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-outline">circle</span>
<span class="text-sm font-medium text-on-surface-variant">Backpropagation Explained</span>
</div>
<span class="text-[10px] text-outline">22:10</span>
</div>
<div class="flex items-center justify-between p-3 rounded-lg hover:bg-surface-container-low transition-colors opacity-60">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-outline">circle</span>
<span class="text-sm font-medium text-on-surface-variant">Loss Functions &amp; Optimization</span>
</div>
<span class="text-[10px] text-outline">18:30</span>
</div>
</div>
</div>
<!-- Module 3 -->
<div>
<h3 class="font-label-caps text-outline mb-3 uppercase tracking-wider">Module 3: Advanced Architectures</h3>
<div class="space-y-1">
<div class="flex items-center justify-between p-3 rounded-lg hover:bg-surface-container-low transition-colors opacity-60">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-outline">lock</span>
<span class="text-sm font-medium text-on-surface-variant">Convolutional Neural Networks (CNNs)</span>
</div>
<span class="text-[10px] text-outline">25:15</span>
</div>
</div>
</div>
</div>
</aside>
<!-- Bottom NavBar -->
<nav class="fixed bottom-0 left-0 w-full flex justify-around items-center px-4 py-2 bg-surface dark:bg-inverse-surface border-t border-border-soft z-50 md:hidden h-16">
<!-- Dashboard/Canvas - Active context is the Player (Canvas) -->
<a class="flex flex-col items-center justify-center text-outline dark:text-outline-variant hover:text-secondary transition-colors" href="#">
<span class="material-symbols-outlined">dashboard</span>
<span class="text-[10px] font-bold uppercase tracking-tighter">Dashboard</span>
</a>
<button class="flex flex-col items-center justify-center text-outline dark:text-outline-variant hover:text-secondary transition-colors relative" id="toggle-modules">
<span class="material-symbols-outlined">account_tree</span>
<span class="text-[10px] font-bold uppercase tracking-tighter">Modules</span>
<div class="absolute -top-1 -right-1 w-2 h-2 bg-secondary-container rounded-full"></div>
</button>
<a class="flex flex-col items-center justify-center text-secondary dark:text-secondary-fixed-dim bg-secondary-container/10 rounded-xl px-4 py-1 active:scale-90 transition-transform" href="#">
<span class="material-symbols-outlined">edit_note</span>
<span class="text-[10px] font-bold uppercase tracking-tighter">Canvas</span>
</a>
<a class="flex flex-col items-center justify-center text-outline dark:text-outline-variant hover:text-secondary transition-colors" href="#">
<span class="material-symbols-outlined">settings</span>
<span class="text-[10px] font-bold uppercase tracking-tighter">Settings</span>
</a>
</nav>


  </div>
</template>

<script setup>
</script>

<style scoped>
/* Copy any specific styles if needed, or rely on global Tailwind classes */
</style>
