from hashlib import md5


def generate_hash(instance):
    hash_obj = md5()
    for chunk in instance.image.chunks():
        hash_obj.update(chunk)
    return hash_obj.hexdigest()
