from functools import reduce
import hashlib as hl
import json
import pickle
# from collections import OrderedDict

from hash_util import hash_block
from block import Block
from transaction import Transaction
from verification import Verification

MINING_REWARD = 10
class Blockchain:

    def __init__(self, hosting_node_id):
        # Our starting block for the blockchain
        genesis_block = Block(0, '', [], 100, 0)
        # Initializing our (empty) blockchain list
        self.chain = [genesis_block]
        self.open_transactions = []
        self.load_data()
        self.hosting_node = hosting_node_id


    

    genesis_block = {
            'previous_hash': '', 
            'index' : 0,    
            'transactions' : [],
            'proof': 100
            }
    blockchain = [genesis_block]
  
    participants = {'Gabriel', 'Andrei', 'Mihai' }

    def load_data(self):
        try:
            with open('blockchain.txt', mode='r') as f:
                file_content = f.readlines()

                blockchain = json.loads(file_content[0][:-1])
                updated_blockchain = []
                for block in blockchain:
                    
                    converted_tx = [Transaction(tx['sender'], tx['recipient'], tx['amount']) for tx in block['transactions']]
                    # converted_tx = [Transaction(tx['sender'], tx['recipient'], tx['amount']) for tx in block['transactions']]
                    # converted_tx = [OrderedDict ([('sender',tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])]) for tx in block['transactions']]

                    # Create a block object which will no longer be a dictionary
                    updated_block = Block(
                            block['index'],
                            block['previous_hash'],
                            converted_tx,
                            block['proof'],
                            block['timestamp']                    
                            )
                    # updated_block = {
                    #         'previous_hash': block['previous_hash'],
                    #         'index': block['index'],
                    #         'proof': block['proof'],
                    #         'transactions' : [OrderedDict
                    #         ([('sender',tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])]) for tx in block['transactions']]
                    # }
                    updated_blockchain.append(updated_block)   
                    
                self.chain = updated_blockchain
                open_transactions = json.loads(file_content[1])
                updated_transactions = []
                for tx in open_transactions:
                    updated_transaction = Transaction(tx['sender'], tx['recipient'], tx['amount'])               
                    # updated_transaction = OrderedDict([('sender',tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])])
                    updated_transactions.append(updated_transaction)
                
                self.open_transactions = updated_transactions

                #   """ Using pickle for blockchain. 
                # Use blockchain.p and mode binary data 'rb' """ 
                #  file_content = pickle.loads(f.read())
                # print(file_content)
                #  blockchain = file_content['chain']
                #  open_transactions = file_content['ot']
        except (IOError, IndexError):  
            # genesis_block = {
            # 'previous_hash': '', 
            # 'index' : 0,    
            # 'transactions' : [],
            # 'proof': 100
            # }
            print("Handled exception!")
        finally:
            """ This code will always be executed and is good when we have a clean up! """
            print("Cleanup!")

    
    

    def save_data(self):
        with open('blockchain.txt', mode='w') as f:
            saveable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [tx.__dict__ for tx in block_el.transactions] ,block_el.proof, block_el.timestamp) for block_el in self.chain]]        
            # saveable_chain = [block.__dict__ for block in blockchain]
            # f.write(json.dumps(blockchain))
            f.write(json.dumps(saveable_chain))
            # f.write(str(blockchain))
            f.write('\n')
            saveable_tx = [tx.__dict__ for tx in self.open_transactions]
            f.write(json.dumps(saveable_tx))
            # f.write(json.dumps(open_transactions))
            #f.write(str(open_transactions))

            """ Using pickle for blockchain. 
            Use blockchain.p and mode binary data 'wb' """ 
            # save_data = {
            #     'chain':blockchain,
            #     'ot': open_transactions
            # }
            # f.write(pickle.dumps(save_data))

    def proof_of_work(self):
        last_block = self.chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        verifier = Verification() 
        while not verifier.valid_proof(self.open_transactions, last_hash, proof):
            proof += 1
        return proof

    def get_balance(self):
        """ Calculate and return the balance for a participant """

        participant = self.hosting_node

        tx_sender = [[tx.amount for tx in block.transactions if tx.sender == participant] for block in self.chain]
        # tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
        
        # verify open_transaction
        open_tx_sender = [tx.amount for tx in self.open_transactions if tx.sender == participant]
        tx_sender.append(open_tx_sender)

        amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0 ,tx_sender, 0)

        print(tx_sender)

        # amount_sent = 0
        # for tx in tx_sender:
        #     if len(tx) > 0:
        #         amount_sent += tx[0]
        
        tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient == participant] for block in self.chain]   
        # tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]   
        amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0 ,tx_recipient, 0)

        # amount_received = 0
        # for tx in tx_recipient:
        #     if len(tx) > 0:
        #         amount_received += tx[0]

        return amount_received - amount_sent

    def get_last_blockchain_value(self):
        """ Returns the last value of the current blockchain. """
        if len(self.chain) < 1:
            return None
        return self.chain[-1]

    # This function accepts two arguments.
    # One required one (transaction_amount) and one optional one (last_transaction)
    # The optional one is optional because it has a default value => [1]

    def add_transaction(self, recipient, sender, amount=1.0):
        """ Append a new value as well as the last blockchain value to the blockchain.
            Arguments:
            :sender: The sender of the coins.
            :recepient: The recepient of the coins.
            :amount: The amount of coins sent with the transaction (default = 1.0)
        """
        # transaction = {
        #     'sender': sender, 
        #     'recipient' : recipient,
        #     'amount' : amount
        # }

        transaction = Transaction(sender, recipient, amount)
        # transaction = OrderedDict([('sender',sender), ('recipient', recipient), ('amount', amount)])
        verifier = Verification()

        if  verifier.verify_transaction(transaction, self.get_balance):
            self.open_transactions.append(transaction)
            # participants.add(sender)
            # participants.add(recipient)
            self.save_data()
            return True
        return False   

    def mine_block(self):
        last_block = self.chain[-1]
        hashed_block = hash_block(last_block)
        print(hashed_block)

        proof = self.proof_of_work()

        # reward_transaction = {
        #     'sender' : 'MINING',
        #     'recipient' : owner,
        #     'amount' : MINING_REWARD
        # }

        reward_transaction = Transaction('MINING', self.hosting_node, MINING_REWARD)
        # reward_transaction = OrderedDict([('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])

        # for key in last_block:
        #     value = last_block[key]
        #     hashed_block = hashed_block + str(value)
        # print(hashed_block)

        # copied by value the open_transaction locally
        copied_transactions = self.open_transactions[:]
        copied_transactions.append(reward_transaction)

        block = Block(len(self.chain), hashed_block, copied_transactions, proof)

        # block = {
        #     'previous_hash': hashed_block, 
        #     'index': len(blockchain),
        #     'transactions': copied_transactions,
        #     'proof' : proof
        # }

        self.chain.append(block)
        return True