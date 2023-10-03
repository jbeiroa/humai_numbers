import pytest


@pytest.mark.asyncio
async def test_get_example(client) -> None:
    headers = {
        "Content-Type": "application/json",
    }
    response = await client.get("/example", headers=headers)
    assert response.status_code == 200