<h1 align="center">Hi there 👋, I'm Ibrahim</h1>

<p align="center">
  <a href="https://www.linkedin.com/in/ibrahimqureshi123/"><img src="https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin" alt="LinkedIn"></a>
  <a href="https://github.com/iqureshi123"><img src="https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github" alt="GitHub"></a>
</p>

---

## 🧑‍💻 About Me

Currently, I'm a **Computer Engineering** student @ the **University of Guelph**
in Canada, and **Software Engineer, AI Training @AfterQuery (YC25)**.

What pulled me into computer engineering is the seam between software and
hardware, the point where code has to survive contact with a real device. That's
most of what I build. **car-ai** puts a local language model on a Raspberry Pi 5
and has it query a car's ECU over OBD-II, so the whole loop runs inside the
vehicle with nothing leaving it. **chip8** goes the other way, emulating a 1970s
CPU precisely enough that original ROMs run unmodified. In between there's
plenty of ordinary software: iOS apps, FastAPI backends, TypeScript frontends.

The areas I'm pushing into are **embedded systems with AI running on-device**,
**robotics**, and low-level systems work generally.

Most of what I know about writing software came from one habit: proving it
works. At AfterQuery I write SWE-bench-style training tasks for frontier AI
models, reading real bugs in real codebases and building test harnesses that can
tell a correct fix from a plausible-looking one. If I say something works, I've
run it.

**Right now**

- 🔧 Building **car-ai**; a local LLM on a Raspberry Pi 5 answering questions about a car over OBD-II, with nothing leaving the vehicle
- 💼 **Software Engineer, AI Training @ AfterQuery (YC25)**; evaluation tasks for frontier models
- 📱 **Co-Founder @ LiveHub**; an iOS app matching students with study partners by course and interest
- 🏆 **Winner, TECHNATION Data Intelligence track**, SummerHacks 2026
- 🎓 **B.Eng Computer Engineering**, University of Guelph, expected May 2029

---

## 🛠️ Tech Stack

**Languages**

![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)
![TypeScript](https://img.shields.io/badge/TypeScript-000?style=for-the-badge&logo=typescript)
![JavaScript](https://img.shields.io/badge/JavaScript-000?style=for-the-badge&logo=javascript)
![Java](https://img.shields.io/badge/Java-000?style=for-the-badge&logo=openjdk)
![C++](https://img.shields.io/badge/C++-000?style=for-the-badge&logo=cplusplus)
![C](https://img.shields.io/badge/C-000?style=for-the-badge&logo=c)
![Swift](https://img.shields.io/badge/Swift-000?style=for-the-badge&logo=swift)
![SQL](https://img.shields.io/badge/SQL-000?style=for-the-badge&logo=postgresql)
![HTML5](https://img.shields.io/badge/HTML5-000?style=for-the-badge&logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-000?style=for-the-badge&logo=css3)

**Frameworks & Runtime**

![FastAPI](https://img.shields.io/badge/FastAPI-000?style=for-the-badge&logo=fastapi)
![Node.js](https://img.shields.io/badge/Node.js-000?style=for-the-badge&logo=nodedotjs)
![React](https://img.shields.io/badge/React-000?style=for-the-badge&logo=react)
![SwiftUI](https://img.shields.io/badge/SwiftUI-000?style=for-the-badge&logo=swift)
![WebAssembly](https://img.shields.io/badge/WebAssembly-000?style=for-the-badge&logo=webassembly)

**Platforms & Services**

![Supabase](https://img.shields.io/badge/Supabase%20(Postgres)-000?style=for-the-badge&logo=supabase)
![Modal](https://img.shields.io/badge/Modal-000?style=for-the-badge&logo=modal)
![Docker](https://img.shields.io/badge/Docker-000?style=for-the-badge&logo=docker)
![Linux](https://img.shields.io/badge/Linux-000?style=for-the-badge&logo=linux)
![SQLite](https://img.shields.io/badge/SQLite-000?style=for-the-badge&logo=sqlite)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-000?style=for-the-badge&logo=raspberrypi)

**Tools**

![Git](https://img.shields.io/badge/Git-000?style=for-the-badge&logo=git)
![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github)
![VS Code](https://img.shields.io/badge/VS%20Code-000?style=for-the-badge&logo=visualstudiocode)
![Cursor](https://img.shields.io/badge/Cursor-000?style=for-the-badge&logo=cursor)
![MATLAB](https://img.shields.io/badge/MATLAB-000?style=for-the-badge&logo=mathworks)
![AutoCAD](https://img.shields.io/badge/AutoCAD-000?style=for-the-badge&logo=autodesk)
![SolidWorks](https://img.shields.io/badge/SolidWorks-000?style=for-the-badge&logo=dassaultsystemes)

---

## 🚀 Things I've built

**[LandMarked](https://github.com/iqureshi123/landmarked-summerhacks)** · `TypeScript` · `MapLibre`; Winner, TECHNATION track

A location game where you claim real places by photographing them. Stand at a
landmark, take one photo, and you hold it for three hours, until someone takes
it from you. The claim rotates; the photograph never does. Every accepted photo
joins that place's permanent archive, and its pixels feed a live reading of what
colour the neighbourhood is right now.

Built in 26 hours at SummerHacks 2026 with a team of three, across 4,235 real
places pulled from OpenStreetMap. I owned the frontend: a hand-drawn SVG icon
system, interaction design, and the correctness pass, including catching a
statistic in our own pitch deck that the live dashboard would have contradicted
on stage.

**[car-ai](https://github.com/iqureshi123/car-ai)** · `Python` · `Raspberry Pi`

An on-device AI diagnostic assistant for cars. A local LLM (`llama3.2:3b`)
running on a Raspberry Pi 5 answers plain-English questions about your vehicle
by calling OBD-II tools. No cloud, no API keys, no data leaving the car.
*Currently running against simulated OBD-II data.*

**[patchcheck](https://github.com/iqureshi123/patchcheck)** · `Python` · `Docker`

Runs AI-generated code patches inside isolated Docker containers and verifies
them against real test suites. Same principle as my day job: a patch that looks
right and a patch that passes are different things.

**[chip8](https://github.com/iqureshi123/chip8)** · `C++` · `WebAssembly`

A CHIP-8 emulator written from scratch. The same C++ core compiles natively and
to WebAssembly, so it runs in a browser with no install. Backed by 41 unit tests
and an independently-authored public correctness ROM.
▶ **[Play it in your browser](https://iqureshi123.github.io/chip8/)**

---

## 🔭 Where this is going

- Taking **car-ai** off simulated data and onto a live ECU in a real vehicle
- More systems work generally, I want to keep building at the layer where the abstraction leaks
- Open to **Summer 2027 computer engineering and software engineering internships**

---

## 📫 Get in touch

I'm always happy to talk about anything that involves making software prove
it actually works.

<p>
  <a href="https://www.linkedin.com/in/ibrahimqureshi123/"><img src="https://img.shields.io/badge/LinkedIn-Ibrahim%20Qureshi-000?style=for-the-badge&logo=linkedin" alt="LinkedIn"></a>
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=iqureshi123&show_icons=true&hide_border=true&theme=graywhite&hide=contribs" alt="GitHub stats" height="150">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=iqureshi123&layout=compact&hide_border=true&theme=graywhite&langs_count=6" alt="Top languages" height="150">
</p>
