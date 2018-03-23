# def hash(data, hash_key):
  #  data = str(data)
   # return sum([ord(data[i]) ** (i + 1) for i in range(0, len(data))]) % hash_key


def hash(data):
    import hashlib
    md5 = hashlib.md5()
    md5.update(data)
    return md5.hexdigest()




