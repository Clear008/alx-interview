#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


code = 0
counter = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_count(dict_sc, total_size):
    """ function that count file size and status code"""

    print("File size: {}".format(total_size))
    for key, value in sorted(dict_sc.items()):
        if value != 0:
            print("{}: {}".format(key, value))


total_size = 0

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in status_codes.keys()):
                    status_codes[code] += 1

            if (counter == 10):
                print_count(status_codes, total_size)
                counter = 0

finally:
    print_count(status_codes, total_size)
