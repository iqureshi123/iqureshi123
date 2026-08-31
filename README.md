<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=26&duration=3200&pause=900&color=D97706&center=true&vCenter=true&width=720&height=64&lines=Hi%2C+I'm+Ibrahim+%F0%9F%91%8B;Computer+Engineering+%40+University+of+Guelph;Embedded+systems%2C+on-device+AI%2C+robotics;I+build+things+that+prove+they+work;Open+to+Summer+2027+internships" alt="Hi, I'm Ibrahim - Computer Engineering @ University of Guelph, embedded systems / on-device AI / robotics, open to Summer 2027 internships" />

<a href="https://www.linkedin.com/in/ibrahimqureshi123/"><img src="https://skillicons.dev/icons?i=linkedin" height="42" alt="LinkedIn" /></a>
&nbsp;
<a href="https://github.com/iqureshi123"><img src="https://skillicons.dev/icons?i=github" height="42" alt="GitHub" /></a>

</div>

---

## 🧑‍💻 About Me

Computer Engineering student at the **University of Guelph**, previously a
Software Engineer on AI Training at **AfterQuery (YC25)**. I'm drawn to the seam
between software and hardware, and to embedded systems, on-device AI, and
robotics. So far I've built an LLM inference engine from scratch, local
language models on a Raspberry Pi, an emulator that runs in the browser, iOS
apps, and FastAPI backends. Whether it's low-level systems work or shipping a
full-stack product, I enjoy building things that hold up when you actually run
them.

---

## 🛠️ Tech Stack

<div align="center">

**Languages**

<img src="https://skillicons.dev/icons?i=python,typescript,javascript,java,cpp,c,swift,postgresql,html,css" alt="Python, TypeScript, JavaScript, Java, C++, C, Swift, SQL, HTML, CSS" />

<br><br>

**Frameworks &amp; Runtime**

<img src="https://skillicons.dev/icons?i=fastapi,nodejs,react,webassembly" alt="FastAPI, Node.js, React, WebAssembly" />

<br><br>

**Platforms &amp; Services**

<img src="https://skillicons.dev/icons?i=aws,supabase,docker,linux,sqlite,raspberrypi" alt="AWS, Supabase, Docker, Linux, SQLite, Raspberry Pi" />

<br><br>

**Tools**

<img src="https://skillicons.dev/icons?i=git,github,vscode,matlab,autocad" alt="Git, GitHub, VS Code, MATLAB, AutoCAD" />

<br><br>

**AI &amp; Agentic Tooling**

<img src="https://img.shields.io/badge/Claude_Code-D97757?style=for-the-badge&logo=claude&logoColor=white" alt="Claude Code" />
<img src="https://img.shields.io/badge/Cursor-000000?style=for-the-badge&logo=cursor&logoColor=white" alt="Cursor" />
<img src="https://img.shields.io/badge/OpenAI_Codex-412991?style=for-the-badge" alt="OpenAI Codex" />
<img src="https://img.shields.io/badge/OpenClaw-334155?style=for-the-badge" alt="OpenClaw" />
<img src="https://img.shields.io/badge/Hermes_Agent-475569?style=for-the-badge" alt="Hermes Agent" />

<br><br>

**Also**

<img src="https://img.shields.io/badge/SwiftUI-F05138?style=for-the-badge&logo=swift&logoColor=white" alt="SwiftUI" />
<img src="https://img.shields.io/badge/Modal-7FEE64?style=for-the-badge&logo=modal&logoColor=black" alt="Modal" />
<img src="https://img.shields.io/badge/SolidWorks-E31E24?style=for-the-badge&logo=dassaultsystemes&logoColor=white" alt="SolidWorks" />

</div>

---

## 🚀 Things I've built

### [tinyinfer](https://github.com/iqureshi123/tinyinfer) — an LLM inference engine from scratch

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++" /> <img src="https://img.shields.io/badge/Metal-000000?style=for-the-badge&logo=apple&logoColor=white" alt="Metal" /> <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />

