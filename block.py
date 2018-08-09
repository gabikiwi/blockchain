# from time import time

# class Block:
#     def __init__(self, index, previous_hash, transactions, proof, time=time()):
#         self.index = index
#         self.previous_hash = previous_hash
#         self.transactions = transactions
#         self.proof = proof
#         self.timestamp = time

from time import time
 
class Block:
    def __init__(self, index, previous_hash, transactions, proof, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time() if timestamp is None else timestamp
        self.transactions = transactions
        self.proof = proof
