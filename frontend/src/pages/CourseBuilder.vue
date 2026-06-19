<template>
  <div>
    
<!-- TopAppBar -->
<header class="bg-surface dark:bg-inverse-surface border-b border-border-soft dark:border-outline-variant flex justify-between items-center w-full px-lg py-md h-20 fixed top-0 z-[60] docked full-width shadow-sm">
<div class="flex items-center gap-md">
<button class="hover:bg-surface-container transition-colors active:scale-95 duration-150 p-2 rounded-full flex items-center justify-center">
<span class="material-symbols-outlined text-primary dark:text-primary-fixed-dim">arrow_back</span>
</button>
<div class="flex flex-col">
<input class="bg-transparent border-none focus:ring-0 font-headline-md text-headline-md md:font-headline-lg md:text-headline-lg p-0 text-text-primary dark:text-primary-fixed-dim placeholder:text-outline-variant" type="text" value="Advanced Data Science 101"/>
</div>
</div>
<div class="flex items-center gap-sm">
<button class="hidden md:flex font-button-text text-button-text text-primary dark:text-primary-fixed-dim border border-primary/20 px-lg py-2 rounded-full hover:bg-surface-container transition-all active:scale-95">
                Preview
            </button>
<button class="bg-secondary-container text-on-secondary-container font-button-text text-button-text px-lg py-2 rounded-full hover:bg-accent-hover transition-all active:scale-95 shadow-md">
                Publish Course
            </button>
