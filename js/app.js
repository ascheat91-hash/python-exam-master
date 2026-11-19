/**
 * Main Application Script: Common Navigation, Header, Offline Detection & Theme Toggling
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Theme toggle button handler
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  if (themeToggleBtn) {
    const updateIcon = () => {
      const current = StorageManager.getTheme();
      themeToggleBtn.innerHTML = current === 'dark' ? '☀️' : '🌙';
    };
    updateIcon();

    themeToggleBtn.addEventListener('click', () => {
      const current = StorageManager.getTheme();
      const next = current === 'dark' ? 'light' : 'dark';
      StorageManager.setTheme(next);
      updateIcon();
    });
  }

  // 2. Offline / Online Indicator
  const offlineBanner = document.getElementById('offline-banner');
  const updateOnlineStatus = () => {
    if (!offlineBanner) return;
    if (navigator.onLine) {
      offlineBanner.classList.remove('visible');
    } else {
      offlineBanner.classList.add('visible');
    }
  };
  window.addEventListener('online', updateOnlineStatus);
  window.addEventListener('offline', updateOnlineStatus);
  updateOnlineStatus();

  // 3. Highlight current page in Bottom Nav
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.bottom-nav .nav-item').forEach(item => {
    const href = item.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      item.classList.add('active');
    }
  });

  // 4. Register Service Worker for Offline PWA Capabilities
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('./sw.js')
      .then(reg => {
        console.log('ServiceWorker registered successfully:', reg.scope);
      })
      .catch(err => {
        console.log('ServiceWorker registration note:', err);
      });
  }
});

// Utility to fetch local JSON safely
async function loadJSON(path) {
  try {
    const res = await fetch(path);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error(`Failed loading ${path}:`, err);
    return null;
  }
}

