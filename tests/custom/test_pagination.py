# Ours, kept from regeneration by .fernignore: next_page() on the last page returns None instead of
# fetching the first page again. Keep it after Fern's fix lands, as a regression test for their version.
import typing

import httpx

from synthesia_ai import AsyncSynthesia, Synthesia

PAGES = {
    None: {"data": [{"language": "en-US", "name": "English", "supports": ["dubbing_source"]}], "nextCursor": "p2"},
    "p2": {"data": [{"language": "de-DE", "name": "German", "supports": ["dubbing_target"]}], "nextCursor": None},
}


def _handler(cursors: typing.List[typing.Optional[str]]) -> typing.Callable[[httpx.Request], httpx.Response]:
    def handle(request: httpx.Request) -> httpx.Response:
        cursor = request.url.params.get("cursor")
        cursors.append(cursor)
        return httpx.Response(200, json=PAGES[cursor])

    return handle


def test_next_page_stops_on_the_last_page() -> None:
    cursors: typing.List[typing.Optional[str]] = []
    client = Synthesia(api_key="test", httpx_client=httpx.Client(transport=httpx.MockTransport(_handler(cursors))))

    first = client.localizations.list_languages()
    last = first.next_page()
    assert last is not None and [item.language for item in last.items or []] == ["de-DE"]
    assert last.next_page() is None
    assert cursors == [None, "p2"]


def test_iteration_reads_every_page_once() -> None:
    cursors: typing.List[typing.Optional[str]] = []
    client = Synthesia(api_key="test", httpx_client=httpx.Client(transport=httpx.MockTransport(_handler(cursors))))

    assert [item.language for item in client.localizations.list_languages()] == ["en-US", "de-DE"]
    assert cursors == [None, "p2"]


async def test_async_next_page_stops_on_the_last_page() -> None:
    cursors: typing.List[typing.Optional[str]] = []
    client = AsyncSynthesia(
        api_key="test", httpx_client=httpx.AsyncClient(transport=httpx.MockTransport(_handler(cursors)))
    )

    first = await client.localizations.list_languages()
    last = await first.next_page()
    assert last is not None and [item.language for item in last.items or []] == ["de-DE"]
    assert await last.next_page() is None
    assert cursors == [None, "p2"]
