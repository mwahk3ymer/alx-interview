#!/usr/bin/python3
import sys

def parse_log():
    total_file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    lines_read = 0

    try:
        for line in sys.stdin:
            fields = line.split()
            if len(fields) >= 9:
                status_code = int(fields[8])
                file_size = int(fields[7])
                total_file_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1

                lines_read += 1

                if lines_read % 10 == 0:
                    print_statistics(total_file_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes)

def print_statistics(total_file_size, status_codes):
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")

if __name__ == "__main__":
    parse_log()
