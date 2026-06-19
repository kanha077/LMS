<template>
  <div class="flex h-screen bg-surface-offwhite dark:bg-surface-bgDark font-sans transition-colors duration-200">
    <Sidebar />
    <div class="flex-1 flex flex-col overflow-hidden">
      <Navbar />
      <main class="flex-1 overflow-y-auto p-6 lg:p-8">
        <div class="mb-8 flex items-center justify-between gap-4">
          <div class="flex items-center gap-4">
            <button @click="$router.back()" class="text-ink-mid hover:text-ink-dark dark:text-ink-mutedDark dark:hover:text-surface-light bg-surface-light dark:bg-surface-dark px-3 py-1.5 rounded-md border border-ink-lightest dark:border-ink-mid shadow-sm transition-colors text-[13px] font-medium">
              &larr; Back
            </button>
            <h1 class="text-[24px] font-semibold text-ink-dark dark:text-surface-light">Quiz Builder</h1>
          </div>
          <BaseButton variant="primary">Save Quiz</BaseButton>
        </div>
        
        <div class="grid grid-cols-1 xl:grid-cols-4 gap-8">
          <!-- Quiz Settings -->
          <div class="xl:col-span-1 space-y-6">
            <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid p-6 space-y-4">
              <h2 class="text-[16px] font-medium text-ink-dark dark:text-surface-light mb-2">Quiz Settings</h2>
              <BaseInput v-model="quiz.title" label="Quiz Title *" placeholder="e.g. Midterm Exam" />
              <div class="flex flex-col gap-1 w-full">
                <label class="text-[13px] font-medium text-ink-mid dark:text-ink-mutedDark">Time Limit (minutes)</label>
                <input v-model="quiz.timeLimit" type="number" class="w-full px-3 py-2 text-[15px] rounded-md border transition-all duration-150 outline-none bg-surface-light text-ink-dark dark:bg-surface-dark dark:text-ink-lightest border-ink-lightest dark:border-ink-mid focus:border-brand-accent focus:ring-2 focus:ring-brand-accent/20" />
              </div>
              <div class="flex flex-col gap-1 w-full">
                <label class="text-[13px] font-medium text-ink-mid dark:text-ink-mutedDark">Passing Score (%)</label>
                <input v-model="quiz.passingScore" type="number" class="w-full px-3 py-2 text-[15px] rounded-md border transition-all duration-150 outline-none bg-surface-light text-ink-dark dark:bg-surface-dark dark:text-ink-lightest border-ink-lightest dark:border-ink-mid focus:border-brand-accent focus:ring-2 focus:ring-brand-accent/20" />
              </div>
              <label class="flex items-center gap-2 cursor-pointer mt-4">
                <input type="checkbox" v-model="quiz.randomize" class="rounded text-brand-accent focus:ring-brand-accent/20" />
                <span class="text-[13px] text-ink-dark dark:text-surface-light">Randomize Questions</span>
              </label>
            </div>
          </div>

          <!-- Questions Builder -->
          <div class="xl:col-span-3">
            <div class="space-y-6">
              <div v-for="(q, qIndex) in questions" :key="q.id" class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid p-6">
                <div class="flex justify-between items-start mb-4">
                  <span class="bg-brand-accent/10 text-brand-accent px-2 py-1 rounded text-[11px] font-bold uppercase tracking-widest">Question {{qIndex + 1}}</span>
                  <button @click="removeQuestion(qIndex)" class="text-ink-light hover:text-alert-error"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg></button>
                </div>
                
                <div class="space-y-4">
                  <div class="flex flex-col gap-1 w-full">
                    <input v-model="q.text" type="text" placeholder="Enter your question here..." class="w-full px-3 py-2 text-[15px] font-medium rounded-md border transition-all duration-150 outline-none bg-surface-offwhite text-ink-dark dark:bg-ink-dark dark:text-surface-light border-ink-lightest dark:border-ink-mid focus:border-brand-accent focus:ring-2 focus:ring-brand-accent/20" />
                  </div>
                  
                  <div class="pl-4 space-y-3 mt-4 border-l-2 border-ink-lightest dark:border-ink-mid">
                    <div v-for="(opt, oIndex) in q.options" :key="oIndex" class="flex items-center gap-3">
                      <input type="radio" :name="'correct_' + q.id" :checked="q.correctIndex === oIndex" @change="q.correctIndex = oIndex" class="text-alert-success focus:ring-alert-success/20 cursor-pointer" title="Mark as correct answer" />
                      <input v-model="q.options[oIndex]" type="text" placeholder="Option text" class="w-full px-3 py-1.5 text-[14px] rounded-md border transition-all duration-150 outline-none bg-surface-light text-ink-dark dark:bg-surface-dark dark:text-surface-light border-ink-lightest dark:border-ink-mid focus:border-brand-accent" />
                      <button @click="removeOption(qIndex, oIndex)" class="text-ink-light hover:text-alert-error"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg></button>
                    </div>
                    <button @click="addOption(qIndex)" class="text-[12px] font-medium text-brand-accent hover:text-brand-accentHover flex items-center gap-1 mt-2">
                      <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg> Add Option
                    </button>
                  </div>
                </div>
              </div>
              
              <div class="flex justify-center border-2 border-dashed border-ink-lightest dark:border-ink-mid rounded-xl p-8 hover:bg-surface-offwhite dark:hover:bg-ink-dark transition-colors cursor-pointer" @click="addQuestion">
                <div class="text-center">
                  <svg class="w-8 h-8 text-ink-light mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                  <span class="text-[14px] font-medium text-ink-dark dark:text-surface-light">Add New Question</span>
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
import { ref } from 'vue';
import Navbar from '../../components/Navbar.vue';
import Sidebar from '../../components/Sidebar.vue';
import BaseInput from '../../components/ui/BaseInput.vue';
import BaseButton from '../../components/ui/BaseButton.vue';

const quiz = ref({
  title: '',
  timeLimit: 60,
  passingScore: 70,
  randomize: false
});

const questions = ref([
  {
    id: 1,
    text: 'What is the primary function of the mitochondria?',
    options: ['Powerhouse of the cell', 'DNA storage', 'Protein synthesis', 'Waste removal'],
    correctIndex: 0
  }
]);

const addQuestion = () => {
  questions.value.push({
    id: Date.now(),
    text: '',
    options: ['Option 1', 'Option 2'],
    correctIndex: 0
  });
};

const removeQuestion = (index) => {
  questions.value.splice(index, 1);
};

const addOption = (qIndex) => {
  questions.value[qIndex].options.push('');
};

const removeOption = (qIndex, oIndex) => {
  questions.value[qIndex].options.splice(oIndex, 1);
  if(questions.value[qIndex].correctIndex === oIndex) {
    questions.value[qIndex].correctIndex = 0;
  }
};
</script>
