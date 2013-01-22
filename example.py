#!/usr/bin/env python

import sys
import shelve

from uuid import uuid1

class KVError(Exception):
    pass

def get_transaction(transaction_id):
    database = get_database()

    try:
        value = database[transaction_id]
    except KeyError:
        raise KVError('Transaction {0} does not exists'.format(transaction_id))

    database.close()

    return value

def save_transaction(transaction_id=None, value=None, print_result=True):
    if not value:
        raise KVError('You need a value to store')

    if transaction_id:
        save_to_db(key=transaction_id, value=value, print_result=print_result)
    else:
        save_to_db(key=None, value=value, print_result=print_result)

def save_to_db(key, value, print_result=True):
    database = get_database()

    if not key:
        key = generate_id()

    database[key] = value
    database.close()

    if print_result:
        print('Stored {0}:{1}'.format(key, value))

def generate_id():
    return uuid1().__str__()

def get_database():
    return shelve.open('transactions', writeback=True)

if __name__ == '__main__':
    # insert some random transactions
    save_transaction('1', '$0.99', print_result=False)
    save_transaction('2', '$9.99', print_result=False)
    save_transaction('3', '$2.99', print_result=False)

    if len(sys.argv) > 1:
        print(get_transaction(sys.argv[1]))
