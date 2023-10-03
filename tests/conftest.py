import httpx
import pytest
import pytest_asyncio

from app.core.main import app
from asgi_lifespan import LifespanManager
import asyncio



@pytest.fixture(scope="session")
def event_loop():
    """
    will ensure that we always work with the same event loop instance. It's automatically requested
    by pytest-asyncio before executing asynchronous tests.
    """
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def client():
    """
    will create an instance of HTTPX for our FastAPI application.
    We must also remember to trigger the app events with asgi-lifespan
    """
    async with LifespanManager(app):
        async with httpx.AsyncClient(app=app, base_url="http://testserver") as test_client:
            yield test_client
