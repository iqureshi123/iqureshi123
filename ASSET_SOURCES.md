# Profile asset sources

- Skill Icons: https://github.com/tandpfun/skill-icons (MIT; see skill-icons-LICENSE.txt).
- Badge SVGs: https://shields.io/.
- Google Sans: https://github.com/googlefonts/googlesans and https://github.com/google/fonts/tree/main/ofl/googlesans (SIL OFL 1.1; see GoogleSans-OFL.txt). Affiliation lettering is outlined so GitHub does not need a remote font.
- University of Guelph: actual full-colour horizontal crest and wordmark, extracted from the official site header at https://www.uoguelph.ca/brand-guide/logos (official @uoguelph/web-components). Artwork is preserved, with a black backing appropriate to this white-lettered variant.
- AfterQuery blue: adapted for each theme from the public site's #2F5BB8 blue, https://www.afterquery.com/.
- Gryphon Racing crest: https://gryphonracing.org/media/crest.svg. The original white crest has a small dark backing for visibility in both themes.
- Contribution chart: GitHub contribution calendar for @iqureshi123. Refresh through scripts/update_activity.py and the profile-activity workflow.

The TinyInfer SVG is the preserved original from Cursor commit 655d7c4. SHA-256: 117583f9ffe07ef923e8a359255bd3e72e2b7d2c6e3d0abc2d7fa3538e6e9c16.

Header typography and accessibility references: [GitHub Primer typography](https://primer.style/product/primitives/typography/) and [Primer motion guidance](https://primer.style/accessibility/design-guidance/motion-and-animation/). The header is static so both the focus and availability remain visible. Run `python3 scripts/build_header.py` to rebuild the desktop/mobile and dark/light variants. No remote fonts or animation services are required.
