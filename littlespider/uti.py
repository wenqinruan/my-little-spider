import hashlib


def my_md5(data):
    hash_md5 = hashlib.md5(data.encode(encoding='utf-8'))
    return hash_md5.hexdigest()
