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
SANS = "Arial,Helvetica,sans-serif"


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
    width, height = (340, 382) if mobile else (680, 248)
    parts = [f'<svg xmlns="{NS}" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="about-title about-description">',
             '<title id="about-title">About Me</title>',
             '<desc id="about-description">Computer Engineering (Co-op) at the University of Guelph. Embedded Systems at Gryphon Formula Racing. Technical Director at Google Developer Group. Previously, AI Training at AfterQuery. Interests: machine learning and robotics.</desc>',
             f'<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="10" fill="{bg}" stroke="{border}"/>']

    def text(x, y, content, color=value, size=16, mono=False, bold=False):
        family = MONO if mono else SANS
        parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" font-weight="{600 if bold else 400}">{html.escape(content)}</text>')

    def label(x, y, content):
        text(x, y, content, key, 14.5, mono=True)

    if mobile:
        label(18, 30, "education:")
        text(18, 55, "Computer Engineering (Co-op)")
        text(18, 79, "@ University of Guelph")
        label(18, 117, "current_roles:")
        text(28, 145, "- Embedded Systems @")
        parts.append(asset("gryphon-racing-badge.svg", 28, 159, height=24))
        text(56, 178, "Gryphon Formula Racing", ink, bold=True)
        text(28, 211, "- Technical Director @")
        parts.append(asset(f"gdg-{theme}.svg", 46, 223, height=24))
        label(18, 270, "previously:")
        text(18, 296, "AI Training @")
        parts.append(asset(f"afterquery-{theme}.svg", 128, 277, height=24))
        label(18, 334, "interests:")
        text(18, 360, "machine learning + robotics")
    else:
        label(26, 36, "education:")
        text(136, 36, "Computer Engineering (Co-op) @ University of Guelph")
        label(26, 78, "current_roles:")
        text(42, 111, "- Embedded Systems @")
        parts.append(asset("gryphon-racing-badge.svg", 226, 92, height=24))
        text(254, 111, "Gryphon Formula Racing", ink, 17, bold=True)
        text(42, 145, "- Technical Director @")
        parts.append(asset(f"gdg-{theme}.svg", 213, 126, height=24))
        label(26, 187, "previously:")
        text(136, 187, "AI Training @")
        parts.append(asset(f"afterquery-{theme}.svg", 246, 168, height=24))
        label(26, 224, "interests:")
        text(136, 224, "[machine learning, robotics]")
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
