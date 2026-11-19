from log_parser.parser import parse_log_line


def test_valid_log_parsing():

    line = (
        '192.168.1.10 - - '
        '[15/Oct/2025:10:30:45 +0000] '
        '"GET /index.html HTTP/1.1" '
        '200 1024 '
        '"https://example.com" '
        '"Mozilla/5.0"'
    )

    result = parse_log_line(line)

    assert result is not None
    assert result["ip_address"] == "192.168.1.10"
    assert result["method"] == "GET"
    assert result["endpoint"] == "/index.html"
    assert result["status_code"] == 200


def test_invalid_log_parsing():

    line = "This is an invalid log entry"

    result = parse_log_line(line)

    assert result is None


def test_post_request_parsing():

    line = (
        '10.0.0.5 - - '
        '[15/Oct/2025:11:00:00 +0000] '
        '"POST /login HTTP/1.1" '
        '401 512'
    )

    result = parse_log_line(line)

    assert result is not None
    assert result["method"] == "POST"
    assert result["status_code"] == 401
