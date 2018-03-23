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


def hash(data):
    import hashlib
    return hashlib.sha384(bytes(data, 'utf-8')).hexdigest()


def cuted_hash(data, n):
    h = hash(data)
    ch = convert_base(h, 10, 16)
    return int(ch[:(len(str(n)))], 10)




