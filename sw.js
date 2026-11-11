'use strict';
const CACHE='sugam-v1-20261111';
const FILES=['./','./index.html','./styles.css','./app.js','./lessons.json','./icon.svg','./manifest.webmanifest'];
self.addEventListener('install',event=>event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(FILES)).then(()=>self.skipWaiting())));
self.addEventListener('activate',event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('sugam-')&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',event=>{if(event.request.method!=='GET'||new URL(event.request.url).origin!==self.location.origin)return;event.respondWith(fetch(event.request).then(response=>{if(response.ok){const copy=response.clone();event.waitUntil(caches.open(CACHE).then(cache=>cache.put(event.request,copy)))}return response}).catch(()=>caches.match(event.request).then(response=>response||(event.request.mode==='navigate'?caches.match('./index.html'):Response.error()))))});
self.addEventListener('message',event=>{if(event.data==='CACHE_STATUS')event.waitUntil(caches.open(CACHE).then(async cache=>{const matches=await Promise.all(FILES.map(f=>cache.match(f)));if(matches.every(Boolean))event.source?.postMessage('CACHE_READY')}))});
