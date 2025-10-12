if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker
      .register('/static/js/serviceworker.js')
      .then(reg => console.log('✅ Service Worker registered:', reg))
      .catch(err => console.error('❌ Service Worker not registered', err));
  });
}
