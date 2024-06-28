#!/usr/bin/python3
""" UTF-8 Validation module """


def validUTF8(data):
    """  determines if a given data set represents a valid UTF-8 encoding """
    if (type(data) is not list or any(not isinstance(i, int) for i in data)):
        return False
    byte_data = [i & 0xFF for i in data]
    try:
        byte_data = bytes(byte_data)
        byte_data.decode('utf-8')
    except UnicodeDecodeError:
        return False
    return True
