from __future__ import annotations

import asyncio
from datetime import datetime
from html import escape

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(title="FastAPI + Datastar Starter")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


def render_datastar_patch(html: str, selector: str | None = None, mode: str = "outer") -> str:
    """Format a Datastar patch-elements event for an SSE response."""
    lines = ["event: datastar-patch-elements"]
    if selector:
        lines.append(f"data: selector {selector}")
    lines.append(f"data: mode {mode}")

    for line in html.splitlines():
        lines.append(f"data: elements {line}")

    return "\n".join(lines) + "\n\n"


def live_status_card(step: int) -> str:
    now = datetime.now().strftime("%H:%M:%S")
    states = [
        ("Ready", "Waiting for the next server event.", "idle"),
        ("Syncing", "FastAPI is streaming a Datastar patch.", "active"),
        ("Updated", "The live status card was replaced from SSE.", "success"),
    ]
    label, detail, tone = states[step % len(states)]

    return f"""
<article id="live-status" class="status-card status-card--{tone}">
  <div>
    <p class="eyebrow">Live status</p>
    <h2>{label}</h2>
    <p>{detail}</p>
  </div>
  <time datetime="{datetime.now().isoformat(timespec='seconds')}">{now}</time>
</article>
""".strip()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "index.html")


@app.get("/server-action", response_class=HTMLResponse)
async def server_action(message: str = "Datastar") -> HTMLResponse:
    safe_message = escape(message.strip() or "Datastar")
    timestamp = datetime.now().strftime("%H:%M:%S")

    html = f"""
<div id="server-result" class="server-result">
  <strong>FastAPI rendered this update.</strong>
  <span>{safe_message} checked in at {timestamp}.</span>
</div>
""".strip()
    return HTMLResponse(html)


@app.get("/live-status")
async def live_status() -> StreamingResponse:
    async def event_stream():
        for step in range(3):
            yield render_datastar_patch(live_status_card(step), selector="#live-status")
            await asyncio.sleep(1)

    return StreamingResponse(event_stream(), media_type="text/event-stream")
