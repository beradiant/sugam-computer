import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const data=JSON.parse(fs.readFileSync(new URL('./lessons.json',import.meta.url)));
const code=fs.readFileSync(new URL('./app.js',import.meta.url),'utf8');
const context=vm.createContext({});
const iconCode=code.slice(code.indexOf('function icon('),code.indexOf('function keycaps('));
const sceneCode=code.slice(code.indexOf('function scene('),code.indexOf('function voicesChanged('));
vm.runInContext(`const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));${iconCode}${sceneCode}`,context);
const ids=new Set();let steps=0;let failures=[];
for(const l of data.lessons){assert(!ids.has(l.id),'duplicate lesson ID');ids.add(l.id);assert(data.categories.includes(l.category));assert(l.steps.length>0);for(const h of l.help)assert(data.help[h],`Missing help ${h}`);for(const s of l.sources)assert(data.sources[s]);for(const s of l.steps){steps++;for(const key of ['title','instruction','mouse','expected','scene','target'])assert(s[key],`Missing ${key} in ${l.id}`);const html=vm.runInContext(`scene(${JSON.stringify(s.scene)},${JSON.stringify(s.target)})`,context);const targets=(html.match(/native-target/g)||[]).length;if(targets!==1)failures.push({id:l.id,title:s.title,target:s.target,targets});assert(!html.includes('undefined'),'undefined in scene');}}
assert.deepEqual(failures,[],JSON.stringify(failures));
console.log(`PASS: ${ids.size} lessons, ${steps} steps, ${Object.keys(data.help).length} help paths; each teaching screen has exactly one target.`);
