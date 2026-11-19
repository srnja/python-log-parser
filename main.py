import argparse

from log_parser.processor import process_log_file
from log_parser.database import LogDatabase


def main():

    parser = argparse.ArgumentParser(
        description="Python Log Parser and Data Validation"
    )

    parser.add_argument(
        "logfile",
        help="Path to the input log file"
    )

    parser.add_argument(
        "--database",
        default="logs.db",
        help="SQLite database path"
    )

    args = parser.parse_args()

    print("\nStarting log processing...\n")

    results = process_log_file(
        args.logfile,
        args.database
    )

    print("Processing completed!")
    print("-------------------------")
    print(f"Valid records: {results['valid_records']}")
    print(f"Invalid records: {results['invalid_records']}")
    print(f"Total processed: {results['total_processed']}")

    database = LogDatabase(args.database)

    print("\nHTTP Status Summary")
    print("-------------------------")

    for row in database.get_status_summary():
        print(
            f"Status {row['status_code']}: "
            f"{row['total']} requests"
        )

    print(
        f"\nTotal database records: "
        f"{database.get_total_records()}"
    )

    database.close()


if __name__ == "__main__":
    main()
