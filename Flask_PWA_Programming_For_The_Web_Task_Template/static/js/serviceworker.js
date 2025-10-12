const assets = [
  "/",
  "static/css/style.css",
  "static/js/app.js",
  "static/images/logo.png",
  "static/images/favicon.png",
  "static/icons/icon-128x128.png",
  "static/icons/icon-192x192.png",
  "static/icons/icon-384x384.png",
  "static/icons/icon-512x512.png",
  "static/icons/desktop_screenshot.png",
  "static/icons/mobile_screenshot.png"
];

const CATALOGUE_ASSETS = "catalogue-assets";

self.addEventListener("install", (installEvt) => {
  installEvt.waitUntil(
    caches
      .open(CATALOGUE_ASSETS)
      .then((cache) => {
        console.log("Caching assets...");
        cache.addAll(assets);
      })
      .then(() => self.skipWaiting())
      .catch((e) => console.log("Cache install failed:", e))
  );
});

self.addEventListener("activate", (evt) => {
  evt.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(
        keyList.map((key) => {
          if (key !== CATALOGUE_ASSETS) {
            console.log("Removing old cache:", key);
            return caches.delete(key);
          }
        })
      );
    })
  );
  self.clients.claim();
});

self.addEventListener("fetch", (evt) => {
  evt.respondWith(
    fetch(evt.request).catch(() =>
      caches.open(CATALOGUE_ASSETS).then((cache) => cache.match(evt.request))
    )
  );
});
