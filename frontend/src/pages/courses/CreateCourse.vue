<template>
  <div class="flex h-screen bg-surface-offwhite dark:bg-surface-bgDark font-sans transition-colors duration-200">
    <Sidebar />
    <div class="flex-1 flex flex-col overflow-hidden">
      <Navbar />
      <main class="flex-1 overflow-y-auto p-6 lg:p-8">
        <div class="mb-8 flex items-center justify-between gap-4">
          <div class="flex items-center gap-4">
            <router-link to="/courses" class="text-ink-mid hover:text-ink-dark dark:text-ink-mutedDark dark:hover:text-surface-light bg-surface-light dark:bg-surface-dark px-3 py-1.5 rounded-md border border-ink-lightest dark:border-ink-mid shadow-sm transition-colors text-[13px] font-medium">
              &larr; Back
            </router-link>
            <h1 class="text-[24px] font-semibold text-ink-dark dark:text-surface-light">Course Builder</h1>
          </div>
          <BaseButton variant="primary" @click="handleCreate" :disabled="loading">
            {{ loading ? 'Saving...' : 'Publish Course' }}
          </BaseButton>
        </div>
        
        <div class="grid grid-cols-1 xl:grid-cols-3 gap-8">
          <!-- Course Settings -->
          <div class="xl:col-span-1 space-y-6">
            <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid p-6">
              <h2 class="text-[16px] font-medium text-ink-dark dark:text-surface-light mb-4">General Details</h2>
              <div class="space-y-4">
                <BaseInput v-model="form.name" label="Course Name *" placeholder="e.g. Advanced Vue 3" required />
                <BaseInput v-model="form.code" label="Course Code *" placeholder="e.g. VUE400" required />
                <BaseInput v-model="form.semester" label="Semester" placeholder="e.g. Fall 2026" />
                <div class="flex flex-col gap-1 w-full">
                  <label class="text-[13px] font-medium text-ink-mid dark:text-ink-mutedDark">Brief Description</label>
                  <textarea v-model="form.description" rows="4" class="w-full px-3 py-2 text-[15px] rounded-md border transition-all duration-150 outline-none bg-surface-light text-ink-dark dark:bg-surface-dark dark:text-ink-lightest border-ink-lightest dark:border-ink-mid focus:border-brand-accent focus:ring-2 focus:ring-brand-accent/20"></textarea>
                </div>
              </div>
            </div>
            
            <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid p-6">
              <h2 class="text-[16px] font-medium text-ink-dark dark:text-surface-light mb-4">Course Thumbnail</h2>
              <div class="border-2 border-dashed border-ink-lightest dark:border-ink-mid rounded-lg p-8 flex flex-col items-center justify-center text-center cursor-pointer hover:bg-surface-offwhite dark:hover:bg-ink-dark transition-colors">
                <svg class="w-8 h-8 text-ink-light mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                <span class="text-[13px] text-ink-mid dark:text-ink-mutedDark font-medium">Click to upload thumbnail</span>
                <span class="text-[11px] text-ink-light mt-1">PNG, JPG up to 5MB</span>
              </div>
            </div>
          </div>

          <!-- Curriculum Builder -->
          <div class="xl:col-span-2">
            <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid overflow-hidden">
              <div class="px-6 py-4 border-b border-ink-lightest dark:border-ink-mid flex justify-between items-center bg-surface-offwhite dark:bg-surface-dark">
                <div>
                  <h2 class="text-[16px] font-medium text-ink-dark dark:text-surface-light">Curriculum Planner</h2>
                  <p class="text-[13px] text-ink-light dark:text-ink-mutedDark mt-0.5">Drag and drop lessons to organize your course structure.</p>
                </div>
                <BaseButton variant="outline" size="sm" @click="addModule">Add Module</BaseButton>
              </div>
              
              <div class="p-6 space-y-6 bg-surface-offwhite dark:bg-surface-bgDark">
                <!-- Modules Loop -->
                <div v-for="(mod, index) in curriculum" :key="mod.id" class="bg-surface-light dark:bg-surface-dark border border-ink-lightest dark:border-ink-mid rounded-lg shadow-sm">
                  <div class="px-4 py-3 border-b border-ink-lightest dark:border-ink-mid flex items-center gap-3 cursor-move bg-surface-offwhite/50 dark:bg-ink-dark/50">
                    <svg class="w-4 h-4 text-ink-light" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8h16M4 16h16"></path></svg>
                    <input v-model="mod.title" type="text" class="bg-transparent border-none focus:ring-0 text-[15px] font-semibold text-ink-dark dark:text-surface-light p-0 outline-none w-full" placeholder="Module Title" />
                    <button @click="removeModule(index)" class="text-ink-light hover:text-alert-error"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg></button>
                  </div>
                  
                  <div class="p-4 space-y-3">
                    <!-- Lessons Loop -->
                    <div v-for="(lesson, lIndex) in mod.lessons" :key="lesson.id" class="flex items-center gap-3 bg-surface-offwhite dark:bg-ink-dark border border-ink-lightest dark:border-ink-mid rounded-md p-3 group">
                      <svg class="w-4 h-4 text-ink-light cursor-move" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8h16M4 16h16"></path></svg>
                      <span class="bg-brand-accent/10 text-brand-accent px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wide">Lesson</span>
                      <input v-model="lesson.title" type="text" class="bg-transparent border-none focus:ring-0 text-[14px] text-ink-dark dark:text-surface-light p-0 outline-none flex-1" placeholder="Lesson Title" />
                      <div class="opacity-0 group-hover:opacity-100 transition-opacity flex gap-2">
                        <button class="text-ink-light hover:text-brand-accent" title="Edit Rich Text Content"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg></button>
                        <button @click="removeLesson(index, lIndex)" class="text-ink-light hover:text-alert-error"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg></button>
                      </div>
                    </div>
                    
                    <button @click="addLesson(index)" class="text-[13px] font-medium text-brand-accent hover:text-brand-accentHover flex items-center gap-1 mt-2">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                      Add Lesson
                    </button>
                  </div>
                </div>
                
                <div v-if="curriculum.length === 0" class="text-center py-10 border-2 border-dashed border-ink-lightest dark:border-ink-mid rounded-xl">
                  <p class="text-ink-mid dark:text-ink-mutedDark text-[14px]">No modules added yet. Start building your curriculum.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router';
