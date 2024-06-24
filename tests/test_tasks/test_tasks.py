from httpx import AsyncClient


async def test_create_task(ac: AsyncClient):
    response = await ac.post("/v1/tasks/", json={"title": "First Task"})
    assert response.status_code == 200, response.json()
