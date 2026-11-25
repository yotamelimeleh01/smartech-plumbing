"""Builds the Smartech Plumbing website into the parent folder.

Run:  python _build/build.py
GitHub Pages (Jekyll) ignores folders starting with "_", so this script is not published.
"""
import html
import json
from datetime import date
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
SITE_URL = "https://yotamelimeleh01.github.io/smartech-plumbing"
BRAND = "Smartech Plumbing"
PHONE = {"disp": "(866) 956-0757", "tel": "+18669560757"}
FB_PAGE = "https://www.facebook.com/profile.php?id=61597012678069"
MESSENGER = "https://m.me/61597012678069"
HOURS = "Sunday to Thursday, 7 AM to 9 PM"
e = html.escape

SERVICES = [
    ("water-heaters", "&#128293;", "Water Heater Repair & Replacement",
     "No hot water, leaking tank, rusty water or a pilot that won't stay lit. Tank and tankless, gas and electric.",
     "water-heater-tech.jpg"),
    ("leaks", "&#128167;", "Leak Detection & Pipe Repair",
     "Dripping pipes, wet cabinets, water stains and burst lines found and fixed before they cause more damage.",
     "under-sink-repair.jpg"),
    ("drains", "&#127744;", "Drain Cleaning",
     "Slow or clogged sinks, tubs, showers and main lines cleared and flowing again.", "kitchen-drain.jpg"),
    ("toilets", "&#128703;", "Toilet Repair & Installation",
     "Running, clogged, leaking or wobbly toilets repaired, or a new one installed.", "toilet-repair.jpg"),
    ("faucets", "&#128688;", "Faucets & Fixtures",
     "Kitchen and bathroom faucets, shower valves, garbage disposals and fixture upgrades.", "kitchen-faucet.jpg"),
    ("installs", "&#128295;", "Repairs & Installs",
     "Shut-off valves, supply lines, hose bibs and everyday plumbing fixes around the home.", "bathroom.jpg"),
]

WH_SIGNS = ["No hot water, or it runs out fast", "Water pooling around the base of the tank",
            "Rusty or discolored hot water", "Popping, rumbling or banging noises",
            "Pilot light won't stay lit, or the breaker keeps tripping", "The tank is 10+ years old"]

FAQ = [
    ("How fast can you come out?", "Same-day service is often available. Call us and we'll give you the earliest time we have."),
    ("Should I repair or replace my water heater?", "If the tank is leaking from the body or is more than 10 to 12 years old, replacement is usually the better value. Many other problems, like a bad thermostat, element, igniter or valve, can be repaired. We'll walk you through both options and the price before any work starts."),
    ("Do you work on tankless water heaters?", "Yes. We service tank and tankless water heaters, both gas and electric."),
    ("How much does it cost?", "It depends on the problem and the parts needed. You'll get the price up front, before any work starts. No surprises."),
    ("What should I do if my water heater is leaking?", "Turn off the cold water supply valve on top of the tank and turn off the power (electric) or set the gas valve to \"off\" or \"pilot\". Then call us."),
    ("What are your hours?", f"{HOURS}."),
]


def faq_block(items):
    return '<div class="faq">' + "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in items) + "</div>"


def call_btn(cls="btn"):
    return f'<a class="{cls}" href="tel:{PHONE["tel"]}"><small>Call now</small><b>{PHONE["disp"]}</b></a>'


def msg_btn():
    return f'<a class="btn blue" href="{MESSENGER}" target="_blank" rel="noopener"><small>Prefer to text?</small><b>Message us</b></a>'


def photo(r, src, alt, ratio=None):
    style = f' style="aspect-ratio:{ratio}"' if ratio else ""
    return f'<div class="photo"{style}><img src="{r}assets/img/{src}" alt="{e(alt)}" loading="lazy"></div>'


def header(r):
    return f"""<header class="top"><div class="wrap">
<a class="logo" href="{r}" aria-label="{BRAND} home"><img src="{r}assets/smartech-plumbing-logo.png" alt="{BRAND}" width="226" height="70"></a>
<button class="menu-btn" aria-label="Menu" aria-expanded="false">&#9776;</button>
<nav class="nav"><a href="{r}#water-heaters">Water Heaters</a><a href="{r}#services">Services</a><a href="{r}#faq">FAQ</a>
<a class="btn" href="tel:{PHONE['tel']}">Call {PHONE['disp']}</a></nav>
</div></header>"""


