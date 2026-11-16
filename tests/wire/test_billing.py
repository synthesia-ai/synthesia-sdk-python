import pytest
from .conftest import get_client, verify_request_count

from synthesia_ai import (
    BadRequestError,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    NotFoundError,
    PaymentRequiredError,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
)
from synthesia_ai.core.jsonable_encoder import jsonable_encoder


def test_billing_get_credits() -> None:
    """Test getCredits endpoint with WireMock"""
    test_id = "billing.get_credits.0"
    client = get_client(test_id)
    client.billing.get_credits()
    verify_request_count(test_id, "GET", "/api/billing/credits", None, 1)


def test_billing_get_credits_throws_bad_request_error() -> None:
    """Test getCredits endpoint error response (BadRequestError) with WireMock"""
    test_id = "billing.get_credits.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.billing.get_credits()
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/billing/credits", None, 1)


def test_billing_get_credits_throws_unauthorized_error() -> None:
    """Test getCredits endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "billing.get_credits.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.billing.get_credits()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/billing/credits", None, 1)


def test_billing_get_credits_throws_payment_required_error() -> None:
    """Test getCredits endpoint error response (PaymentRequiredError) with WireMock"""
    test_id = "billing.get_credits.3"
    client = get_client(test_id)
    with pytest.raises(PaymentRequiredError) as exc_info:
        client.billing.get_credits()
    assert exc_info.value.status_code == 402
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/billing/credits", None, 1)


def test_billing_get_credits_throws_forbidden_error() -> None:
    """Test getCredits endpoint error response (ForbiddenError) with WireMock"""
    test_id = "billing.get_credits.4"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.billing.get_credits()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/billing/credits", None, 1)


def test_billing_get_credits_throws_not_found_error() -> None:
    """Test getCredits endpoint error response (NotFoundError) with WireMock"""
    test_id = "billing.get_credits.5"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.billing.get_credits()
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/billing/credits", None, 1)


def test_billing_get_credits_throws_too_many_requests_error() -> None:
    """Test getCredits endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "billing.get_credits.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.billing.get_credits()
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/billing/credits", None, 1)


def test_billing_get_credits_throws_internal_server_error() -> None:
    """Test getCredits endpoint error response (InternalServerError) with WireMock"""
    test_id = "billing.get_credits.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.billing.get_credits()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/billing/credits", None, 1)


def test_billing_get_credits_throws_service_unavailable_error() -> None:
    """Test getCredits endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "billing.get_credits.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.billing.get_credits()
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/billing/credits", None, 1)


def test_billing_get_credits_throws_gateway_timeout_error() -> None:
    """Test getCredits endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "billing.get_credits.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.billing.get_credits()
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"type": "type", "title": "title", "status": 1, "code": "code"}
    verify_request_count(test_id, "GET", "/api/billing/credits", None, 1)
