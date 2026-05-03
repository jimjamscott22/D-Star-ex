from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home_page_renders_datastar_dashboard():
    response = client.get("/")

    assert response.status_code == 200
    assert "FastAPI + Datastar Starter" in response.text
    assert "data-signals:counter" in response.text
    assert "data-bind:message" in response.text
    assert "https://cdn.jsdelivr.net/gh/starfederation/datastar" in response.text


def test_server_action_returns_patchable_html():
    response = client.get("/server-action")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert 'id="server-result"' in response.text
    assert "FastAPI rendered this update" in response.text


def test_live_status_streams_datastar_patch_events():
    with client.stream("GET", "/live-status") as response:
        body = response.read().decode()

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/event-stream")
    assert "event: datastar-patch-elements" in body
    assert "data: selector #live-status" in body
    assert "data: mode outer" in body
    assert 'id="live-status"' in body
