# def hash(data, hash_key):
  #  data = str(data)
   # return sum([ord(data[i]) ** (i + 1) for i in range(0, len(data))]) % hash_key


def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def get_hash(data, n):
    """Returns the truncated SHA521 hash of the message."""
    import hashlib
    message_hash = hashlib.sha512(data).digest()
    e = int.from_bytes(message_hash, 'big')

    # FIPS 180 says that when a hash needs to be truncated, the rightmost bits
    # should be discarded.
    z = e >> (e.bit_length() - n.bit_length())

    assert z.bit_length() <= n.bit_length()

    return z




