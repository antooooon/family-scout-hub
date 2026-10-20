from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from app.web import api as api_module


@pytest.mark.asyncio
async def test_lifespan_startup(monkeypatch):

    db_init_mock = AsyncMock()
    start_mock = AsyncMock()
    disconnect_mock = AsyncMock()
    register_handlers_mock = AsyncMock()

    fake_client = SimpleNamespace(
        start=start_mock,
        disconnect=disconnect_mock
    )

    monkeypatch.setattr(api_module, "db_init", db_init_mock)
    monkeypatch.setattr(api_module, "client", fake_client)
    monkeypatch.setattr(api_module, "register_handlers", register_handlers_mock)

    async with api_module.app.router.lifespan_context(api_module.app):
        db_init_mock.assert_awaited_once()
        start_mock.assert_awaited_once()
        register_handlers_mock.assert_awaited_once()

    disconnect_mock.assert_awaited_once()
