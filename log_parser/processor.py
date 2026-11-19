from log_parser.parser import parse_log_line
from log_parser.database import LogDatabase


def process_log_file(file_path, db_path="logs.db", batch_size=500):
    """
    Process a large log file using streaming and batch insertion.

    Valid records are stored in SQLite.
    Malformed records are skipped and counted.
    """

    database = LogDatabase(db_path)

    valid_count = 0
    invalid_count = 0
    batch = []

    try:
        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="replace"
        ) as log_file:

            for line in log_file:

                record = parse_log_line(line)

                if record is None:
                    invalid_count += 1
                    continue

                batch.append(record)
                valid_count += 1

                if len(batch) >= batch_size:
                    database.insert_many(batch)
                    batch.clear()

            # Insert remaining records.
            if batch:
                database.insert_many(batch)

    finally:
        database.close()

    return {
        "valid_records": valid_count,
        "invalid_records": invalid_count,
        "total_processed": valid_count + invalid_count
    }