No PyTorch `generate()`, no `transformers`, no `llama.cpp`. The safetensors
parser, BPE tokenizer, forward pass, KV cache, sampler, and quantizer are all
implemented here, and it runs within 1.14× of llama.cpp on matched fp32/CPU.

Phase 7 started with a profile instead of a kernel. The profile found a one-line
float64 promotion worth 1.95× throughput: a defect that made the accuracy metric
look *better* while halving speed, which is what made it invisible to
correctness testing.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/iqureshi123/tinyinfer/main/results/quant_sensitivity_dark.svg">
  <img src="https://raw.githubusercontent.com/iqureshi123/tinyinfer/main/results/quant_sensitivity_light.svg" width="620" alt="Perplexity cost of INT4 quantization by weight matrix type" />
</picture>

<br>

Quantizing `k_proj` to INT4 costs +0.44% perplexity. Quantizing `down_proj`, at
the same bit width and group size, costs 16× more. I wrote the obvious follow-up,
mixed precision, into the README as a prediction before I measured it, and the
measurement contradicted me.

---

### [LandMarked](https://github.com/iqureshi123/landmarked-summerhacks) — SummerHacks 2026, claim real places by photographing them

<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" /> <img src="https://img.shields.io/badge/MapLibre-396CB2?style=for-the-badge&logo=maplibre&logoColor=white" alt="MapLibre" /> <img src="https://img.shields.io/badge/SummerHacks-2026-334155?style=for-the-badge" alt="SummerHacks 2026" /> <img src="https://img.shields.io/badge/%F0%9F%8F%86_Winner-TECHNATION_track-D4A017?style=for-the-badge" alt="Winner, TECHNATION track" />

Stand at a landmark, take one photo, and you hold it for three hours, until
someone takes it from you. The claim rotates; the photograph never does. Every
accepted photo joins that place's permanent archive, and its pixels feed a live
reading of what colour the neighbourhood is right now.

Built in 26 hours at SummerHacks 2026 alongside 200 other participants, with a
team of three, across 4,235 real places pulled from OpenStreetMap. I owned the
frontend: a hand-drawn SVG icon system, interaction design, and the correctness
pass, including catching a statistic in our own pitch deck that the live
dashboard would have contradicted on stage.

---

### [car-ai](https://github.com/iqureshi123/car-ai) — ask your car a question, offline

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Raspberry_Pi-A22846?style=for-the-badge&logo=raspberrypi&logoColor=white" alt="Raspberry Pi" /> <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama" />

An on-device diagnostic assistant for cars. Ask it something in plain English,
like *"is my engine running hot?"*, and a local LLM (`llama3.2:3b`) reads the
relevant OBD-II sensor and answers like a mechanic explaining it to a normal
person. No cloud, no API keys, no data leaving the car.

*Designed for a Raspberry Pi 5. The six OBD-II tools are verified by self-test
against simulated data. The full chat loop is written but has not been run
end-to-end, and nothing is validated on a vehicle yet.*

---

### [patchcheck](https://github.com/iqureshi123/patchcheck) — verify AI patches before you trust them

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />

Given a patch and a target repository, `patchcheck` applies it inside a
sandboxed Docker container with no network access and hard resource limits, runs
the repository's real tests against it, and reports pass or fail. It does this
for many patches in parallel, and results are persisted so an interrupted run
resumes without redoing work.

```
10/10 gold patches passed
10/10 empty patches correctly failed
wall clock: 4.3s
```

A patch that looks right and a patch that passes are different things.

---

## 🔭 Where this is going

- Taking **car-ai** off simulated data and onto a live ECU in a real vehicle
- A real INT4 kernel for **tinyinfer** — 96.9% of decode time is matmul, so that's where the headroom is
- More systems work generally, I want to keep building at the layer where the abstraction leaks
- Open to **Summer 2027 computer engineering and software engineering internships**

---

## 📫 Get in touch

I'm always happy to talk about anything that involves making software prove
it actually works.

