# FastAPI + Datastar Starter

A minimal server-driven reactive web app using FastAPI, Jinja2 templates, Datastar, plain CSS, and Server-Sent Events.

The app is intentionally small so it can grow into a TokenTally-style tracker, a ThreatStream-lite feed, or a homelab dashboard without adding a frontend build step.

## What is included

- FastAPI app served by Uvicorn
- Jinja2 base and index templates
- Datastar loaded from the CDN
- Local Datastar signals for a counter and text input
- A server-powered button that returns patchable HTML
- An SSE endpoint that streams `datastar-patch-elements` events
- Plain CSS dashboard layout

## Project structure

```text
app/
  main.py
  templates/
    base.html
    index.html
  static/
    style.css
pyproject.toml
README.md
```

## Setup

Install dependencies with uv:

```bash
uv sync
```

Run the development server:

```bash
uv run uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 in your browser.

## Try the Datastar pieces

1. Use the counter buttons to update a browser-side signal.
2. Type into the message input to update a bound signal.
3. Click **Call server** to fetch HTML from FastAPI and patch it into the page.
4. Click **Start stream** to open an SSE response that streams Datastar patch events into the live status card.

## Tests

```bash
uv run pytest
```