def footer(r):
    svc = "".join(f'<li><a href="{r}#svc-{s[0]}">{s[2]}</a></li>' for s in SERVICES)
    return f"""<footer><div class="wrap"><div class="grid">
<div><a class="logo" href="{r}"><img src="{r}assets/smartech-plumbing-logo-white.png" alt="{BRAND}"></a>
<p>Residential plumbing you can count on. Water heaters, leaks, drains, toilets and faucets.</p></div>
<div><h4>Services</h4><ul>{svc}</ul></div>
<div><h4>Company</h4><ul><li><a href="{FB_PAGE}" target="_blank" rel="noopener">Facebook</a></li><li><a href="{r}privacy.html">Privacy Policy</a></li></ul>
<h4 style="margin-top:18px">Hours</h4><p>{HOURS}</p></div>
<div><h4>Call us</h4><ul><li><a href="tel:{PHONE['tel']}"><b>{PHONE['disp']}</b></a></li>
<li style="margin-top:10px"><a href="{MESSENGER}" target="_blank" rel="noopener">Message us on Facebook</a></li></ul></div>
</div><div class="bottom"><span>&copy; {date.today().year} {BRAND}. All rights reserved.</span><span><a href="{r}privacy.html">Privacy Policy</a></span></div></div></footer>
<div class="callbar"><a href="tel:{PHONE['tel']}"><small>Call now</small>{PHONE['disp']}</a>
<a class="blue" href="{MESSENGER}" target="_blank" rel="noopener"><small>Prefer to text?</small>Message us</a></div>
<script src="{r}assets/site.js" defer></script>"""


def business_schema():
    return {
        "@context": "https://schema.org", "@type": "Plumber", "name": BRAND, "url": SITE_URL + "/",
        "logo": SITE_URL + "/assets/smartech-plumbing-logo.png", "image": SITE_URL + "/assets/img/water-heater-tech.jpg",
        "telephone": PHONE["tel"], "priceRange": "$$", "sameAs": [FB_PAGE],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                       "dayOfWeek": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"],
                                       "opens": "07:00", "closes": "21:00"}],
        "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": html.unescape(s[2])}} for s in SERVICES],
    }


SITEMAP = []


def write(path, title, desc, body, depth=0, noindex=False, schema=None, priority="0.7"):
    r = ("../" * depth or "./") if path != "404.html" else "/smartech-plumbing/"
    url = SITE_URL + "/" + (path[:-len("index.html")] if path.endswith("index.html") else path)
    schemas = [business_schema()] + ([schema] if schema else [])
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    doc = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">{'<meta name="robots" content="noindex">' if noindex else ''}
<meta property="og:type" content="website"><meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE_URL}/assets/facebook-profile-1080.png">
<meta name="theme-color" content="#0B1F3A">
<link rel="icon" href="{r}assets/smartech-plumbing-icon.png"><link rel="apple-touch-icon" href="{r}assets/smartech-plumbing-icon.png">
<link rel="stylesheet" href="{r}assets/site.css">{ld}
</head><body>
{header(r)}
<main>{body}</main>
{footer(r)}
</body></html>
"""
    f = OUT / path
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(doc, encoding="utf-8")
    if not noindex:
        SITEMAP.append((url, priority))


def build_home():
    r = ""
    cards = "".join(f'<div class="card" id="svc-{s[0]}" style="padding:0;overflow:hidden;scroll-margin-top:90px">'
                    f'<img src="{r}assets/img/{s[4]}" alt="{e(html.unescape(s[2]))}" loading="lazy" style="width:100%;aspect-ratio:16/10;object-fit:cover">'
                    f'<div style="padding:22px 24px 24px"><h3>{s[2]}</h3><p>{e(s[3])}</p>'
                    f'<a class="more" href="tel:{PHONE["tel"]}" style="text-decoration:none">Call {PHONE["disp"]} &rarr;</a></div></div>'
                    for s in SERVICES)
    signs = "".join(f"<li>{e(x)}</li>" for x in WH_SIGNS)
    body = f"""<section class="hero" style="background-image:url(assets/img/hero-kitchen.jpg)"><div class="wrap">
