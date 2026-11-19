/**
 * Service Worker for Offline PWA Support
 * Caches all local HTML, CSS, JS, and JSON data files so student can prepare
 * without an active internet connection.
 */

const CACHE_NAME = 'python-exam-master-v2';

const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './notes.html',
  './topic.html',
  './practice.html',
  './programs.html',
  './exam.html',
  './model-papers.html',
  './revision.html',
  './progress.html',
  './manifest.json',
  './assets/icon-192.png',
  './assets/icon-512.png',
  './css/main.css',
  './css/notes.css',
  './css/exam.css',
  './css/mobile.css',
  './js/storage.js',
  './js/app.js',
  './data/syllabus.json',
  './data/notes.json',
  './data/questions.json',
  './data/programs.json',
  './data/model-papers.json',
  './data/revision.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('Caching all offline study assets for Python Exam Master');
      return cache.addAll(ASSETS_TO_CACHE);
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.map(key => {
          if (key !== CACHE_NAME) {
            console.log('Clearing older cache', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(cachedResponse => {
      if (cachedResponse) {
        return cachedResponse;
      }
      return fetch(event.request).catch(() => {
        // Fallback for document navigation
        if (event.request.mode === 'navigate') {
          return caches.match('./index.html');
        }
      });
    })
  );
});

