#!/usr/bin/python3
""" UTF-8 Validation module """


def validUTF8(data):
    """  determines if a given data set represents a valid UTF-8 encoding """
    if type(data) is not list or any(not isinstance(i, int) for i in data):
        return False
    data_bytes = [byte & 0xFF for byte in data]
    try:
        data_bytes = bytes(data_bytes)
        data_bytes.decode('utf-8')
    except UnicodeDecodeError:
        return False
    return True
