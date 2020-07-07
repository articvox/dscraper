from functools import reduce


def deep_get(dictionary, keys, default={}):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)
