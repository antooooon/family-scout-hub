from app.telegram import client as client_module


def test_create_telegram_client(monkeypatch):
    constructor_calls = {}

    def fake_telegram_client(**kwargs):
        constructor_calls.update(kwargs)
        return "fake client"

    monkeypatch.setattr(
        client_module,
        "TelegramClient",
        fake_telegram_client
    )

    result = client_module.create_telegram_client()

    assert result == "fake client"

    assert constructor_calls["session"] == "telegram_monitor"
    assert constructor_calls["api_id"] == client_module.settings.telegram_api_id
    assert constructor_calls["api_hash"] == client_module.settings.telegram_api_hash
    assert constructor_calls["connection_retries"] == 10
    assert constructor_calls["retry_delay"] == 5
    assert constructor_calls["auto_reconnect"] is True
    assert constructor_calls["timeout"] == 10


# client_module.settings - setting импортировано в пространсво имен модуля, т.е. дотупно
# settings — не атрибут TelegramClient, а переменная самого модуля client.py.

# monkeypatch говорит:
#  найти в модуле client_module перемменную по имени "TelegramClient"
# и замени ее на fake_telegram_client