Create a FastAPI + Datastar starter repo.

Goal:
Build a minimal server-driven reactive web app using FastAPI, Jinja2 templates, and Datastar.

Use:
- FastAPI
- Uvicorn
- Jinja2
- Datastar via CDN
- plain CSS
- Server-Sent Events for live UI updates

Project structure:
app/
  main.py
  templates/
    base.html
    index.html
  static/
    style.css
requirements.txt
README.md

Features:
1. Home page with a small dashboard layout.
2. A counter using Datastar signals.
3. A text input bound to a signal.
4. A server-powered button that calls a FastAPI endpoint.
5. An SSE endpoint that streams Datastar patch-elements events to update a live status card.
6. Clean README with setup commands.

Important:
- Keep the app simple and beginner-friendly.
- Do not use React, Vue, or frontend build tools.
- Comment the code where Datastar is doing something important.
- Make it easy to expand into TokenTally, ThreatStream-lite, or a homelab dashboard.
