from collections.abc import Iterable

import pytest
import requests
from faker import Faker

from ..testlib.client import Client

fake = Faker("ru_RU")

default_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Penetrator/9000",
}

host = "127.0.0.1"


@pytest.fixture(scope="session")
def client_session() -> Iterable[Client]:
    with requests.Session() as session:
        session.headers.update(default_headers)
        yield Client(host=f"http://{host}:8000", session=session)
