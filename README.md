# Synthesia Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fsynthesia-ai%2Fsynthesia-sdk-python)
[![pypi](https://img.shields.io/pypi/v/synthesia-ai)](https://pypi.python.org/pypi/synthesia-ai)

This SDK is under active development and is not yet fully stable. Its interface may change in any release before 1.0. Breaking changes bump the minor version.

## Table of Contents

- [Documentation](#documentation)
- [Installation](#installation)
- [Reference](#reference)
- [Keep Your Api Key on The Server](#keep-your-api-key-on-the-server)
- [Timeouts](#timeouts)
- [Retries](#retries)
- [Verify A Release](#verify-a-release)
- [Support](#support)
- [Usage](#usage)
- [Environments](#environments)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Pagination](#pagination)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Custom Client](#custom-client)

## Documentation

API reference documentation is available [here](https://developers.synthesia.io/docs/introduction).

## Installation

```sh
pip install synthesia-ai
```

## Reference

A full reference for this library is available [here](https://github.com/synthesia-ai/synthesia-sdk-python/blob/HEAD/./reference.md).

## Keep your API key on the server

Use this SDK only in server-side code, and never put your API key in code you ship to users. Load it from an environment variable or a secret manager:

```python
import os

from synthesia_ai import Synthesia

client = Synthesia(api_key=os.environ["SYNTHESIA_API_KEY"])
```


## Timeouts

The SDK defaults to a 90 second timeout. You can configure this with a timeout option at the client or request level.

```python
from synthesia_ai import Synthesia

client = Synthesia(..., timeout=20.0)

# Override timeout for a specific method
client.localizations.get(..., request_options={
    "timeout": 1
})
```


## Retries

The SDK retries a failed request up to 2 times, with exponential backoff, when the response status is 408, 409, 429 or 5XX. It waits as long as a `Retry-After` header asks, up to 60 seconds.

Requests that create something (an interactive avatar, a session or a localization) are never retried, so a timeout can't create a duplicate. Check whether the first request succeeded before you send it again.

Use the `max_retries` option to change the number of retries for other requests:

```python
client.localizations.get(..., request_options={
    "max_retries": 1
})
```

## Verify a release

Every release is published from this repository's release workflow with [PyPI attestations](https://docs.pypi.org/attestations/), which link each file to the commit and workflow run that built it. To check a release, install [pypi-attestations](https://pypi.org/project/pypi-attestations/) and verify the file against this repository, replacing `<version>`:

```sh
pip install pypi-attestations
pypi-attestations verify pypi --repository https://github.com/synthesia-ai/synthesia-sdk-python pypi:synthesia_ai-<version>-py3-none-any.whl
```


## Support

For help with the SDK or the API, see the [API documentation](https://developers.synthesia.io/docs/introduction) or [contact Synthesia Support](https://help.synthesia.io/en/articles/7182166-how-can-i-contact-synthesia). To report a security issue, follow [SECURITY.md](./SECURITY.md).

This SDK is generated from the Synthesia API definition, so we don't accept pull requests to this repository.

## Usage

Instantiate and use the client with the following:

```python
from synthesia_ai import Synthesia

client = Synthesia(
    api_key="<token>",
)

client.localizations.create_from_media_url(
    lipsync_enabled=True,
    burned_in_captions_enabled=False,
    media_url="https://my-bucket.s3.amazonaws.com/onboarding.mp4?X-Amz-Signature=...",
    title="Product onboarding",
    source_language="en-US",
    target_languages=[
        "es-ES",
        "fr-FR"
    ],
)
```

## Environments

This SDK allows you to configure different environments for API requests.

```python
from synthesia_ai import Synthesia
from synthesia_ai.environment import SynthesiaEnvironment

client = Synthesia(
    environment=SynthesiaEnvironment.DEFAULT,
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from synthesia_ai import AsyncSynthesia

client = AsyncSynthesia(
    api_key="<token>",
)


async def main() -> None:
    await client.localizations.create_from_media_url(
        lipsync_enabled=True,
        burned_in_captions_enabled=False,
        media_url="https://my-bucket.s3.amazonaws.com/onboarding.mp4?X-Amz-Signature=...",
        title="Product onboarding",
        source_language="en-US",
        target_languages=[
            "es-ES",
            "fr-FR"
        ],
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from synthesia_ai.core.api_error import ApiError

try:
    client.localizations.create_from_media_url(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from synthesia_ai import Synthesia

client = Synthesia(
    api_key="<token>",
)

client.localizations.list_languages()
```

```python
# You can also iterate through pages and access the typed response per page
pager = client.localizations.list_languages(...)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from synthesia_ai import Synthesia

client = Synthesia(...)
response = client.localizations.with_raw_response.create_from_media_url(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from synthesia_ai import Synthesia

client = Synthesia(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```
