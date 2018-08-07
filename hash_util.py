import hashlib as hl
import json


def hash_string_256 (string):
    return hl.sha256(string).hexdigest()

def hash_block(block):
    """ Hashes the block """

    return hash_string_256(json.dumps(block, sort_keys=True).encode())
  #  return '-'.join([str(block[key]) for key in block])
