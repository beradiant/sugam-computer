# सुगम · Sugam Computer

A Hindi, keyboard-first computer learning companion. Large text, magnification guidance, task search, step-by-step instructions and optional spoken guidance are the main experience.

## Current version

- **52 guides, 149 steps, 48 help/recovery entries**, across nine categories.
- Windows basics and accessibility; Wi-Fi, Bluetooth, hotspot and Phone Link; file management; Chrome; Gmail and PDFs; WhatsApp for Windows; Word and typing; maintenance.
- Each step provides keyboard actions, mouse equivalent and expected result.
- Guides include email → PDF and WhatsApp video call → screen sharing.
- Illustrative Windows/app teaching interfaces, target highlighting, separate visual zoom and enlarged dialog.
- Guided target-identification practice and native copy/paste practice.
- Text size 100–180%, contrast theme, visible focus, semantic controls, skip link, reflow and reduced-motion support.
- Local progress/resume, learned filter, JSON progress/preferences backup and restore.
- Same-origin service-worker cache for offline guide access after successful loading.
- No account requirement, analytics, external font/image CDN, build step, package installation or API secret.

## Run

Download or clone the repository, then serve its root:

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000`. On Windows, use `py -m http.server 8000` if Python is installed with the launcher.

Opening `index.html` directly as a `file:` URL will not work because the guide loads `lessons.json`. Offline caching requires HTTPS or localhost and a supported browser. Other devices need a reachable hosted HTTPS origin; their localhost is not this computer.

This repository stores the app source. Creating the repository does **not** publish a live website. Deploy these static root files to a static HTTPS host when ready. Do not upload `build-content.py` or `check.mjs` as runtime dependencies; only the seven files listed below are needed. The relative URLs and hash routes support a repository subpath. GitHub Pages is an option when the account/visibility plan supports it; this private repository has not had Pages enabled.

Runtime files:

```text
index.html
styles.css
app.js
lessons.json
sw.js
icon.svg
manifest.webmanifest
```

## Hindi speech: what is and is not included

The app uses the browser's Web Speech API. It discovers Hindi (`hi-*`) voices and prefers voices whose names identify Natural/Neural quality. Users can choose a voice, test it, change speed, stop playback and opt into reading subsequent steps.

Natural speech availability is **not guaranteed**. Browser access to a voice is different from the voice being available in another app such as Edge Read aloud. When no Hindi voice is exposed, the app says so and keeps the written guide usable. It does not silently use an English voice to read Hindi.

Local voices may work offline. Provider-backed voices may need internet and may send lesson text to that provider. No custom TTS service, paid generation, account credentials or embedded API key is included. A consistent natural Hindi recording pack or authenticated TTS backend would be a future enhancement.

## Graphics and coverage boundaries

The visuals are **illustrative teaching recreations**, not actual screenshots and not a 99.9%-matching clone of any particular Windows/app version. Personal Windows theme, display scaling, window dimensions, language, release and app updates affect appearance. Actual device screenshots would be needed to validate and improve matching. Highlighted labels are teaching cues; some simplify the real icon/menu arrangement.

Practice recognizes the highlighted target; it is **not a full Windows emulator** and does not reproduce every real dialog or key sequence. It never controls real apps, starts a call, shares the actual screen, reads Gmail or sends messages.

Help entries cover common, documented or expected cases and provide an unknown-message route. They are not an exhaustive list of every possible popup. Guides intentionally avoid a hardcoded number of Tab presses and avoid blanket permission approvals. Real steps should be checked against the intended computer before relying on them for independent training. Sources accompany each guide.

## Accessibility behavior

- Guide controls work with Tab, Shift+Tab and Enter; native dialogs support Escape and focus return.
- Action keys such as Win+E belong to the actual operating system. They are not globally captured by the practice surface.
- App-only shortcuts, outside form fields and modal dialogs: `Alt+Shift+Right` next, `Alt+Shift+Left` previous, `Alt+Shift+S` speak.
- Sequential keys are labeled “फिर”; simultaneous chords use “+”.
- Graphics deliberately preserve desktop layout and can scroll within their own frame. Main content reflows.
- Size/contrast preferences do not alter the illustrated reference app's colors or text dimensions; use the visual enlargement controls for those.
- For use on a phone alongside the laptop, open the hosted guide on the phone while performing tasks on the laptop.

## Expand the curriculum

`build-content.py` is the editable content source. Add `L(...)` lessons with `S(...)` steps, help IDs and official reference keys, then regenerate:

```sh
python3 build-content.py
node --check app.js
node --check sw.js
node check.mjs
```

Each step has `title`, `keys`, `instruction`, `mouse`, `expected`, `scene`, and `target`. Each scene renderer must produce exactly one highlighted target. To add a different kind of interface, extend `scene()` in `app.js`. Update the cache name in `sw.js` when releasing changed files.

## Validation performed

- JavaScript syntax checks and curriculum/renderer consistency checks passed: 52 distinct lesson IDs, 149 nonempty steps, valid help/source references and exactly one visual target per step.
- Cloud Chrome browser checks: task search; Gmail PDF lesson next/previous flow; contextual recovery dialog; Escape dismissal; practice target with Enter; completion and learned state; persisted resume after reload; voice availability/fallback; text size 180%; contrast rendering; visible WhatsApp call controls.
- Main page had no horizontal overflow at the tested desktop viewport and 180% app text size. Dedicated phone-sized viewport and real assistive-device testing are still needed.
- Guide reloaded from the service-worker cache after its server was stopped.
- Hindi audio playback quality could not be tested: the test browser exposed no Hindi voice. No claim of audio quality verification.
- No real Windows installation or live Gmail/WhatsApp/Word account actions were used for end-to-end task validation. Latest third-party UI fidelity remains unverified.

Content reference review: 11 November 2026. Windows, Chrome, Gmail, WhatsApp and Word belong to their respective owners; this is an independent guide.
