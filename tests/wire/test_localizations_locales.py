import pytest
from .conftest import get_client, verify_request_count

from synthesia_ai import (
    BadRequestError,
    ConflictError,
    ContentTooLargeError,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    NewLocale,
    NotFoundError,
    PaymentRequiredError,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
    UnsupportedMediaTypeError,
)
from synthesia_ai.core.jsonable_encoder import jsonable_encoder


def test_localizations_locales_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "localizations.locales.list_.0"
    client = get_client(test_id)
    client.localizations.locales.list(
        localization_id="localization_id",
    )
    verify_request_count(test_id, "GET", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_list__throws_bad_request_error() -> None:
    """Test list endpoint error response (BadRequestError) with WireMock"""
    test_id = "localizations.locales.list_.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.localizations.locales.list(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "localizations.locales.list_.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.localizations.locales.list(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_list__throws_forbidden_error() -> None:
    """Test list endpoint error response (ForbiddenError) with WireMock"""
    test_id = "localizations.locales.list_.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.localizations.locales.list(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_list__throws_not_found_error() -> None:
    """Test list endpoint error response (NotFoundError) with WireMock"""
    test_id = "localizations.locales.list_.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.localizations.locales.list(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_list__throws_too_many_requests_error() -> None:
    """Test list endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "localizations.locales.list_.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.localizations.locales.list(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "localizations.locales.list_.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.localizations.locales.list(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_list__throws_service_unavailable_error() -> None:
    """Test list endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "localizations.locales.list_.7"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.localizations.locales.list(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_list__throws_gateway_timeout_error() -> None:
    """Test list endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "localizations.locales.list_.8"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.localizations.locales.list(
            localization_id="localization_id",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_add() -> None:
    """Test add endpoint with WireMock"""
    test_id = "localizations.locales.add.0"
    client = get_client(test_id)
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
    verify_request_count(test_id, "PUT", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_add_throws_bad_request_error() -> None:
    """Test add endpoint error response (BadRequestError) with WireMock"""
    test_id = "localizations.locales.add.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.localizations.locales.add(
            localization_id="localization_id",
            locales=[
                NewLocale(
                    language="language",
                ),
                NewLocale(
                    language="language",
                ),
            ],
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "PUT", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_add_throws_unauthorized_error() -> None:
    """Test add endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "localizations.locales.add.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.localizations.locales.add(
            localization_id="localization_id",
            locales=[
                NewLocale(
                    language="language",
                ),
                NewLocale(
                    language="language",
                ),
            ],
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "PUT", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_add_throws_payment_required_error() -> None:
    """Test add endpoint error response (PaymentRequiredError) with WireMock"""
    test_id = "localizations.locales.add.3"
    client = get_client(test_id)
    with pytest.raises(PaymentRequiredError) as exc_info:
        client.localizations.locales.add(
            localization_id="localization_id",
            locales=[
                NewLocale(
                    language="language",
                ),
                NewLocale(
                    language="language",
                ),
            ],
        )
    assert exc_info.value.status_code == 402
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "PUT", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_add_throws_forbidden_error() -> None:
    """Test add endpoint error response (ForbiddenError) with WireMock"""
    test_id = "localizations.locales.add.4"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.localizations.locales.add(
            localization_id="localization_id",
            locales=[
                NewLocale(
                    language="language",
                ),
                NewLocale(
                    language="language",
                ),
            ],
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "PUT", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_add_throws_not_found_error() -> None:
    """Test add endpoint error response (NotFoundError) with WireMock"""
    test_id = "localizations.locales.add.5"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.localizations.locales.add(
            localization_id="localization_id",
            locales=[
                NewLocale(
                    language="language",
                ),
                NewLocale(
                    language="language",
                ),
            ],
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "PUT", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_add_throws_conflict_error() -> None:
    """Test add endpoint error response (ConflictError) with WireMock"""
    test_id = "localizations.locales.add.6"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.localizations.locales.add(
            localization_id="localization_id",
            locales=[
                NewLocale(
                    language="language",
                ),
                NewLocale(
                    language="language",
                ),
            ],
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "PUT", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_add_throws_content_too_large_error() -> None:
    """Test add endpoint error response (ContentTooLargeError) with WireMock"""
    test_id = "localizations.locales.add.7"
    client = get_client(test_id)
    with pytest.raises(ContentTooLargeError) as exc_info:
        client.localizations.locales.add(
            localization_id="localization_id",
            locales=[
                NewLocale(
                    language="language",
                ),
                NewLocale(
                    language="language",
                ),
            ],
        )
    assert exc_info.value.status_code == 413
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "PUT", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_add_throws_unsupported_media_type_error() -> None:
    """Test add endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "localizations.locales.add.8"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.localizations.locales.add(
            localization_id="localization_id",
            locales=[
                NewLocale(
                    language="language",
                ),
                NewLocale(
                    language="language",
                ),
            ],
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "PUT", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_add_throws_too_many_requests_error() -> None:
    """Test add endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "localizations.locales.add.9"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.localizations.locales.add(
            localization_id="localization_id",
            locales=[
                NewLocale(
                    language="language",
                ),
                NewLocale(
                    language="language",
                ),
            ],
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "PUT", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_add_throws_internal_server_error() -> None:
    """Test add endpoint error response (InternalServerError) with WireMock"""
    test_id = "localizations.locales.add.10"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.localizations.locales.add(
            localization_id="localization_id",
            locales=[
                NewLocale(
                    language="language",
                ),
                NewLocale(
                    language="language",
                ),
            ],
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "PUT", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_add_throws_service_unavailable_error() -> None:
    """Test add endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "localizations.locales.add.11"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.localizations.locales.add(
            localization_id="localization_id",
            locales=[
                NewLocale(
                    language="language",
                ),
                NewLocale(
                    language="language",
                ),
            ],
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "PUT", "/api/localizations/localization_id/locales", None, 1)


def test_localizations_locales_add_throws_gateway_timeout_error() -> None:
    """Test add endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "localizations.locales.add.12"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.localizations.locales.add(
            localization_id="localization_id",
            locales=[
                NewLocale(
                    language="language",
                ),
                NewLocale(
                    language="language",
                ),
            ],
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "PUT", "/api/localizations/localization_id/locales", None, 1)
