import ipaddress
from datetime import datetime


def validate_ip(ip_address):
    """Check whether an IP address is valid."""
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False


def validate_timestamp(timestamp):
    """Validate Apache and ISO-formatted timestamps."""

    if not isinstance(timestamp, str):
        return False

    try:
        datetime.strptime(
            timestamp,
            "%d/%b/%Y:%H:%M:%S %z"
        )
        return True
    except ValueError:
        pass

    try:
        datetime.fromisoformat(timestamp)
        return True
    except ValueError:
        return False


def validate_record(record):
    """Validate all required log record fields."""

    required_fields = [
        "ip_address",
        "timestamp",
        "method",
        "endpoint",
        "status_code",
        "event_details"
    ]

    for field in required_fields:
        if field not in record or record[field] is None:
            return False

    if not validate_ip(record["ip_address"]):
        return False

    if not validate_timestamp(record["timestamp"]):
        return False

    if not isinstance(record["status_code"], int):
        return False

    if not 100 <= record["status_code"] <= 599:
        return False

    return True
