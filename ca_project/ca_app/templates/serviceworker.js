importScripts('https://storage.googleapis.com/workbox-cdn/releases/5.1.2/workbox-sw.js');

console.log('Hello from service worker');

// This will listen for messages of type: 'SKIP_WAITING' and run the skipWaiting() method, forcing the service worker to
// activate right away.
self.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        console.log("Invoked skipWaiting");
        self.skipWaiting();
    }
});

// Check if workbox loaded
if (workbox) {
    console.log("Workbox is loaded.");
} else {
    console.log("Workbox didn't load");
}

//workbox.setConfig({debug: true});

// This will trigger the importScripts() for workbox.strategies, routing etc and their dependencies:
const {strategies} = workbox;
const {routing} = workbox;
const {precaching} = workbox;
const {core} = workbox;
const cacheable_response = workbox.cacheableResponse;
const expiration = workbox.expiration;
// const {navigtaionPreload} = workbox;

// Set default cache names
core.setCacheNameDetails({
    prefix: 'awm2021',
    suffix: 'v1',
    precache: 'precache',
    runtime: 'runtime',
    googleAnalytics: 'analytics'
});