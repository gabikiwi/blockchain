from functools import reduce
import hashlib as hl
import json
from collections import OrderedDictq

# Initializing our (empty) blockchain list
MINING_REWARD = 10

genesis_block = {
        'previous_hash': '', 
        'index' : 0,    
        'transactions' : [],
        'proof': 100
        }
blockchain = [genesis_block]
open_transactions = []
owner = 'Gabriel'
participants = {'Gabriel', 'Andrei', 'Mihai' }

def hash_block(block):
    """ Hashes the block """

    return hl.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
  #  return '-'.join([str(block[key]) for key in block])

def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hl.sha256(guess).hexdigest()
    print(guess_hash)
    return guess_hash[0:2] == '00'

def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    
    # verify open_transaction
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)

    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0 ,tx_sender, 0)

    print(tx_sender)

    # amount_sent = 0
    # for tx in tx_sender:
    #     if len(tx) > 0:
    #         amount_sent += tx[0]
    
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]   
    amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0 ,tx_recipient, 0)

    # amount_received = 0
    # for tx in tx_recipient:
    #     if len(tx) > 0:
    #         amount_received += tx[0]

    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    print(sender_balance)
    return (sender_balance >= transaction['amount'])



def add_transaction(recipient, sender=owner, amount=1.0):
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

    transaction = OrderedDict([('sender',sender), ('recipient', recipient), ('amount', amount)])

    if  verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False   


def mine_block():
    last_block = blockchain [-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)

    proof = proof_of_work()

    # reward_transaction = {
    #     'sender' : 'MINING',
    #     'recipient' : owner,
    #     'amount' : MINING_REWARD
    # }

    reward_transaction = OrderedDict([('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])

    # for key in last_block:
    #     value = last_block[key]
    #     hashed_block = hashed_block + str(value)
    # print(hashed_block)

    # copied by value the open_transaction locally
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)

    block = {
        'previous_hash': hashed_block, 
        'index': len(blockchain),
        'transactions': copied_transactions,
        'proof' : proof
    }

    blockchain.append(block)
    return True


def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    tx_recipient = input('enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    """ Output the blockchain list to the console """
    for block in blockchain:
        print('Outputting Block')
        print(block)


def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False  """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
        
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print('Proof of work is invalid')
            return False

    return True



def verify_chain_old():
    # block_index = 0
    is_valid = True

    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1



    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     if block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    return is_valid


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])

    # is_valid = True
    # for tx in open_transactions:
    #     if verify_transaction(tx):
    #         is_valid = True
    #     else:
    #         is_valid = False
    # return is_valid


# Get the first transaction input and add the value to the blockchain
# tx_amount = get_user_input()
# add_value(tx_amount)

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add  new transaction value')
    print('2: Mine a new block')
    print('3: Output the bockchain blocks')
    print('4: Output participants')
    print('5: Check transaction validity')
    print('h: Manipultate the bockchain')
    print('q: Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data

        # Add transaction amount to the blockchain
        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed!')
            
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []

    elif user_choice == '3':
        print_blockchain_elements()

    elif user_choice == '4':
        print(participants)
    
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('Thre are invalid transactions')

    elif  user_choice == 'h':
        if len(blockchain) >= 1:
           blockchain[0]= {
                'previous_hash': '', 
                'index' : 0,
                'transactions' : [{'sender': 'Hacker' , 'recipient': 'Max', 'amount': 100}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
        # break
    else:
        print('Input was invalid, please pick  vallue from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
    print('Balance of {}: {:6.2f}'.format('Gabriel', get_balance('Gabriel')))
else:
    print('User left!')


print('Done!')
