import hashlib as hl
import json


def hash_string_256 (string):
    return hl.sha256(string).hexdigest()

def hash_block(block):
    """ Hashes the block """

    hashable_block = block.__dict__.copy()
    print(hashable_block)
    hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())
  #  return '-'.join([str(block[key]) for key in block])
