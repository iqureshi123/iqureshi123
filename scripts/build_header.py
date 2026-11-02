#!/usr/bin/env python3
"""Build animated, theme-aware profile headers with readable mobile variants."""

from pathlib import Path
import html
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FONT = "'Avenir Next','Segoe UI',Arial,sans-serif"


def header(theme, mobile=False):
    dark = theme == "dark"
    ink = "#edf0f6" if dark else "#1f2328"
    accent = "#a5cbbb" if dark else "#216e55"
    muted = "#9da7b3" if dark else "#59636e"
    gradient = ("#a7bddb", "#c8b9dd", "#a5cbbb") if dark else ("#315b8c", "#76528f", "#216e55")
    width, height = (340, 140) if mobile else (680, 136)
    center = width / 2
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="name-title name-desc">',
        '<title id="name-title">Ibrahim Qureshi</title>',
        '<desc id="name-desc">Interested in machine learning and robotics. Open to Summer 2027 internships and co-ops.</desc>',
        '''<style>
        .interest{opacity:1}.availability{opacity:0}.reduced{display:none}
        @media(prefers-reduced-motion:no-preference){
          .interest{animation:interest-fade 14s cubic-bezier(.45,0,.55,1) infinite}
          .availability{animation:availability-fade 14s cubic-bezier(.45,0,.55,1) infinite}
          @keyframes interest-fade{
            0%,38%,100%{opacity:1;transform:translateY(0);filter:blur(0)}
            45%{opacity:0;transform:translateY(-6px);filter:blur(3px)}
            88%{opacity:0;transform:translateY(6px);filter:blur(3px)}
            95%{opacity:1;transform:translateY(0);filter:blur(0)}
          }
          @keyframes availability-fade{
            0%,38%{opacity:0;transform:translateY(6px);filter:blur(3px)}
            45%,88%{opacity:1;transform:translateY(0);filter:blur(0)}
            95%{opacity:0;transform:translateY(-6px);filter:blur(3px)}
            100%{opacity:0;transform:translateY(6px);filter:blur(3px)}
          }
        }
        @media(prefers-reduced-motion:reduce){.cycle{display:none}.reduced{display:inline}}
        </style>''',
        f'<defs><linearGradient id="focus-gradient" x1="0" y1="0" x2="1" y2="0"><stop stop-color="{gradient[0]}"/><stop offset=".5" stop-color="{gradient[1]}"/><stop offset="1" stop-color="{gradient[2]}"/></linearGradient></defs>',
    ]

    def text(y, content, size, color, weight=400, tracking=0):
        parts.append(
            f'<text x="{center:g}" y="{y}" text-anchor="middle" fill="{color}" '
            f'font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
            f'letter-spacing="{tracking}">{html.escape(content)}</text>'
        )

    text(49 if mobile else 55, "Ibrahim Qureshi", 32 if mobile else 46, ink, 650, -1)
    parts.append('<g class="cycle"><g class="interest">')
    text(96 if mobile else 101, "Machine learning + robotics", 17 if mobile else 21, "url(#focus-gradient)", 500)
    parts.append('</g><g class="availability">')
    if mobile:
        text(87, "Open to Summer 2027", 15.5, "url(#focus-gradient)", 500)
        text(109, "internships & co-ops", 15.5, "url(#focus-gradient)", 500)
    else:
        text(101, "Open to Summer 2027 internships & co-ops", 17.5, "url(#focus-gradient)", 500)
    parts.append('</g></g><g class="reduced">')
    text(80 if mobile else 90, "Machine learning + robotics", 17 if mobile else 21, accent, 500)
    if mobile:
        text(108, "Open to Summer 2027", 12.5, muted)
        text(126, "internships & co-ops", 12.5, muted)
    else:
        text(119, "Open to Summer 2027 internships & co-ops", 13, muted)
    parts.append('</g></svg>\n')
    return '\n'.join(parts)


if __name__ == "__main__":
    for theme in ("dark", "light"):
        for mobile in (False, True):
            name = f"name-mobile-{theme}.svg" if mobile else ("name.svg" if theme == "dark" else "name-light.svg")
            content = header(theme, mobile)
            ET.fromstring(content)
            (ROOT / name).write_text(content)
            print(name)
