#!/usr/bin/python3
""" Log parsing module """
import sys
import signal


def signal_handler(sig, frame):
    """ Handle CTRL+C signal """
    print("File size: {}".format(file_size))
    for k, v in status_codes.items():
        if v != 0:
            print("{}: {}".format(k, v))
            v = 0

signal.signal(signal.SIGINT, signal_handler)


count = 0
file_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
for line in sys.stdin:
    line = line.strip()
    size = int(line.split(' ')[-1])
    code = line.split(' ')[-2]
    status_codes[code] += 1
    file_size += size
    print(line)
    count += 1
    if count % 10 == 0:
        print("File size: {}".format(file_size))
        for k, v in status_codes.items():
            if v != 0:
                print("{}: {}".format(k, v))
                v = 0


