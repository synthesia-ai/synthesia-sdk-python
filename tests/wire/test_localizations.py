import pytest
from .conftest import get_client, verify_request_count

from synthesia_ai import (
    BadRequestError,
    ContentTooLargeError,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    NotFoundError,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
    UnsupportedMediaTypeError,
)
from synthesia_ai.core.jsonable_encoder import jsonable_encoder


def test_localizations_list_languages() -> None:
    """Test listLanguages endpoint with WireMock"""
    test_id = "localizations.list_languages.0"
    client = get_client(test_id)
    client.localizations.list_languages()
    verify_request_count(test_id, "GET", "/api/localizations/languages", None, 1)


def test_localizations_list_languages_throws_bad_request_error() -> None:
    """Test listLanguages endpoint error response (BadRequestError) with WireMock"""
    test_id = "localizations.list_languages.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.localizations.list_languages()
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/languages", None, 1)


def test_localizations_list_languages_throws_unauthorized_error() -> None:
    """Test listLanguages endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "localizations.list_languages.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.localizations.list_languages()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/languages", None, 1)


def test_localizations_list_languages_throws_forbidden_error() -> None:
    """Test listLanguages endpoint error response (ForbiddenError) with WireMock"""
    test_id = "localizations.list_languages.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.localizations.list_languages()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/languages", None, 1)


def test_localizations_list_languages_throws_too_many_requests_error() -> None:
    """Test listLanguages endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "localizations.list_languages.4"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.localizations.list_languages()
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/languages", None, 1)


def test_localizations_list_languages_throws_internal_server_error() -> None:
    """Test listLanguages endpoint error response (InternalServerError) with WireMock"""
    test_id = "localizations.list_languages.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.localizations.list_languages()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/languages", None, 1)


def test_localizations_list_languages_throws_service_unavailable_error() -> None:
    """Test listLanguages endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "localizations.list_languages.6"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.localizations.list_languages()
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/languages", None, 1)


def test_localizations_list_languages_throws_gateway_timeout_error() -> None:
    """Test listLanguages endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "localizations.list_languages.7"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.localizations.list_languages()
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/languages", None, 1)


def test_localizations_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "localizations.get.0"
    client = get_client(test_id)
    client.localizations.get(
        localization_id="localization_id",
    )
    verify_request_count(test_id, "GET", "/api/localizations/localization_id", None, 1)


def test_localizations_get_throws_bad_request_error() -> None:
    """Test get endpoint error response (BadRequestError) with WireMock"""
    test_id = "localizations.get.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.localizations.get(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id", None, 1)


def test_localizations_get_throws_unauthorized_error() -> None:
    """Test get endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "localizations.get.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.localizations.get(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id", None, 1)


def test_localizations_get_throws_forbidden_error() -> None:
    """Test get endpoint error response (ForbiddenError) with WireMock"""
    test_id = "localizations.get.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.localizations.get(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id", None, 1)


def test_localizations_get_throws_not_found_error() -> None:
    """Test get endpoint error response (NotFoundError) with WireMock"""
    test_id = "localizations.get.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.localizations.get(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id", None, 1)


def test_localizations_get_throws_too_many_requests_error() -> None:
    """Test get endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "localizations.get.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.localizations.get(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id", None, 1)


def test_localizations_get_throws_internal_server_error() -> None:
    """Test get endpoint error response (InternalServerError) with WireMock"""
    test_id = "localizations.get.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.localizations.get(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id", None, 1)


