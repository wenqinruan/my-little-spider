import hashlib


def my_md5(data):
    hash_md5 = hashlib.md5(data)
    return hash_md5.hexdigest()
