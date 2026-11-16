import pytest
from .conftest import get_client, verify_request_count

from synthesia_ai import (
    BadRequestError,
    ContentTooLargeError,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    NotFoundError,
    PaymentRequiredError,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
    UnsupportedMediaTypeError,
)
from synthesia_ai.core.jsonable_encoder import jsonable_encoder


def test_interactiveAvatars_avatars_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "interactive_avatars.avatars.create.0"
    client = get_client(test_id)
    client.interactive_avatars.avatars.create(
        source_id="av_6c9edb85a2f947e5",
        regenerate=False,
    )
    verify_request_count(test_id, "POST", "/api/interactive-avatars/avatars", None, 1)


def test_interactiveAvatars_avatars_create_throws_bad_request_error() -> None:
    """Test create endpoint error response (BadRequestError) with WireMock"""
    test_id = "interactive_avatars.avatars.create.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.interactive_avatars.avatars.create(
            source_id="sourceId",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/interactive-avatars/avatars", None, 1)


def test_interactiveAvatars_avatars_create_throws_unauthorized_error() -> None:
    """Test create endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "interactive_avatars.avatars.create.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.interactive_avatars.avatars.create(
            source_id="sourceId",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/interactive-avatars/avatars", None, 1)


def test_interactiveAvatars_avatars_create_throws_payment_required_error() -> None:
    """Test create endpoint error response (PaymentRequiredError) with WireMock"""
    test_id = "interactive_avatars.avatars.create.3"
    client = get_client(test_id)
    with pytest.raises(PaymentRequiredError) as exc_info:
        client.interactive_avatars.avatars.create(
            source_id="sourceId",
        )
    assert exc_info.value.status_code == 402
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/interactive-avatars/avatars", None, 1)


def test_interactiveAvatars_avatars_create_throws_forbidden_error() -> None:
    """Test create endpoint error response (ForbiddenError) with WireMock"""
    test_id = "interactive_avatars.avatars.create.4"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.interactive_avatars.avatars.create(
            source_id="sourceId",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/interactive-avatars/avatars", None, 1)


def test_interactiveAvatars_avatars_create_throws_not_found_error() -> None:
    """Test create endpoint error response (NotFoundError) with WireMock"""
    test_id = "interactive_avatars.avatars.create.5"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.interactive_avatars.avatars.create(
            source_id="sourceId",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/interactive-avatars/avatars", None, 1)


def test_interactiveAvatars_avatars_create_throws_content_too_large_error() -> None:
    """Test create endpoint error response (ContentTooLargeError) with WireMock"""
    test_id = "interactive_avatars.avatars.create.6"
    client = get_client(test_id)
    with pytest.raises(ContentTooLargeError) as exc_info:
        client.interactive_avatars.avatars.create(
            source_id="sourceId",
        )
    assert exc_info.value.status_code == 413
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/interactive-avatars/avatars", None, 1)


def test_interactiveAvatars_avatars_create_throws_unsupported_media_type_error() -> None:
    """Test create endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "interactive_avatars.avatars.create.7"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.interactive_avatars.avatars.create(
            source_id="sourceId",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/interactive-avatars/avatars", None, 1)


def test_interactiveAvatars_avatars_create_throws_too_many_requests_error() -> None:
    """Test create endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "interactive_avatars.avatars.create.8"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.interactive_avatars.avatars.create(
            source_id="sourceId",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/interactive-avatars/avatars", None, 1)


def test_interactiveAvatars_avatars_create_throws_internal_server_error() -> None:
    """Test create endpoint error response (InternalServerError) with WireMock"""
    test_id = "interactive_avatars.avatars.create.9"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.interactive_avatars.avatars.create(
            source_id="sourceId",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/interactive-avatars/avatars", None, 1)


def test_interactiveAvatars_avatars_create_throws_service_unavailable_error() -> None:
    """Test create endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "interactive_avatars.avatars.create.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.interactive_avatars.avatars.create(
            source_id="sourceId",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/interactive-avatars/avatars", None, 1)


def test_interactiveAvatars_avatars_create_throws_gateway_timeout_error() -> None:
    """Test create endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "interactive_avatars.avatars.create.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.interactive_avatars.avatars.create(
            source_id="sourceId",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "POST", "/api/interactive-avatars/avatars", None, 1)
