#!/usr/bin/env python3
"""Render a local GitHub activity SVG from the public contribution calendar."""

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import urllib.request
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
QUERY = '''{ user(login:"iqureshi123") {
  login repositories(privacy:PUBLIC) { totalCount }
  contributionsCollection {
    contributionCalendar { totalContributions weeks {
      contributionDays { date contributionCount }
    } }
  }
} }'''


def fetch():
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        request = urllib.request.Request(
            "https://api.github.com/graphql",
            data=json.dumps({"query": QUERY}).encode(),
            headers={"Authorization": f"Bearer {token}",
                     "Content-Type": "application/json", "User-Agent": "profile-activity"},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    return json.loads(subprocess.check_output(
        ["gh", "api", "graphql", "-f", f"query={QUERY}"], text=True))


def render(payload):
    if payload.get("errors"):
        raise ValueError("GitHub returned GraphQL errors; keeping the previous card.")
    user = payload["data"]["user"]
    if user["login"] != "iqureshi123":
        raise ValueError("Unexpected GitHub account.")
    calendar = user["contributionsCollection"]["contributionCalendar"]
    weeks = calendar["weeks"]
    days = [day for week in weeks for day in week["contributionDays"]]
    if not days or len(weeks) < 50:
        raise ValueError("Incomplete calendar; keeping the previous card.")
    months = defaultdict(int)
    for day in days:
        months[day["date"][:7]] += day["contributionCount"]
    counts = [months[month] for month in sorted(months)]
    total = calendar["totalContributions"]
    active = sum(day["contributionCount"] > 0 for day in days)
    repos = user["repositories"]["totalCount"]
    start = dt.date.fromisoformat(days[0]["date"])
    end = dt.date.fromisoformat(days[-1]["date"])
    maximum = max(max(counts), 1)
    ceiling = ((maximum + 9) // 10) * 10
    left, right, top, bottom = 300, 644, 44, 142
    points = [(left + i * (right-left)/(len(counts)-1),
               bottom - count/ceiling*(bottom-top)) for i, count in enumerate(counts)]
    line = "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in points)
    area = f"{line} L {right} {bottom} L {left} {bottom} Z"
    span = f"{start:%b %Y} to {end:%b %Y}"
    middle = dt.date.fromisoformat(sorted(months)[len(months)//2] + "-01")
    peak_index = counts.index(max(counts))
    peak_x, peak_y = points[peak_index]
    peak_month = dt.date.fromisoformat(sorted(months)[peak_index] + "-01")
    peak_label = f"Most active: {peak_month:%b %Y}" if max(counts) else "Awaiting first contribution"
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="680" height="202" viewBox="0 0 680 202" role="img" aria-labelledby="activity-title activity-desc">
  <title id="activity-title">GitHub activity</title>
  <desc id="activity-desc">{total} contributions over the past year, {active} active days, and {repos} public repositories. Monthly counts from {span}, including partial first and last months. Updated {end:%d %b %Y}. Source: GitHub contribution calendar. Contributions can include anonymized private activity allowed by the profile settings.</desc>
  <defs>
    <linearGradient id="trace-color"><stop stop-color="#9cb3d2"/><stop offset=".55" stop-color="#b2b2c9"/><stop offset="1" stop-color="#9ebcc5"/></linearGradient>
    <linearGradient id="trace-area" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#99b2d8" stop-opacity=".2"/><stop offset="1" stop-color="#99b2d8" stop-opacity=".02"/></linearGradient>
  </defs>
  <style>
    .trace-line{{stroke-dasharray:1000;stroke-dashoffset:0}}
    .peak-halo{{opacity:.25}}
    @media(prefers-reduced-motion:no-preference){{
      .trace-line{{animation:trace-in 1.8s cubic-bezier(.22,1,.36,1) both}}
      .peak-halo{{animation:signal-pulse 5s cubic-bezier(.32,0,.67,1) infinite}}
      @keyframes trace-in{{from{{stroke-dashoffset:1000}}to{{stroke-dashoffset:0}}}}
      @keyframes signal-pulse{{0%,100%{{opacity:.15}}50%{{opacity:.5}}}}
    }}
  </style>
  <rect x=".5" y=".5" width="679" height="201" rx="12" fill="#0d1117" stroke="#30363d"/>
  <g font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif">
    <text x="26" y="35" font-size="16" font-weight="600" fill="#f0f6fc">@iqureshi123</text>
    <text x="26" y="91" font-size="44" font-weight="650" fill="#99b2d8">{total:,}</text>
    <text x="26" y="115" font-size="13" fill="#c9d1d9">contributions in the past year</text>
    <text x="26" y="145" font-size="12" fill="#9198a1">{repos} public repos · {active} active days</text>
    <text x="26" y="165" font-size="11" fill="#a6b3c4">{peak_label}</text>
    <text x="300" y="29" font-size="11" fill="#9198a1">Monthly contributions</text>
    <line x1="{left}" y1="{top}" x2="{right}" y2="{top}" stroke="#21262d"/>
    <line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="#30363d"/>
    <g>
      <path d="{area}" fill="url(#trace-area)"/>
      <path class="trace-line" pathLength="1000" d="{line}" fill="none" stroke="url(#trace-color)" stroke-width="2" stroke-linejoin="round"/>
      {''.join(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.5" fill="#a7b9d1"/>' for x, y in points)}
      <circle class="peak-halo" cx="{peak_x:.2f}" cy="{peak_y:.2f}" r="8" fill="none" stroke="#c0c6da" stroke-width="1.5"/>
    </g>
    <text x="651" y="{top+4}" font-size="10" fill="#9198a1">{ceiling}</text>
    <text x="651" y="{bottom+4}" font-size="10" fill="#9198a1">0</text>
    <text x="{left}" y="163" font-size="10" fill="#9198a1">{start:%b %y}</text>
    <text x="{(left+right)/2}" y="163" text-anchor="middle" font-size="10" fill="#9198a1">{middle:%b %y}</text>
    <text x="{right}" y="163" text-anchor="end" font-size="10" fill="#9198a1">{end:%b %y}</text>
    <text x="26" y="183" font-size="10" fill="#9198a1">Source: GitHub</text>
    <text x="654" y="183" text-anchor="end" font-size="10" fill="#9198a1">Updated {end:%d %b %Y}</text>
  </g>
</svg>
'''
    folders = [ROOT / "profile", ROOT / "public"] if (ROOT / "profile" / "README.md").exists() else [ROOT]
    for folder in folders:
        path = folder / "activity.svg"
        path.parent.mkdir(exist_ok=True)
        path.write_text(svg)
    print(f"Rendered {total} contributions, {repos} public repos, {active} active days ({end}).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", type=Path, help="Use a previously fetched GitHub response.")
    args = parser.parse_args()
    render(json.loads(args.snapshot.read_text()) if args.snapshot else fetch())
