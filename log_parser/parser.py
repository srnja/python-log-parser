import re
from datetime import datetime

from log_parser.validator import validate_record


LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ '
    r'\[(?P<timestamp>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<endpoint>\S+) (?P<protocol>[^"]+)" '
    r'(?P<status>\d{3}) (?P<size>\S+)'
    r'(?: "(?P<referer>[^"]*)" "(?P<user_agent>[^"]*)")?'
)


def parse_log_line(line):
    """
    Parse one Apache access log line.

    Returns:
        dict: Structured log record.
        None: If the line is malformed.
    """

    match = LOG_PATTERN.match(line.strip())

    if not match:
        return None

    data = match.groupdict()

    try:
        timestamp = datetime.strptime(
            data["timestamp"],
            "%d/%b/%Y:%H:%M:%S %z"
        )

        record = {
            "ip_address": data["ip"],
            "timestamp": timestamp.isoformat(),
            "method": data["method"],
            "endpoint": data["endpoint"],
            "protocol": data["protocol"],
            "status_code": int(data["status"]),
            "response_size": (
                int(data["size"])
                if data["size"].isdigit()
                else 0
            ),
            "referer": data.get("referer") or "",
            "user_agent": data.get("user_agent") or "",
            "event_details": (
                f'{data["method"]} {data["endpoint"]} '
                f'- HTTP {data["status"]}'
            )
        }

        if not validate_record(record):
            return None

        return record

    except (ValueError, TypeError):
        return None
