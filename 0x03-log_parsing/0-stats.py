#!/usr/bin/python3
""" Log parsing module """
import sys


def print_metrics(file_size: int, status_codes: dict):
    """ print the logs after parsing """
    print("File size: {}".format(file_size))
    for k, v in status_codes.items():
        if (v > 0):
            print("{}: {}".format(k, v))


file_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
count = 0

try:
    for line in sys.stdin:
        log = line.split()
        if (len(log) < 2):
            continue
        file_size += int(log[-1])
        code = log[-2]
        if code in status_codes:
            status_codes[code] += 1
        count += 1
        if count % 10 == 0:
            print_metrics(file_size, status_codes)
except KeyboardInterrupt:
    pass
print_metrics(file_size, status_codes)
