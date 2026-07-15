# Clinic Catalyst - Skill Library

Client-facing video library. Every skill in the Clinic Catalyst system, shown on video:
what it does and exactly what to type. Plays inline in the page.

- Live: https://clinic-catalyst-au.github.io/skill-library/
- Videos are web-compressed (H.264 1080p, faststart) and self-hosted in `videos/`.
- Posters (thumbnail frames) in `posters/`.

## Adding a new video (when a "Filming today" placeholder is ready)
1. Drop the web-encoded `<slug>.mp4` into `videos/` and a `<slug>.jpg` frame into `posters/`.
2. In `index.html`, swap the matching `.vcard.soon` placeholder for a real video card
   (copy the pattern from any live card: set `data-src="videos/<slug>.mp4"` and
   `poster="posters/<slug>.jpg"`).
3. Commit + push. GitHub Pages redeploys automatically.