<span class="pill">SAME-DAY SERVICE</span>
<h1>Plumbing <span>Done Right.</span></h1>
<p class="lead">Water heaters, leaks, drains, toilets and faucets, fixed fast by experienced plumbers. You get the price before any work starts.</p>
<div class="calls">{call_btn()}{msg_btn()}</div>
<ul class="checks"><li>Same-day service often available</li><li>Upfront pricing</li><li>Tank &amp; tankless water heaters</li></ul>
</div></section>
<section id="water-heaters" style="scroll-margin-top:80px"><div class="wrap split">
<div><span class="pill">&#128293; WATER HEATER SPECIALISTS</span><h2>No hot water? We'll fix it fast.</h2>
<p class="lead" style="font-size:19px">We repair and replace tank and tankless water heaters, gas and electric. Most jobs are done in a single visit.</p>
<h3>Signs your water heater needs attention</h3><ul class="tick">{signs}</ul>
<div class="warn"><b>Leaking tank?</b> Turn off the cold water valve on top of the heater and shut off the power or gas, then call us.</div>
<div class="calls" style="margin:18px 0 0">{call_btn()}{msg_btn()}</div></div>
{photo(r, "water-heater-tech.jpg", "Plumber servicing a water heater", ratio="3/4")}</div></section>
<section class="alt" id="services" style="scroll-margin-top:80px"><div class="wrap"><div class="section-head"><h2>Plumbing Services</h2>
<p class="muted">From a dripping faucet to a brand-new water heater, we handle it.</p></div><div class="cards">{cards}</div></div></section>
<section class="dark"><div class="wrap"><div class="section-head"><h2>How it works</h2><p class="muted">Getting it fixed is easy.</p></div>
<div class="steps"><div class="step"><h3>Call or message us</h3><p class="muted">Tell us what's going on. It takes a minute.</p></div>
<div class="step"><h3>We come to you</h3><p class="muted">A plumber arrives, finds the problem and gives you the price first.</p></div>
<div class="step"><h3>Fixed and tested</h3><p class="muted">We do the work, test everything and clean up before we leave.</p></div></div></div></section>
<section id="faq" style="scroll-margin-top:80px"><div class="wrap"><div class="section-head"><h2>Frequently Asked Questions</h2></div>{faq_block(FAQ)}</div></section>
<div class="cta"><div class="wrap"><div><h2>Plumbing problem? We'll fix it fast.</h2>
<p class="muted" style="margin:6px 0 0;color:#C9D5E5">Open {HOURS}.</p></div>
<div class="calls" style="margin:0">{call_btn()}{msg_btn()}</div></div></div>"""
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage",
                  "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    write("index.html", f"{BRAND} | Water Heater Repair & Residential Plumbing",
          "Water heater repair and replacement, leaks, drains, toilets and faucets. Same-day service often available. Upfront pricing. Call Smartech Plumbing.",
          body, schema=faq_schema, priority="1.0")


def build_privacy():
    today = date.today().strftime("%B %d, %Y")
    body = f"""<section class="hero page-hero" style="background-image:url(assets/img/bathroom.jpg)"><div class="wrap"><h1>Privacy <span>Policy</span></h1>
<p class="lead">Last updated {today}</p></div></section>
<section><div class="wrap" style="max-width:820px">
<p>This policy explains how {BRAND} ("we", "us") collects and uses information when you visit this website, call us, message us, or submit a request through a form, including Facebook and Instagram lead forms.</p>
<h2>Information we collect</h2>
<ul class="tick"><li>Contact details you give us, such as your name, phone number, email, address and ZIP code</li>
<li>Details about the service you need</li><li>Call recordings and messages, when you call or text us (calls may be recorded for quality assurance)</li>
<li>Basic technical data, such as browser type and pages visited</li></ul>
<h2>How we use it</h2>
<ul class="tick"><li>To contact you about your request, schedule service and provide quotes</li>
<li>To call or text you about your request. Message and data rates may apply. You can reply STOP to opt out of texts at any time.</li>
<li>To improve our service and advertising</li></ul>
<h2>Sharing</h2>
<p>We do not sell your personal information. We share it only with service providers who help us run our business (for example phone, messaging and scheduling tools), with the technician assigned to your job, or when required by law.</p>
<h2>Advertising and cookies</h2>
<p>We advertise on Facebook and Instagram. Meta may use cookies and similar technologies to measure and improve our ads. You can manage your ad preferences in your Meta account settings.</p>
<h2>Data retention and your choices</h2>
<p>We keep your information only as long as needed to serve you and meet legal requirements. To access, correct or delete your information, call us at <a href="tel:{PHONE['tel']}">{PHONE['disp']}</a> or <a href="{MESSENGER}">message us on Facebook</a>.</p>
<h2>Changes</h2><p>We may update this policy from time to time. The date at the top shows the latest version.</p>
</div></section>"""
    write("privacy.html", f"Privacy Policy | {BRAND}", f"How {BRAND} collects, uses and protects your information.", body, priority="0.3")


def build_404():
    body = f"""<section class="hero page-hero" style="background-image:url(/smartech-plumbing/assets/img/bathroom.jpg)"><div class="wrap">
<h1>Page not <span>found</span></h1><p class="lead">That page doesn't exist, but we can still help with your plumbing.</p>
<div class="calls">{call_btn()}<a class="btn blue" href="/smartech-plumbing/"><small>Go to</small><b>Home page</b></a></div></div></section>"""
    write("404.html", f"Page Not Found | {BRAND}", "Page not found.", body, noindex=True)


def build_meta_files():
    urls = "".join(f"<url><loc>{u}</loc><lastmod>{date.today().isoformat()}</lastmod><priority>{p}</priority></url>" for u, p in SITEMAP)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n', encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    build_home()
    build_privacy()
    build_404()
    build_meta_files()
    print("built", len(SITEMAP), "indexed pages")
