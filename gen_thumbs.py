#!/usr/bin/env python3
"""CC Skill Library thumbnails v3 - fully generated brand cards, NO screengrabs.

1280x720: CC gradient + texture, arrow logo top-right, command pill,
skill name in Montserrat ExtraBold (last word teal), one-line 'how it works'
in Inter Medium, small library eyebrow bottom-left. Play button is added
by the page (bottom-right), so the lower-right corner stays clear.
"""
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

POSTERS = Path.home() / "Projects/skill-library/posters"
LOGO = Path.home() / "Projects/clinic-catalyst/cc-reel-logo.png"
FONTS = os.path.expanduser("~/Library/Fonts/")

W, H = 1280, 720
HERO_DARK = (10, 42, 40)
HERO_MID = (13, 61, 56)
TEAL_BRIGHT = (0, 212, 188)
SOFT = (226, 238, 236)

F_TITLE = lambda s: ImageFont.truetype(FONTS + "Montserrat-ExtraBold.ttf", s)
F_DESC = lambda s: ImageFont.truetype(FONTS + "Inter-Medium.ttf", s)
F_PILL = lambda s: ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", s, index=1)
F_EYE = lambda s: ImageFont.truetype(FONTS + "Montserrat-ExtraBold.ttf", s)

SKILLS = {
  "content-engine-watch-first": ("/cc-content-engine", "Content Engine",
    "How your content engine plans your month across the four pillars - the foundation for everything organic."),
  "content-engine-use-what": ("/cc-content-engine", "Use What For What",
    "Which content skill to reach for, and what each one is actually for - so you never stare at a blank caption box."),
  "resonance": ("/cc-resonance", "Your Resonance",
    "Claude interviews you - who your patient is, what they feel, the words they use. The emotional spine of every ad, page and email."),
  "brand-guide": ("/cc-brand-guide", "Your Brand Guide",
    "Turns your resonance into one brand file every skill reads - so Claude sounds like your clinic, not a robot."),
  "meta-ad-copy": ("/cc-metaad-builder", "Meta Ad Copy",
    "5 headlines, 5 hooks, 5 primary texts, 5 descriptions - AHPRA-screened and ready to load into Meta."),
  "google-ads-builder": ("/cc-googlead-builder", "Google Ads Builder",
    "15 headlines, 4 descriptions, keyword plans and negatives - all length-checked and AHPRA-safe."),
  "fb-leadform": ("/cc-fb-leadform", "FB Lead Form + Captions",
    "The lead form that captures the booking - problem-plus-offer headline, value-stacked, in your converting style."),
  "landing-thankyou-page": ("/cc-landing-page", "Landing + Thank-You Page",
    "The offer page that gets the booking, and the confirmation page after it that quietly reduces no-shows."),
  "script-generator": ("/cc-script", "Script Generator",
    "Recordable, AHPRA-safe video scripts with a 3-second hook and a shot list - ready to film."),
  "talking-head-reel": ("/cc-reeltalkinghead", "Talking Head Reel Editor",
    "Raw talking-to-camera video in, captioned approval-ready reel out - it even cuts the dead air."),
  "marketing-genius-slop": ("/cc-marketing-genius", "Marketing Genius & Stop The Slop",
    "The strategy layer over any copy - then catch every AI tell before you publish."),
  "nurture-sequence": ("/cc-nurture-sequence", "Follow-Up That Never Sleeps",
    "The 7-day nurture for ad enquiries who didn't book - SMS and email touches that walk them to a consult, conversation not pressure."),
  "keyword-research": ("/cc-keyword-research", "Keyword Research",
    "What your patients actually type - the terms to build your content and ads around."),
  "geo-seo": ("/cc-geo-seo", "Getting Found In AI Search",
    "Be the clinic ChatGPT and Google's AI recommend when someone asks for one near them."),
  "ad-spy": ("/cc-ad-spy", "Ad Spy",
    "See what competitors are running - and what not to copy - so you out-position them."),
  "website-audit": ("/cc-website-audit", "Website Audit",
    "Point it at your own site and get the honest list of what's costing you bookings."),
  "assemble": ("/cc-assemble", "Stitch Clips + Music",
    "Your short clips joined into one clean edit - crossfades, music under it, sized for reels, feed or YouTube."),
  "cover": ("/cc-cover", "Reel + Story Covers",
    "A branded cover for any reel or story - your photo, your colours, your font, one punchy accent word."),
  "carousel": ("/cc-carousel", "Branded Carousels",
    "Concern-led, swipeable carousels in your brand - teach first, invite the booking last."),
  "leadform-field-mapping": ("Meta + GHL", "Map Lead Fields Into GHL",
    "The step everyone misses - connect your Facebook lead form fields to GHL so every lead lands with their answers attached."),
  "newsletter-engine": ("/cc-newsletter-engine", "Newsletter Engine",
    "Run it once a month - four fresh newsletters written from your Business Brain around the month's offer, loaded into GHL with nothing to rebuild."),
}

