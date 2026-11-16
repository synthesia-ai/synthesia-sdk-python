# Ours, kept from regeneration by .fernignore: a client built without base_url or environment sends
# requests to Synthesia's public API and nowhere else. If the spec's `servers` or our overrides change the generated
# default, this fails on the regeneration PR.
import typing

import httpx

from synthesia_ai import AsyncSynthesia, Synthesia

BASE_URL = "https://developers.synthesia.io"


def _handler(urls: typing.List[str]) -> typing.Callable[[httpx.Request], httpx.Response]:
    def handle(request: httpx.Request) -> httpx.Response:
        urls.append(str(request.url))
        return httpx.Response(200, json={"data": [], "nextCursor": None})

    return handle


def test_default_base_url() -> None:
    urls: typing.List[str] = []
    client = Synthesia(api_key="test", httpx_client=httpx.Client(transport=httpx.MockTransport(_handler(urls))))

    client.localizations.list_languages()
    assert urls == [f"{BASE_URL}/api/localizations/languages"]


async def test_async_default_base_url() -> None:
    urls: typing.List[str] = []
    client = AsyncSynthesia(
        api_key="test", httpx_client=httpx.AsyncClient(transport=httpx.MockTransport(_handler(urls)))
    )

    await client.localizations.list_languages()
    assert urls == [f"{BASE_URL}/api/localizations/languages"]
