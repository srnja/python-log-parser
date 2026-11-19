import sqlite3


class LogDatabase:

    def __init__(self, db_path="logs.db"):
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.create_table()

    def create_table(self):
        """Create the log records table."""

        query = """
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            method TEXT NOT NULL,
            endpoint TEXT NOT NULL,
            protocol TEXT,
            status_code INTEGER NOT NULL,
            response_size INTEGER DEFAULT 0,
            referer TEXT,
            user_agent TEXT,
            event_details TEXT NOT NULL
        )
        """

        with self.connection:
            self.connection.execute(query)

    def insert_record(self, record):
        """Insert one validated record."""

        query = """
        INSERT INTO logs (
            ip_address, timestamp, method, endpoint,
            protocol, status_code, response_size,
            referer, user_agent, event_details
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        values = (
            record["ip_address"],
            record["timestamp"],
            record["method"],
            record["endpoint"],
            record.get("protocol", ""),
            record["status_code"],
            record.get("response_size", 0),
            record.get("referer", ""),
            record.get("user_agent", ""),
            record["event_details"]
        )

        with self.connection:
            self.connection.execute(query, values)

    def insert_many(self, records):
        """Insert multiple records efficiently."""

        query = """
        INSERT INTO logs (
            ip_address, timestamp, method, endpoint,
            protocol, status_code, response_size,
            referer, user_agent, event_details
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        values = [
            (
                r["ip_address"],
                r["timestamp"],
                r["method"],
                r["endpoint"],
                r.get("protocol", ""),
                r["status_code"],
                r.get("response_size", 0),
                r.get("referer", ""),
                r.get("user_agent", ""),
                r["event_details"]
            )
            for r in records
        ]

        with self.connection:
            self.connection.executemany(query, values)

    def get_all_records(self):
        """Retrieve all records."""

        cursor = self.connection.execute(
            "SELECT * FROM logs ORDER BY timestamp"
        )

        return [dict(row) for row in cursor.fetchall()]

    def filter_by_ip(self, ip_address):
        """Retrieve records belonging to an IP."""

        cursor = self.connection.execute(
            "SELECT * FROM logs WHERE ip_address = ?",
            (ip_address,)
        )

        return [dict(row) for row in cursor.fetchall()]

    def filter_by_status(self, status_code):
        """Filter records by HTTP status."""

        cursor = self.connection.execute(
            "SELECT * FROM logs WHERE status_code = ?",
            (status_code,)
        )

        return [dict(row) for row in cursor.fetchall()]

    def get_status_summary(self):
        """Summarize HTTP response status codes."""

        query = """
        SELECT status_code, COUNT(*) AS total
        FROM logs
        GROUP BY status_code
        ORDER BY status_code
        """

        cursor = self.connection.execute(query)

        return [dict(row) for row in cursor.fetchall()]

    def get_total_records(self):
        cursor = self.connection.execute(
            "SELECT COUNT(*) FROM logs"
        )

        return cursor.fetchone()[0]

    def close(self):
        self.connection.close()
