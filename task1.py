import hashlib


def hashing(string: str, hash_t: str = 'sha256') -> str:
    string_enc = string.encode()
    hash_str = hashlib.new(hash_t)
    hash_str.update(string_enc)
    return hash_str.hexdigest()


s = "Python Bootcamp"
print(hashing(s))