def test_localizations_get_throws_service_unavailable_error() -> None:
    """Test get endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "localizations.get.7"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.localizations.get(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id", None, 1)


def test_localizations_get_throws_gateway_timeout_error() -> None:
    """Test get endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "localizations.get.8"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.localizations.get(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id", None, 1)


def test_localizations_create_from_media_url() -> None:
    """Test createFromMediaUrl endpoint with WireMock"""
    test_id = "localizations.create_from_media_url.0"
    client = get_client(test_id)
    client.localizations.create_from_media_url(
        lipsync_enabled=True,
        burned_in_captions_enabled=False,
        media_url="https://my-bucket.s3.amazonaws.com/onboarding.mp4?X-Amz-Signature=...",
        title="Product onboarding",
        source_language="en-US",
        target_languages=["es-ES", "fr-FR"],
    )
    verify_request_count(test_id, "POST", "/api/localizations/from-media-url", None, 1)


def test_localizations_create_from_media_url_throws_bad_request_error() -> None:
    """Test createFromMediaUrl endpoint error response (BadRequestError) with WireMock"""
    test_id = "localizations.create_from_media_url.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.localizations.create_from_media_url(
            media_url="x",
            title="x",
            source_language="x",
            target_languages=["targetLanguages", "targetLanguages"],
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/localizations/from-media-url", None, 1)


def test_localizations_create_from_media_url_throws_unauthorized_error() -> None:
    """Test createFromMediaUrl endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "localizations.create_from_media_url.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.localizations.create_from_media_url(
            media_url="x",
            title="x",
            source_language="x",
            target_languages=["targetLanguages", "targetLanguages"],
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/localizations/from-media-url", None, 1)


def test_localizations_create_from_media_url_throws_forbidden_error() -> None:
    """Test createFromMediaUrl endpoint error response (ForbiddenError) with WireMock"""
    test_id = "localizations.create_from_media_url.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.localizations.create_from_media_url(
            media_url="x",
            title="x",
            source_language="x",
            target_languages=["targetLanguages", "targetLanguages"],
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/localizations/from-media-url", None, 1)


def test_localizations_create_from_media_url_throws_content_too_large_error() -> None:
    """Test createFromMediaUrl endpoint error response (ContentTooLargeError) with WireMock"""
    test_id = "localizations.create_from_media_url.4"
    client = get_client(test_id)
    with pytest.raises(ContentTooLargeError) as exc_info:
        client.localizations.create_from_media_url(
            media_url="x",
            title="x",
            source_language="x",
            target_languages=["targetLanguages", "targetLanguages"],
        )
    assert exc_info.value.status_code == 413
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/localizations/from-media-url", None, 1)


def test_localizations_create_from_media_url_throws_unsupported_media_type_error() -> None:
    """Test createFromMediaUrl endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "localizations.create_from_media_url.5"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.localizations.create_from_media_url(
            media_url="x",
            title="x",
            source_language="x",
            target_languages=["targetLanguages", "targetLanguages"],
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/localizations/from-media-url", None, 1)


def test_localizations_create_from_media_url_throws_too_many_requests_error() -> None:
    """Test createFromMediaUrl endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "localizations.create_from_media_url.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.localizations.create_from_media_url(
            media_url="x",
            title="x",
            source_language="x",
            target_languages=["targetLanguages", "targetLanguages"],
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/localizations/from-media-url", None, 1)


def test_localizations_create_from_media_url_throws_internal_server_error() -> None:
    """Test createFromMediaUrl endpoint error response (InternalServerError) with WireMock"""
    test_id = "localizations.create_from_media_url.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.localizations.create_from_media_url(
            media_url="x",
            title="x",
            source_language="x",
            target_languages=["targetLanguages", "targetLanguages"],
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/localizations/from-media-url", None, 1)


def test_localizations_create_from_media_url_throws_service_unavailable_error() -> None:
    """Test createFromMediaUrl endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "localizations.create_from_media_url.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.localizations.create_from_media_url(
            media_url="x",
            title="x",
            source_language="x",
            target_languages=["targetLanguages", "targetLanguages"],
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/localizations/from-media-url", None, 1)


def test_localizations_create_from_media_url_throws_gateway_timeout_error() -> None:
    """Test createFromMediaUrl endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "localizations.create_from_media_url.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.localizations.create_from_media_url(
            media_url="x",
            title="x",
            source_language="x",
            target_languages=["targetLanguages", "targetLanguages"],
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/localizations/from-media-url", None, 1)
