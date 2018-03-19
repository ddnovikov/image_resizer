from hashlib import md5


def generate_hash(chunks):
    hash_obj = md5()
    for chunk in chunks:
        hash_obj.update(chunk)
    return hash_obj.hexdigest()