import Navbar from '../../components/Navbar.vue';
import Sidebar from '../../components/Sidebar.vue';
import BaseInput from '../../components/ui/BaseInput.vue';
import BaseButton from '../../components/ui/BaseButton.vue';
import apiClient from '../../api';

const router = useRouter();
const loading = ref(false);

const form = reactive({
  name: '',
  code: '',
  description: '',
  semester: ''
});

// Mock curriculum state
const curriculum = ref([
  {
    id: 1,
    title: 'Module 1: Introduction',
    lessons: [
      { id: 101, title: 'Welcome to the Course' },
      { id: 102, title: 'Syllabus Overview' }
    ]
  }
]);

const addModule = () => {
  curriculum.value.push({
    id: Date.now(),
    title: `Module ${curriculum.value.length + 1}: `,
    lessons: []
  });
};

const removeModule = (index) => {
  if (confirm('Are you sure you want to remove this module and all its lessons?')) {
    curriculum.value.splice(index, 1);
  }
};

const addLesson = (moduleIndex) => {
  curriculum.value[moduleIndex].lessons.push({
    id: Date.now(),
    title: ''
  });
};

const removeLesson = (moduleIndex, lessonIndex) => {
  curriculum.value[moduleIndex].lessons.splice(lessonIndex, 1);
};

const handleCreate = async () => {
  loading.value = true;
  try {
    // In real app, we would save the course AND the curriculum here
    await apiClient.post('/courses', form);
    router.push('/courses');
  } catch (error) {
    alert(error.response?.data?.detail || 'Failed to create course');
  } finally {
    loading.value = false;
  }
};
</script>
