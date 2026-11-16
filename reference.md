# Reference
## billing
<details><summary><code>client.billing.<a href="src/synthesia_ai/billing/client.py">get_credits</a>() -> Credits</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get your workspace's current billing period and its credit balance.

Amounts are decimal strings (e.g. `"288.00"`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synthesia_ai import Synthesia
from synthesia_ai.environment import SynthesiaEnvironment

client = Synthesia(
    api_key="<token>",
    environment=SynthesiaEnvironment.DEFAULT,
)

client.billing.get_credits()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Localizations
<details><summary><code>client.localizations.<a href="src/synthesia_ai/localizations/client.py">list_languages</a>(...) -> PageLanguage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the languages you can localize from and into, with the roles each supports.

**Required scope:** [`localization:read`](https://developers.synthesia.io/docs/scopes) (in Studio: Localization (read))
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synthesia_ai import Synthesia
from synthesia_ai.environment import SynthesiaEnvironment

client = Synthesia(
    api_key="<token>",
    environment=SynthesiaEnvironment.DEFAULT,
)

client.localizations.list_languages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The `nextCursor` of the previous page. Omit for the first page.
    
</dd>
</dl>

<dl>
<dd>

**supports:** `typing.Optional[LanguageRole]` — Only list languages that support this role. Omit to list every language.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.localizations.<a href="src/synthesia_ai/localizations/client.py">get</a>(...) -> Localization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Required scope:** [`localization:read`](https://developers.synthesia.io/docs/scopes) (in Studio: Localization (read))
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synthesia_ai import Synthesia
from synthesia_ai.environment import SynthesiaEnvironment

client = Synthesia(
    api_key="<token>",
    environment=SynthesiaEnvironment.DEFAULT,
)

client.localizations.get(
    localization_id="localization_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**localization_id:** `str` — The localization id, prefixed `l10n_…`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.localizations.<a href="src/synthesia_ai/localizations/client.py">create_from_media_url</a>(...) -> Localization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start localizing a video from a URL.

Poll `GET /localizations/{localization_id}` until `done` is true, then poll its locales until each is done.

**Required scope:** [`localization:write`](https://developers.synthesia.io/docs/scopes) (in Studio: Localization (write))
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synthesia_ai import Synthesia
from synthesia_ai.environment import SynthesiaEnvironment

client = Synthesia(
    api_key="<token>",
    environment=SynthesiaEnvironment.DEFAULT,
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
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**media_url:** `str` — A presigned S3 HTTPS URL for the video to localize, with the bucket in the host (`https://<bucket>.s3.<region>.amazonaws.com/...`). Other URLs are not supported yet.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The title of the localized video.
    
</dd>
</dl>

<dl>
<dd>

**source_language:** `str` — The language spoken in the video, from `GET /localizations/languages?supports=dubbing_source`, or `auto` to detect it.
    
</dd>
</dl>

<dl>
<dd>

**target_languages:** `typing.List[str]` — The languages to localize into, from `GET /localizations/languages?supports=dubbing_target`. Each language once.
    
</dd>
</dl>

<dl>
<dd>

**lipsync_enabled:** `typing.Optional[bool]` — Whether to lip-sync the localized videos. Lip-sync costs extra credit and needs a plan that includes it: without it, adding locales is refused, and a new localization fails once processed.
    
</dd>
</dl>

<dl>
<dd>

**burned_in_captions_enabled:** `typing.Optional[bool]` — Whether to burn captions into the localized videos.
    
</dd>
</dl>

<dl>
<dd>

**video_duration:** `typing.Optional[VideoDuration]` — `adaptive` adjusts the video's speed to fit the translation; `original` keeps the source's duration.
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[Visibility]` — Who can view the localized videos.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InteractiveAvatars Sessions
<details><summary><code>client.interactive_avatars.sessions.<a href="src/synthesia_ai/interactive_avatars/sessions/client.py">create</a>(...) -> Session</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start an interactive avatar session.

- Each running session counts toward your plan's concurrent-session limit until it ends.
- Only sessions started through this API count toward the limit.
- Over the limit, the request fails with `429` and code `concurrency_limit`; its `detail`
  states your plan's limit and how many sessions are running.

| Plan | Concurrent sessions |
| --- | --- |
| Freemium | 1 |
| All paid plans | 100 |

**Required scope:** [`interactive_avatars:write`](https://developers.synthesia.io/docs/scopes) (in Studio: Interactive Avatars (write))
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synthesia_ai import Synthesia
from synthesia_ai.environment import SynthesiaEnvironment

client = Synthesia(
    api_key="<token>",
    environment=SynthesiaEnvironment.DEFAULT,
)

client.interactive_avatars.sessions.create(
    avatar_ids=[
        "av_6c9edb85a2f947e5"
    ],
    livekit_url="wss://your-app.livekit.cloud",
    livekit_token="<your-livekit-token>",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**avatar_ids:** `typing.List[str]` — The interactive avatars to join the session — e.g. the id returned by POST /api/interactive-avatars/avatars once its status is completed.
    
</dd>
</dl>

<dl>
<dd>

**livekit_url:** `str` — The WebSocket URL (wss://…) of your LiveKit room the avatar joins.
    
</dd>
</dl>

<dl>
<dd>

**livekit_token:** `str` — A LiveKit access token you mint for the avatar's participant in that room. Set its lk.publish_on_behalf attribute to your agent's participant identity, exactly (LiveKit server SDKs: AccessToken(...).with_attributes(...)). If you retry a failed request, reuse the same livekitUrl and livekitToken, so give the token a TTL that covers your retries.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InteractiveAvatars Avatars
<details><summary><code>client.interactive_avatars.avatars.<a href="src/synthesia_ai/interactive_avatars/avatars/client.py">create</a>(...) -> InteractiveAvatar</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an interactive avatar from an existing Studio avatar.

- Generation is asynchronous: the request answers `202` with the avatar's current status.
- Poll by repeating the same request (with `regenerate` omitted) until `done` is true — a
  repeat never starts a second generation.
- Each poll re-runs the credit check, so a drained balance answers `402` even while an
  already-dispatched generation continues.
- Once `status` is `completed`, include the returned `id` in the `avatarIds` list of
  `POST /api/interactive-avatars/sessions`.

**Required scope:** [`interactive_avatars:write`](https://developers.synthesia.io/docs/scopes) (in Studio: Interactive Avatars (write))
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synthesia_ai import Synthesia
from synthesia_ai.environment import SynthesiaEnvironment

client = Synthesia(
    api_key="<token>",
    environment=SynthesiaEnvironment.DEFAULT,
)

client.interactive_avatars.avatars.create(
    source_id="av_6c9edb85a2f947e5",
    regenerate=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `str` — The avatar id shown in Studio, with the av_ prefix.
    
</dd>
</dl>

<dl>
<dd>

**regenerate:** `typing.Optional[bool]` — Force a fresh interactive avatar generation instead of returning the existing avatar.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Localizations Locales
<details><summary><code>client.localizations.locales.<a href="src/synthesia_ai/localizations/locales/client.py">list</a>(...) -> PageLocale</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Required scope:** [`localization:read`](https://developers.synthesia.io/docs/scopes) (in Studio: Localization (read))
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synthesia_ai import Synthesia
from synthesia_ai.environment import SynthesiaEnvironment

client = Synthesia(
    api_key="<token>",
    environment=SynthesiaEnvironment.DEFAULT,
)

client.localizations.locales.list(
    localization_id="localization_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**localization_id:** `str` — The localization id, prefixed `l10n_…`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The `nextCursor` of the previous page. Omit for the first page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.localizations.locales.<a href="src/synthesia_ai/localizations/locales/client.py">add</a>(...) -> PageLocale</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a locale for each language, and return the requested locales.

- 202 when new locales were added: poll them until each is done.
- 200 when every language already had a locale.
- A language that already has a locale is skipped, so repeating a request is safe. A failed locale isn't
  redone: create a new localization to retry it.
- Locales are never removed: a language left out keeps its locale.

**Required scope:** [`localization:write`](https://developers.synthesia.io/docs/scopes) (in Studio: Localization (write))
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synthesia_ai import Synthesia, NewLocale
from synthesia_ai.environment import SynthesiaEnvironment

client = Synthesia(
    api_key="<token>",
    environment=SynthesiaEnvironment.DEFAULT,
)

client.localizations.locales.add(
    localization_id="localization_id",
    lipsync_enabled=True,
    burned_in_captions_enabled=False,
    locales=[
        NewLocale(
            language="es-ES",
            generate=True,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**localization_id:** `str` — The localization id, prefixed `l10n_…`.
    
</dd>
</dl>

<dl>
<dd>

**locales:** `typing.List[NewLocale]` — One entry per language. A language that already has a locale is skipped.
    
</dd>
</dl>

<dl>
<dd>

**lipsync_enabled:** `typing.Optional[bool]` — Whether to lip-sync the localized videos. Lip-sync costs extra credit and needs a plan that includes it: without it, adding locales is refused, and a new localization fails once processed.
    
</dd>
</dl>

<dl>
<dd>

**burned_in_captions_enabled:** `typing.Optional[bool]` — Whether to burn captions into the localized videos.
    
</dd>
</dl>

<dl>
<dd>

**video_duration:** `typing.Optional[VideoDuration]` — `adaptive` adjusts the video's speed to fit the translation; `original` keeps the source's duration.
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[Visibility]` — Who can view the localized videos.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

