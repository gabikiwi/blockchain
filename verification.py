from hash_util import hash_block, hash_string_256
class Verification:

    @staticmethod
    def valid_proof(transactions, last_hash, proof):
        """ Validate a proof of work and sees if it solves the puzzle algorithm 00
        : last_hash: the previous block's hash which will be stored in the 
        : proof: The proof number we are testing
         """

        # guess = (str(transactions) + str(last_hash) + str(proof)).encode()
        guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) + str(proof)).encode()

        print('This is your guess', guess, '\n')
        guess_hash = hash_string_256(guess)
        print(guess_hash, '\n')
        return guess_hash[0:2] == '00'
    
    @classmethod
    def verify_chain(cls, blockchain):
        """ Verify the current blockchain and return True if it's valid, False  """
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue
            # if block['previous_hash'] != hash_block(blockchain[index - 1]):
            if block.previous_hash != hash_block(blockchain[index - 1]):
                return False
            
            # if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            if not cls.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print('Proof of work is invalid')
                return False
        return True

    @staticmethod
    def verify_transaction(transaction, get_balance):
        sender_balance = get_balance()
        print(sender_balance)
        return (sender_balance >= transaction.amount)

    @classmethod
    def verify_transactions(cls, open_transactions, get_balance):
        return all([cls.verify_transaction(tx, get_balance) for tx in open_transactions])

        # is_valid = True
        # for tx in open_transactions:
        #     if verify_transaction(tx):
        #         is_valid = True
        #     else:
        #         is_valid = False
        # return is_valid