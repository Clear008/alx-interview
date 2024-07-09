#!/usr/bin/python3
""" Module to test the minOperations function """


def minOperations(n):
    """ Method to calculate the fewest number of operations needed
        to result in exactly n H characters in the file """

    if n <= 1:
        return 0

    opr = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            opr += factor
            n //= factor
        factor += 1

    return opr
