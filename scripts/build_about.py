#!/usr/bin/env python3
"""Build responsive About Me panels while preserving local affiliation artwork."""

import html
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "profile" if (ROOT / "profile" / "README.md").exists() else ROOT
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"


def asset(name, x, y, width=None, height=None):
    source = (ASSETS / name).read_text()
    prefix = name.replace(".svg", "") + "-"
    for ident in re.findall(r'\bid="([^"]+)"', source):
        source = source.replace(f'id="{ident}"', f'id="{prefix}{ident}"')
        source = source.replace(f'url(#{ident})', f'url(#{prefix}{ident})')
        source = source.replace(f'href="#{ident}"', f'href="#{prefix}{ident}"')
    source = re.sub(r'(?<=\.)cls-(\d+)', lambda m: prefix + "cls-" + m[1], source)
    source = re.sub(r'class="cls-(\d+)"', lambda m: f'class="{prefix}cls-{m[1]}"', source)
    root = ET.fromstring(source)
    viewbox = root.attrib["viewBox"].split()
    ratio = float(viewbox[2]) / float(viewbox[3])
    if width is None:
        width = height * ratio
    if height is None:
        height = width / ratio
    root.attrib.update(x=str(x), y=str(y), width=str(width), height=str(height))
    return ET.tostring(root, encoding="unicode")


def panel(theme, mobile=False):
    dark = theme == "dark"
    bg, border = ("#151b23", "#30363d") if dark else ("#f6f8fa", "#d1d9e0")
    key = "#8fc6b6" if dark else "#116b58"
    value = "#add1ec" if dark else "#185b8c"
    ink = "#e6edf3" if dark else "#24292f"
    width, height = (340, 416) if mobile else (680, 294)
    parts = [f'<svg xmlns="{NS}" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="about-title about-description">',
             '<title id="about-title">About Ibrahim Qureshi</title>',
             '<desc id="about-description">Computer Engineering (Co-op) at the University of Guelph. Embedded Systems at Gryphon Formula Racing. Technical Director at Google Developer Group. Previously, AI Training at AfterQuery. Interests: machine learning and robotics.</desc>',
             f'<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="10" fill="{bg}" stroke="{border}"/>']

    def text(x, y, content, color=value, size=None, sans=False, bold=False):
        family = "-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif" if sans else MONO
        size = size or (15.5 if mobile else 17)
        parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" font-weight="{600 if bold else 400}">{html.escape(content)}</text>')

    if mobile:
        text(18, 31, "name:", key)
        text(92, 31, "Ibrahim Qureshi")
        text(18, 63, "education:", key)
        text(18, 88, "Computer Engineering (Co-op)")
        text(18, 116, "@ University of Guelph")
        text(18, 154, "current_roles:", key)
        text(28, 182, "- Embedded Systems @")
        text(46, 209, "Gryphon Formula Racing", ink, 16, sans=True, bold=True)
        parts.append(asset("gryphon-racing-badge.svg", 257, 190, height=24))
        text(28, 242, "- Technical Director @")
        parts.append(asset(f"gdg-{theme}.svg", 46, 252, height=24))
        text(18, 305, "previously:", key)
        text(18, 331, "AI Training @")
        parts.append(asset(f"afterquery-{theme}.svg", 151, 313, height=24))
        text(18, 369, "interests:", key)
        text(18, 395, "machine learning + robotics")
    else:
        text(26, 36, "name:", key)
        text(174, 36, "Ibrahim Qureshi")
        text(26, 82, "education:", key)
        text(174, 82, "Computer Engineering (Co-op) @ University of Guelph", size=16)
        text(26, 125, "current_roles:", key)
        text(46, 159, "- Embedded Systems @", size=16)
        text(249, 159, "Gryphon Formula Racing", ink, 17, sans=True, bold=True)
        parts.append(asset("gryphon-racing-badge.svg", 475, 140, height=24))
        text(46, 193, "- Technical Director @", size=16)
        parts.append(asset(f"gdg-{theme}.svg", 267, 174, height=24))
        text(26, 233, "previously:", key)
        text(174, 233, "AI Training @", size=16)
        parts.append(asset(f"afterquery-{theme}.svg", 308, 214, height=24))
        text(26, 270, "interests:", key)
        text(174, 270, "[machine learning, robotics]", size=16)
    parts.append("</svg>\n")
    return "".join(parts)


if __name__ == "__main__":
    folders = [ROOT / "profile", ROOT / "public"] if ASSETS != ROOT else [ROOT]
    for theme in ("dark", "light"):
        for mobile in (False, True):
            name = f"about-{'mobile-' if mobile else ''}{theme}.svg"
            content = panel(theme, mobile)
            ET.fromstring(content)
            for folder in folders:
                (folder / name).write_text(content)
            print(name)
