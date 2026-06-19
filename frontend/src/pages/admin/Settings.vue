<template>
  <div class="flex h-screen bg-surface-offwhite dark:bg-surface-bgDark font-sans transition-colors duration-200">
    <Sidebar />
    <div class="flex-1 flex flex-col overflow-hidden">
      <Navbar />
      <main class="flex-1 overflow-y-auto p-6 lg:p-8">
        <h1 class="text-[24px] font-semibold text-ink-dark dark:text-surface-light mb-8">System Settings</h1>
        
        <div class="grid grid-cols-1 xl:grid-cols-2 gap-8">
          <!-- Global Announcements -->
          <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid overflow-hidden">
            <div class="px-6 py-4 border-b border-ink-lightest dark:border-ink-mid">
              <h2 class="text-[18px] font-medium text-ink-dark dark:text-surface-light">Global Announcements</h2>
              <p class="text-[13px] text-ink-light dark:text-ink-mutedDark mt-1">Broadcast messages to all tenants and users on the platform.</p>
            </div>
            <div class="p-6 space-y-4">
              <BaseInput v-model="announcement.title" label="Announcement Title" placeholder="e.g. Scheduled Maintenance Notice" />
              <div class="flex flex-col gap-1 w-full">
                <label class="text-[13px] font-medium text-ink-mid dark:text-ink-mutedDark">Message Content</label>
                <textarea v-model="announcement.message" rows="4" class="w-full px-3 py-2 text-[15px] rounded-md border transition-all duration-150 outline-none bg-surface-light text-ink-dark dark:bg-surface-dark dark:text-ink-lightest border-ink-lightest dark:border-ink-mid focus:border-brand-accent focus:ring-2 focus:ring-brand-accent/20" placeholder="Write your message here..."></textarea>
              </div>
              <div class="flex flex-col gap-1 w-full">
                <label class="text-[13px] font-medium text-ink-mid dark:text-ink-mutedDark">Visibility</label>
                <select v-model="announcement.visibility" class="px-3 py-2 text-[15px] rounded-md border border-ink-lightest dark:border-ink-mid bg-surface-light text-ink-dark dark:bg-surface-dark dark:text-ink-lightest focus:border-brand-accent focus:ring-2 focus:ring-brand-accent/20 outline-none transition-all duration-150">
                  <option value="all">All Users (Global)</option>
                  <option value="teachers">Teachers Only</option>
                  <option value="students">Students Only</option>
                  <option value="admins">Tenant Admins Only</option>
                </select>
              </div>
              <div class="pt-2 flex justify-end">
                <BaseButton variant="primary" @click="publishAnnouncement">Publish Announcement</BaseButton>
              </div>
            </div>
          </div>

          <!-- Email Template Configurator -->
          <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid overflow-hidden">
            <div class="px-6 py-4 border-b border-ink-lightest dark:border-ink-mid">
              <h2 class="text-[18px] font-medium text-ink-dark dark:text-surface-light">Email Template Configurator</h2>
              <p class="text-[13px] text-ink-light dark:text-ink-mutedDark mt-1">Customize system-generated automated emails.</p>
            </div>
            <div class="p-6 space-y-4">
              <div class="flex flex-col gap-1 w-full">
                <label class="text-[13px] font-medium text-ink-mid dark:text-ink-mutedDark">Select Template</label>
                <select v-model="emailTemplate.type" class="px-3 py-2 text-[15px] rounded-md border border-ink-lightest dark:border-ink-mid bg-surface-light text-ink-dark dark:bg-surface-dark dark:text-ink-lightest focus:border-brand-accent focus:ring-2 focus:ring-brand-accent/20 outline-none transition-all duration-150">
                  <option value="welcome">Welcome Email</option>
                  <option value="password_reset">Password Reset</option>
                  <option value="new_assignment">New Assignment Notification</option>
                  <option value="grade_posted">Grade Posted</option>
                </select>
              </div>
              <BaseInput v-model="emailTemplate.subject" label="Email Subject" />
              <div class="flex flex-col gap-1 w-full">
                <label class="text-[13px] font-medium text-ink-mid dark:text-ink-mutedDark">Email Body (HTML Supported)</label>
                <div class="text-[12px] text-brand-accent mb-1 font-mono">Available variables: {{user.name}}, {{tenant.name}}, {{link}}</div>
                <textarea v-model="emailTemplate.body" rows="6" class="w-full px-3 py-2 font-mono text-[13px] rounded-md border transition-all duration-150 outline-none bg-surface-light text-ink-dark dark:bg-surface-dark dark:text-ink-lightest border-ink-lightest dark:border-ink-mid focus:border-brand-accent focus:ring-2 focus:ring-brand-accent/20"></textarea>
              </div>
              <div class="pt-2 flex gap-3 justify-end">
                <BaseButton variant="outline" @click="sendTestEmail">Send Test Email</BaseButton>
                <BaseButton variant="primary" @click="saveTemplate">Save Template</BaseButton>
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

const announcement = ref({
  title: '',
  message: '',
  visibility: 'all'
});

const emailTemplate = ref({
  type: 'welcome',
  subject: 'Welcome to {{tenant.name}}!',
  body: '<p>Hi {{user.name}},</p>\n<p>Welcome to our learning platform!</p>\n<p><a href="{{link}}">Click here to log in</a></p>'
});

const publishAnnouncement = () => {
  if(!announcement.value.title || !announcement.value.message) {
    alert("Please fill out the announcement fields.");
    return;
  }
  alert(`Published announcement: ${announcement.value.title}`);
  announcement.value.title = '';
  announcement.value.message = '';
};

const saveTemplate = () => {
  alert('Template saved successfully!');
};

const sendTestEmail = () => {
  alert('Test email sent to your inbox.');
};
</script>
