self.addEventListener('install', function(event) {
    console.log('Service worker installing...');
    event.waitUntil(
        caches.open('v1').then(function(cache) {
            console.log('Service worker installing...');
            return cache.addAll([
                '/',
                '/us/',
                '/India/',
                '/assets/'
            ]);
        })
    );
})

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {
            return response || fetch(event.request);
        })
    );
})
