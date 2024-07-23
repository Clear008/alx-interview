#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Number of bytes in the current UTF-8 character"""
    num_bytes = 0

    mask_a = 1 << 7
    mask_b = 1 << 6

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:

            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask_a and not (byte & mask_b)):
                return False

        num_bytes -= 1
    return num_bytes == 0