<p>
  <a href="https://www.linkedin.com/in/ibrahimqureshi123/"><img src="https://img.shields.io/badge/LinkedIn-Ibrahim%20Qureshi-0A66C2?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNTYgMjU2Ij48cGF0aCBkPSJNMTg0LjcxNSAyMTcuNjg1SDIxMy45ODVDMjE2LjE5NCAyMTcuNjg1IDIxNy45ODUgMjE1Ljg5NSAyMTcuOTg1IDIxMy42ODZMMjE4IDE1MS44NDRDMjE4IDExOS41MjEgMjExLjAzNSA5NC42NzU1IDE3My4yNjIgOTQuNjc1NUMxNTguOTAzIDk0LjE0MjMgMTQ1LjM2MiAxMDEuNTQ0IDEzOC4wNTUgMTEzLjkwNEMxMzcuOTk3IDExNC4wMDIgMTM3Ljg5MyAxMTQuMDYyIDEzNy43NzkgMTE0LjA2MkMxMzcuNjAzIDExNC4wNjIgMTM3LjQ2IDExMy45MTkgMTM3LjQ2IDExMy43NDNWMTAxLjY2QzEzNy40NiA5OS40NTExIDEzNS42NyA5Ny42NjAyIDEzMy40NiA5Ny42NjAySDEwNS42ODNDMTAzLjQ3NCA5Ny42NjAyIDEwMS42ODMgOTkuNDUxMSAxMDEuNjgzIDEwMS42NlYyMTMuNjhDMTAxLjY4MyAyMTUuODkgMTAzLjQ3NCAyMTcuNjggMTA1LjY4MyAyMTcuNjhIMTM0Ljk1MUMxMzcuMTYgMjE3LjY4IDEzOC45NTEgMjE1Ljg5IDEzOC45NTEgMjEzLjY4VjE1OC4zMDdDMTM4Ljk1MSAxNDIuNjUgMTQxLjkyMSAxMjcuNDg3IDE2MS4zMzIgMTI3LjQ4N0MxODAuNDY3IDEyNy40ODcgMTgwLjcxNSAxNDUuNDAzIDE4MC43MTUgMTU5LjMyMVYyMTMuNjg1QzE4MC43MTUgMjE1Ljg5NCAxODIuNTA2IDIxNy42ODUgMTg0LjcxNSAyMTcuNjg1WiIgZmlsbD0id2hpdGUiLz48cGF0aCBkPSJNMzggNTkuNjI3NUMzOCA3MS40OTIxIDQ3Ljc2NzUgODEuMjUzOSA1OS42MzIxIDgxLjI1MzlDNzEuNDk0NCA4MS4yNTI4IDgxLjI1NTEgNzEuNDg1MyA4MS4yNTUxIDU5LjYyM0M4MS4yNTI4IDQ3Ljc2MDcgNzEuNDkxIDM4IDU5LjYyNzUgMzhDNDcuNzYzIDM4IDM4IDQ3Ljc2MyAzOCA1OS42Mjc1WiIgZmlsbD0id2hpdGUiLz48cGF0aCBkPSJNNDQuOTU4OCAyMTcuNjg1SDc0LjI2NTlDNzYuNDc1MSAyMTcuNjg1IDc4LjI2NTkgMjE1Ljg5NCA3OC4yNjU5IDIxMy42ODVWMTAxLjY2Qzc4LjI2NTkgOTkuNDUxMSA3Ni40NzUxIDk3LjY2MDIgNzQuMjY1OSA5Ny42NjAySDQ0Ljk1ODhDNDIuNzQ5NyA5Ny42NjAyIDQwLjk1ODggOTkuNDUxMSA0MC45NTg4IDEwMS42NlYyMTMuNjg1QzQwLjk1ODggMjE1Ljg5NCA0Mi43NDk3IDIxNy42ODUgNDQuOTU4OCAyMTcuNjg1WiIgZmlsbD0id2hpdGUiLz48L3N2Zz4=&logoColor=white" alt="LinkedIn"></a>
</p>
