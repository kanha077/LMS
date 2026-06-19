<template>
  <div class="flex flex-col gap-1 w-full">
    <label v-if="label" class="text-[13px] font-medium text-ink-mid dark:text-ink-mutedDark">
      {{ label }}
    </label>
    <input
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      :type="type"
      :placeholder="placeholder"
      :disabled="disabled"
      :class="[
        'w-full px-3 py-2 text-[15px] rounded-md border transition-all duration-150 outline-none',
        'bg-surface-light text-ink-dark dark:bg-surface-dark dark:text-ink-lightest',
        error 
          ? 'border-alert-error focus:ring-2 focus:ring-alert-error/20' 
          : 'border-ink-lightest dark:border-ink-mid focus:border-brand-accent focus:ring-2 focus:ring-brand-accent/20',
        disabled ? 'opacity-50 bg-surface-offwhite cursor-not-allowed' : ''
      ]"
    />
    <span v-if="error" class="text-[13px] text-alert-error">{{ error }}</span>
  </div>
</template>

<script setup>
defineProps({
  modelValue: {
    type: [String, Number],
    default: ''
  },
  label: {
    type: String,
    default: ''
  },
  type: {
    type: String,
    default: 'text'
  },
  placeholder: {
    type: String,
    default: ''
  },
  error: {
    type: String,
    default: ''
  },
  disabled: {
    type: Boolean,
    default: false
  }
})

defineEmits(['update:modelValue'])
</script>
