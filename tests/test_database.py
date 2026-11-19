from log_parser.database import LogDatabase


def sample_record():

    return {
        "ip_address": "192.168.1.1",
        "timestamp": "2025-10-15T10:30:45+00:00",
        "method": "GET",
        "endpoint": "/home",
        "protocol": "HTTP/1.1",
        "status_code": 200,
        "response_size": 1024,
        "referer": "",
        "user_agent": "Mozilla/5.0",
        "event_details": "GET /home - HTTP 200"
    }


def test_insert_and_retrieve(tmp_path):

    db = LogDatabase(str(tmp_path / "test.db"))

    db.insert_record(sample_record())

    records = db.get_all_records()

    assert len(records) == 1
    assert records[0]["ip_address"] == "192.168.1.1"

    db.close()


def test_filter_by_ip(tmp_path):

    db = LogDatabase(str(tmp_path / "test.db"))

    db.insert_record(sample_record())

    results = db.filter_by_ip("192.168.1.1")

    assert len(results) == 1

    db.close()


def test_filter_by_status(tmp_path):

    db = LogDatabase(str(tmp_path / "test.db"))

    db.insert_record(sample_record())

    results = db.filter_by_status(200)

    assert len(results) == 1

    db.close()


def test_status_summary(tmp_path):

    db = LogDatabase(str(tmp_path / "test.db"))

    db.insert_record(sample_record())

    summary = db.get_status_summary()

    assert summary[0]["status_code"] == 200
    assert summary[0]["total"] == 1

    db.close()
