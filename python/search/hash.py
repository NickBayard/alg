import struct

SMALL_PRIME = 31

def hash_pos_int(i, m):
    # i is the integer to hash
    # m is the array size (should be prime)
    return i % m

def hash_float(f, m):
    bytes = struct.pack('!f', f)
    integer = struct.unpack('!i', bytes)
    return hash_pos_int(integer, m)


def hash_string(s, m):
    h = 0
    for c in s:
        h = (SMALL_PRIME * hash + ord(c)) % m
    return h

def hash_mixed(mixed, m):
    h = 0
    for item in mixed:
        h = (SMALL_PRIME * hash + mixed) % m
    return h
