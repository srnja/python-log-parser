from log_parser.validator import (
    validate_ip,
    validate_timestamp,
    validate_record
)


def test_valid_ip():
    assert validate_ip("192.168.1.1") is True


def test_invalid_ip():
    assert validate_ip("999.999.999.999") is False


def test_valid_timestamp():
    assert validate_timestamp(
        "15/Oct/2025:10:30:45 +0000"
    ) is True


def test_invalid_timestamp():
    assert validate_timestamp("invalid-date") is False


def test_valid_record():

    record = {
        "ip_address": "192.168.1.1",
        "timestamp": "2025-10-15T10:30:45+00:00",
        "method": "GET",
        "endpoint": "/home",
        "status_code": 200,
        "event_details": "GET /home - HTTP 200"
    }

    assert validate_record(record) is True


def test_missing_field():

    record = {
        "ip_address": "192.168.1.1",
        "timestamp": "2025-10-15T10:30:45+00:00"
    }

    assert validate_record(record) is False
