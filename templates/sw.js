const VERSION = '{{ version }}';

self.addEventListener('install', (event) => {
    console.log('[SW] Installing SW version:', VERSION);
});