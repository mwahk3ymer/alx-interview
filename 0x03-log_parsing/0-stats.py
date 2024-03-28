#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""

import sys

def compute_metrics():
    # Initialize variables
    cache = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0}
    total_size = 0
    counter = 0

    try:
        # Read stdin line by line
        for line in sys.stdin:
            line_list = line.split(" ")
            if len(line_list) > 4:
                # Extract status code and file size
                code = line_list[-2]
                size = int(line_list[-1])

                # Update cache and total size
                if code in cache:
                    cache[code] += 1
                total_size += size
                counter += 1

            # Print metrics after every 10 lines
            if counter == 10:
                counter = 0
                print('File size:', total_size)
                for key in sorted(cache.keys()):
                    if cache[key] != 0:
                        print('{}: {}'.format(key, cache[key]))

    except KeyboardInterrupt:
        # Handle keyboard interruption
        print('File size:', total_size)
        for key in sorted(cache.keys()):
            if cache[key] != 0:
                print('{}: {}'.format(key, cache[key]))

    except Exception as e:
        # Handle other exceptions
        print('An error occurred:', e)

if __name__ == "__main__":
    compute_metrics()
