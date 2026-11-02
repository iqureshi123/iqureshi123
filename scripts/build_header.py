#!/usr/bin/env python3
"""Build static, theme-aware profile headers with readable mobile variants."""

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
    width, height = (340, 140) if mobile else (680, 136)
    center = width / 2
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="name-title name-desc">',
        '<title id="name-title">Ibrahim Qureshi</title>',
        '<desc id="name-desc">Interested in machine learning and robotics. Open to Summer 2027 internships and co-ops.</desc>',
    ]

    def text(y, content, size, color, weight=400, tracking=0):
        parts.append(
            f'<text x="{center:g}" y="{y}" text-anchor="middle" fill="{color}" '
            f'font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
            f'letter-spacing="{tracking}">{html.escape(content)}</text>'
        )

    text(49 if mobile else 55, "Ibrahim Qureshi", 32 if mobile else 46, ink, 650, -1)
    text(80 if mobile else 90, "Machine learning + robotics", 17 if mobile else 21, accent, 500)
    if mobile:
        text(108, "Open to Summer 2027", 12.5, muted)
        text(126, "internships & co-ops", 12.5, muted)
    else:
        text(119, "Open to Summer 2027 internships & co-ops", 13, muted)
    parts.append('</svg>\n')
    return '\n'.join(parts)


if __name__ == "__main__":
    for theme in ("dark", "light"):
        for mobile in (False, True):
            name = f"name-mobile-{theme}.svg" if mobile else ("name.svg" if theme == "dark" else "name-light.svg")
            content = header(theme, mobile)
            ET.fromstring(content)
            (ROOT / name).write_text(content)
            print(name)