</div>
</header>
<!-- Main 3-Panel Layout -->
<main class="pt-20 pb-20 md:pb-0 h-screen flex flex-col md:flex-row overflow-hidden">
<!-- Left Panel: Module Tree -->
<aside class="mobile-panel hidden md:flex flex-col w-full md:w-[280px] bg-primary-container text-on-primary-container border-r border-border-soft/10 h-full overflow-y-auto custom-scrollbar shrink-0" id="panel-modules">
<div class="p-lg">
<div class="flex items-center justify-between mb-lg">
<h2 class="font-label-caps text-label-caps opacity-60 uppercase tracking-widest">Course Structure</h2>
<span class="material-symbols-outlined text-sm opacity-60">account_tree</span>
</div>
<div class="space-y-md">
<!-- Module Item -->
<div class="group">
<div class="flex items-center gap-sm p-sm rounded-lg hover:bg-white/5 transition-colors cursor-pointer border border-transparent hover:border-white/10">
<span class="material-symbols-outlined text-outline opacity-40 cursor-grab">drag_indicator</span>
<span class="flex-1 font-body-sm text-body-sm font-medium">1. Introduction</span>
<span class="material-symbols-outlined text-xs opacity-0 group-hover:opacity-100 transition-opacity">more_vert</span>
</div>
<!-- Lessons -->
<div class="ml-xl mt-xs space-y-base">
<div class="flex items-center gap-sm p-sm rounded-lg bg-secondary/10 border border-secondary/20 text-secondary-fixed transition-colors cursor-pointer">
<span class="material-symbols-outlined text-sm">description</span>
<span class="flex-1 font-body-sm text-body-sm truncate">Neural Networks Intro</span>
</div>
<div class="flex items-center gap-sm p-sm rounded-lg hover:bg-white/5 transition-colors cursor-pointer text-on-primary-container/70">
<span class="material-symbols-outlined text-sm">play_circle</span>
<span class="flex-1 font-body-sm text-body-sm truncate">Setup &amp; History</span>
</div>
</div>
</div>
<!-- Module Item -->
<div class="group">
<div class="flex items-center gap-sm p-sm rounded-lg hover:bg-white/5 transition-colors cursor-pointer border border-transparent hover:border-white/10">
<span class="material-symbols-outlined text-outline opacity-40 cursor-grab">drag_indicator</span>
<span class="flex-1 font-body-sm text-body-sm font-medium">2. Deep Learning Base</span>
<span class="material-symbols-outlined text-xs opacity-0 group-hover:opacity-100 transition-opacity">more_vert</span>
</div>
</div>
<button class="w-full mt-lg flex items-center justify-center gap-sm border border-dashed border-white/20 p-md rounded-xl hover:bg-white/5 hover:border-secondary transition-all group">
<span class="material-symbols-outlined text-on-primary-container/50 group-hover:text-secondary">add_circle</span>
<span class="font-button-text text-button-text text-on-primary-container/60 group-hover:text-secondary">Add Section</span>
</button>
</div>
</div>
</aside>
<!-- Main Canvas (Center): Content Editor -->
<section class="mobile-panel flex-1 bg-surface-muted md:bg-surface overflow-y-auto custom-scrollbar flex flex-col active-tab-content" id="panel-canvas">
<div class="max-w-[800px] mx-auto w-full px-lg py-2xl">
<div class="bg-surface-lowest md:bg-transparent rounded-xl p-lg md:p-0 shadow-sm md:shadow-none">
<header class="mb-xl">
<input class="w-full font-display-hero text-headline-lg-mobile md:text-headline-lg bg-transparent border-none focus:ring-0 p-0 text-primary placeholder:text-outline-variant" type="text" value="Introduction to Neural Networks"/>
<div class="h-1 w-20 bg-secondary-container mt-sm rounded-full"></div>
</header>
<div class="canvas-editor font-body-main text-body-main text-on-surface-variant space-y-lg leading-relaxed min-h-[400px]" contenteditable="true">
<p>Neural networks are a series of algorithms that endeavor to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates.</p>
<p>In this context, neural networks refer to systems of neurons, either organic or artificial in nature. Neural networks can adapt to changing input; so the network generates the best possible result without needing to redesign the output criteria.</p>
<p class="italic text-outline opacity-50">Start typing here to expand your lesson content...</p>
</div>
<!-- Media Toolbar -->
<div class="mt-2xl border-t border-border-soft pt-lg">
<p class="font-label-caps text-label-caps text-outline mb-md uppercase tracking-wider">Embed Content</p>
<div class="flex flex-wrap gap-sm">
<button class="flex items-center gap-sm px-lg py-sm bg-surface-container hover:bg-secondary-container/20 border border-outline-variant/30 rounded-full transition-all group">
<span class="material-symbols-outlined text-primary group-hover:text-secondary">videocam</span>
<span class="font-button-text text-button-text text-on-surface">Video</span>
</button>
<button class="flex items-center gap-sm px-lg py-sm bg-surface-container hover:bg-secondary-container/20 border border-outline-variant/30 rounded-full transition-all group">
<span class="material-symbols-outlined text-primary group-hover:text-secondary">image</span>
<span class="font-button-text text-button-text text-on-surface">Image</span>
</button>
<button class="flex items-center gap-sm px-lg py-sm bg-surface-container hover:bg-secondary-container/20 border border-outline-variant/30 rounded-full transition-all group">
<span class="material-symbols-outlined text-primary group-hover:text-secondary">quiz</span>
<span class="font-button-text text-button-text text-on-surface">Quiz</span>
</button>
<button class="flex items-center gap-sm px-lg py-sm bg-surface-container hover:bg-secondary-container/20 border border-outline-variant/30 rounded-full transition-all group">
<span class="material-symbols-outlined text-primary group-hover:text-secondary">upload_file</span>
<span class="font-button-text text-button-text text-on-surface">File Upload</span>
</button>
</div>
</div>
</div>
</div>
</section>
<!-- Right Panel: Lesson Settings -->
<aside class="mobile-panel hidden md:flex flex-col w-full md:w-[320px] bg-surface border-l border-border-soft h-full overflow-y-auto custom-scrollbar shrink-0" id="panel-settings">
<div class="p-lg">
<div class="flex items-center justify-between mb-xl">
<h2 class="font-label-caps text-label-caps text-outline uppercase tracking-widest">Lesson Settings</h2>
<span class="material-symbols-outlined text-on-surface-variant">settings</span>
</div>
<form class="space-y-xl">
<div class="space-y-xs">
<label class="font-label-caps text-label-caps text-on-surface opacity-80">Lesson Title</label>
<input class="w-full bg-white border border-border-soft rounded-lg px-md py-sm focus:ring-2 focus:ring-secondary-container focus:border-secondary transition-all outline-none" type="text" value="Introduction to Neural Networks"/>
</div>
<div class="grid grid-cols-2 gap-md">
<div class="space-y-xs">
<label class="font-label-caps text-label-caps text-on-surface opacity-80">Duration (Min)</label>
<input class="w-full bg-white border border-border-soft rounded-lg px-md py-sm focus:ring-2 focus:ring-secondary-container focus:border-secondary outline-none" type="number" value="45"/>
</div>
<div class="space-y-xs">
<label class="font-label-caps text-label-caps text-on-surface opacity-80">Order</label>
<input class="w-full bg-white border border-border-soft rounded-lg px-md py-sm focus:ring-2 focus:ring-secondary-container focus:border-secondary outline-none" type="number" value="1"/>
</div>
</div>
<div class="space-y-xs">
<label class="font-label-caps text-label-caps text-on-surface opacity-80">Prerequisites</label>
<select class="w-full bg-white border border-border-soft rounded-lg px-md py-sm focus:ring-2 focus:ring-secondary-container focus:border-secondary outline-none">
<option>None</option>
<option>Basic Python 101</option>
<option>Math for DS</option>
</select>
</div>
<div class="flex items-center justify-between p-md bg-surface-container-low rounded-xl border border-border-soft">
<div class="flex flex-col">
<span class="font-button-text text-button-text text-on-surface">Visibility</span>
<span class="text-xs text-outline">Visible to all students</span>
</div>
<label class="relative inline-flex items-center cursor-pointer">
<input checked="" class="sr-only peer" type="checkbox"/>
<div class="w-11 h-6 bg-outline-variant peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-secondary"></div>
</label>
</div>
<div class="pt-xl border-t border-border-soft">
<button class="w-full text-danger flex items-center justify-center gap-sm py-sm hover:bg-error-container/20 rounded-lg transition-colors" type="button">
<span class="material-symbols-outlined">delete</span>
<span class="font-button-text text-button-text">Delete Lesson</span>
</button>
</div>
</form>
</div>
</aside>
</main>
<!-- BottomNavBar (Mobile Only) -->
<nav class="fixed bottom-0 left-0 w-full flex justify-around items-center px-4 py-2 bg-surface dark:bg-inverse-surface border-t border-border-soft md:hidden z-[60] h-16 shadow-lg">
<button class="flex flex-col items-center justify-center text-outline dark:text-outline-variant hover:text-secondary transition-transform active:scale-90 px-4 py-1" onclick="switchTab('modules', this)">
<span class="material-symbols-outlined" data-icon="account_tree">account_tree</span>
<span class="font-label-caps text-label-caps">Modules</span>
</button>
<button class="flex flex-col items-center justify-center text-secondary dark:text-secondary-fixed-dim bg-secondary-container/10 rounded-xl px-4 py-1 transition-transform active:scale-90" onclick="switchTab('canvas', this)">
<span class="material-symbols-outlined" data-icon="edit_note">edit_note</span>
<span class="font-label-caps text-label-caps">Canvas</span>
</button>
<button class="flex flex-col items-center justify-center text-outline dark:text-outline-variant hover:text-secondary transition-transform active:scale-90 px-4 py-1" onclick="switchTab('settings', this)">
<span class="material-symbols-outlined" data-icon="settings">settings</span>
<span class="font-label-caps text-label-caps">Settings</span>
</button>
</nav>


  </div>
</template>

<script setup>
</script>

<style scoped>
/* Copy any specific styles if needed, or rely on global Tailwind classes */
</style>
