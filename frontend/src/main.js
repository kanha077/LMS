import { createApp } from 'vue';
import { createPinia } from 'pinia';
import './styles/app.css';
import App from './App.vue';
import router from './router';
import { useUIStore } from './stores/ui';

const pinia = createPinia();
const app = createApp(App);

app.use(pinia);
app.use(router);

// Initialize Dark Mode based on localStorage
const uiStore = useUIStore();
uiStore.applyTheme();

app.mount('#app');
