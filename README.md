<h1 align="center">Hey, I'm Ibrahim 👋</h1>

<p align="center">
  <b>Computer Engineering @ University of Guelph</b> · B.Eng, Class of 2029<br>
  Software Engineer, AI Training <b>@AfterQuery</b> (YC25) · Co-Founder @LiveHub
</p>

<p align="center">
  <a href="https://linkedin.com/in/ibrahimqureshi"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:ibrahimqureshi1223@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://github.com/iqureshi123"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
</p>

---

## About me

I build things that run on real hardware and real data — not just demos.

Right now I'm writing SWE-bench-style training tasks for frontier AI models at
**AfterQuery (YC25)**, which means I spend my days reading real bugs in real
codebases and building test harnesses that can tell a correct fix from a
plausible-looking one. That habit shows up in everything else I build: if I
say something works, I've run it.

Outside of work I'm usually building at the layer where software meets
something physical or messy — an emulator that runs a 1970s CPU in your
browser, a language model answering questions about your car over OBD-II, a
map that turns strangers' photographs into a permanent archive of a
neighbourhood.

- 🎓 **B.Eng Computer Engineering**, University of Guelph — expected May 2029
- 🔭 Currently building **car-ai** — an on-device LLM diagnostic assistant on a Raspberry Pi 5
- 🥉 **3rd place, TECHNATION Data Intelligence track** — SummerHacks 2026
- 📜 Certified in *AI Fluency: Framework & Foundations* (Anthropic) and *Intro to Statistics* (Stanford)

---

## Tech stack

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
![Swift](https://img.shields.io/badge/Swift-F05138?style=for-the-badge&logo=swift&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

**Frameworks & Runtime**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=for-the-badge&logo=nodedotjs&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![SwiftUI](https://img.shields.io/badge/SwiftUI-0071E3?style=for-the-badge&logo=swift&logoColor=white)
![WebAssembly](https://img.shields.io/badge/WebAssembly-654FF0?style=for-the-badge&logo=webassembly&logoColor=white)

**Platforms & Services**

![Supabase](https://img.shields.io/badge/Supabase%20(Postgres)-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white)
![Modal](https://img.shields.io/badge/Modal-7C3AED?style=for-the-badge&logo=modal&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=raspberrypi&logoColor=white)

**Tools**

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Cursor](https://img.shields.io/badge/Cursor-000000?style=for-the-badge&logo=cursor&logoColor=white)
![MATLAB](https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge&logo=mathworks&logoColor=white)
![AutoCAD](https://img.shields.io/badge/AutoCAD-E51050?style=for-the-badge&logo=autodesk&logoColor=white)
![SolidWorks](https://img.shields.io/badge/SolidWorks-E31E24?style=for-the-badge&logo=dassaultsystemes&logoColor=white)

---

## What I'm building

### 🎮 [chip8](https://github.com/iqureshi123/chip8) · `C++` · `WebAssembly`
A CHIP-8 emulator written from scratch — the same code compiles natively and to
WebAssembly, so it runs in a browser with no install. Real hardware emulation:
fetch-decode-execute loop, 4KB memory, all ~35 opcodes, XOR sprite collision.

**Verified, not just compiled** — 41 unit tests / 2200+ assertions, plus an
independently-authored public correctness ROM that reports all 18 checks OK.
One anomaly I chased turned out to be a genuine 1970s design quirk in the
original Pong ROM, confirmed by disassembling its boundary-check code.

▶️ **[Play it in your browser](https://iqureshi123.github.io/chip8/)**

### 🚗 [car-ai](https://github.com/iqureshi123/car-ai) · `Python` · `Raspberry Pi`
An on-device AI diagnostic assistant for cars. A local LLM (`llama3.2:3b`)
running on a Raspberry Pi 5 answers plain-English questions about your vehicle
by calling OBD-II tools — no cloud, no API keys, no data leaving the car.
*Currently running against simulated OBD-II data.*

### 🗺️ [LandMarked](https://github.com/iqureshi123/landmarked-summerhacks) · `TypeScript` · `MapLibre` — 🥉 3rd, TECHNATION track
A location game where you claim real places by photographing them. Claims
expire in three hours; the photographs never do. Built in 26 hours at
SummerHacks 2026 with a team of three.

I owned the frontend: a hand-drawn SVG icon system, interaction design, and
the correctness pass — including catching a stat in our own pitch deck that
the live dashboard would have contradicted on stage.

### 🔍 [patchcheck](https://github.com/iqureshi123/patchcheck) · `Python` · `Docker`
Runs AI-generated code patches inside isolated Docker containers and verifies
them against real test suites. Built on the same principle as my day job: a
patch that looks right and a patch that passes are different things.

---

## Where I'm headed

- **Extending car-ai to a live vehicle** — moving from simulated OBD-II data to a real ECU connection
- **A GameBoy emulator** — the natural next step after CHIP-8: Sharp LR35902 CPU, PPU graphics, cartridge mappers
- **More systems work** — I want to keep building at the layer where the abstraction leaks
- **Summer 2027 SWE internships** — open to opportunities

---

## Let's connect

I'm always happy to talk about emulators, on-device inference, or anything
that involves making software prove it actually works.

<p>
  <a href="https://linkedin.com/in/ibrahimqureshi"><img src="https://img.shields.io/badge/LinkedIn-Ibrahim%20Qureshi-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:ibrahimqureshi1223@gmail.com"><img src="https://img.shields.io/badge/Email-ibrahimqureshi1223%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=iqureshi123&show_icons=true&hide_border=true&theme=graywhite&hide=contribs" alt="GitHub stats" height="150">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=iqureshi123&layout=compact&hide_border=true&theme=graywhite&langs_count=6" alt="Top languages" height="150">
</p>