def background():
    bg = Image.new("RGB", (W, H))
    px = bg.load()
    for y in range(H):
        for x in range(0, W, 4):
            t = (x / W + y / H) / 2
            c = tuple(int(HERO_MID[i] + (HERO_DARK[i] - HERO_MID[i]) * t) for i in range(3))
            for dx in range(4):
                if x + dx < W:
                    px[x + dx, y] = c
    bg = bg.convert("RGBA")
    # texture: soft teal glow top-left + two thin rings lower-right
    fx = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(fx)
    d.ellipse([-320, -340, 480, 420], fill=(0, 212, 188, 26))
    d.ellipse([880, 340, 1720, 1180], outline=(0, 212, 188, 46), width=3)
    d.ellipse([1000, 460, 1600, 1060], outline=(0, 212, 188, 30), width=2)
    fx = fx.filter(ImageFilter.GaussianBlur(10))
    bg.alpha_composite(fx)
    return bg

def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur: lines.append(cur)
    return lines

logo = Image.open(LOGO).convert("RGBA")
lw = 292
logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
BG = background()
LM = 64          # left margin
MAXW = 1130      # text width budget

for slug, (cmd, title, desc) in SKILLS.items():
    im = BG.copy()
    d = ImageDraw.Draw(im)
    im.alpha_composite(logo, (W - logo.width - 40, 38))

    # command pill
    pf = F_PILL(27)
    pw = d.textlength(cmd, font=pf)
    py = 168
    d.rounded_rectangle([LM, py, LM + pw + 40, py + 52], radius=12, fill=TEAL_BRIGHT)
    d.text((LM + 20, py + 11), cmd, font=pf, fill=HERO_DARK)

    # title - autoscale so it fits 2 lines
    size = 88
    while size > 46:
        tf = F_TITLE(size)
        tlines = wrap(d, title, tf, MAXW)
        if len(tlines) <= 2: break
        size -= 6
    ty = py + 96
    gap = int(size * 0.26)
    words_total = title.split()
    accent = words_total[-1]
    for ln in tlines:
        parts = ln.split()
        x = LM
        for wd in parts:
            colr = TEAL_BRIGHT if wd == accent else (255, 255, 255)
            d.text((x, ty), wd, font=tf, fill=colr)
            x += d.textlength(wd + " ", font=tf)
        ty += size + gap

    # description
    df = F_DESC(31)
    dy = ty + 18
    for ln in wrap(d, desc, df, MAXW - 90)[:3]:
        d.text((LM, dy), ln, font=df, fill=SOFT + (228,))
        dy += 46

    # eyebrow bottom-left
    ef = F_EYE(20)
    d.text((LM, H - 72), "S K I L L   L I B R A R Y   ·   W A T C H   T H E   D E M O",
           font=ef, fill=TEAL_BRIGHT + (210,))

    im.convert("RGB").save(POSTERS / f"{slug}.jpg", quality=90)
    print("thumb:", slug)

print("done:", len(SKILLS))
