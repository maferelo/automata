import pytest
import requests


def get_my_ip():
    response = requests.get("http://ipinfo.io/json")
    return response.json()["ip"]


def test_get_my_ip(monkeypatch):
    my_ip = "123.123.123.123"

    class MockResponse:
        def __init__(self, json_body):
            self.json_body = json_body

        def json(self):
            return self.json_body

    monkeypatch.setattr(
        requests, "get", lambda *args, **kwargs: MockResponse({"ip": my_ip})
    )

    assert get_my_ip() == my_ip
