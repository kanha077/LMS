<template>
  <button
    :class="[
      'inline-flex items-center justify-center font-medium transition-all duration-150',
      'border border-solid shadow-solid active:scale-[0.98]',
      'disabled:opacity-50 disabled:pointer-events-none',
      sizeClasses[size],
      variantClasses[variant]
    ]"
    :disabled="disabled || loading"
    @click="$emit('click', $event)"
  >
    <svg v-if="loading" class="animate-spin -ml-1 mr-2 h-4 w-4 text-current" fill="none" viewBox="0 0 24 24">
      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
    </svg>
    <slot></slot>
  </button>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  variant: {
    type: String,
    default: 'primary',
    validator: (value) => ['primary', 'secondary', 'outline', 'danger'].includes(value)
  },
  size: {
    type: String,
    default: 'md',
    validator: (value) => ['sm', 'md', 'lg'].includes(value)
  },
  disabled: {
    type: Boolean,
    default: false
  },
  loading: {
    type: Boolean,
    default: false
  }
})

defineEmits(['click'])

const sizeClasses = {
  sm: 'px-3 py-1.5 text-[13px] rounded-md',
  md: 'px-4 py-2 text-[15px] rounded-md',
  lg: 'px-6 py-3 text-[18px] rounded-lg'
}

const variantClasses = {
  primary: 'bg-brand-accent text-surface-light border-brand-accent hover:bg-brand-accentHover',
  secondary: 'bg-surface-offwhite text-ink-dark border-ink-lightest hover:bg-ink-lightest dark:bg-surface-dark dark:text-ink-lightest dark:border-ink-mid dark:hover:bg-ink-mid',
  outline: 'bg-transparent text-brand-accent border-brand-accent hover:bg-brand-accent hover:text-surface-light',
  danger: 'bg-alert-error text-surface-light border-alert-error hover:bg-red-700'
}
</script>
