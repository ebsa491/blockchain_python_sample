#!/usr/bin/python3

import json
import hashlib
from time import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_trxs = []
        self.new_block(previos_hash=1, proof=100)

    def new_block(self, proof, previos_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'trxs': self.current_trxs,
            'proof': proof,
            'previos_hash': previos_hash or hash(self.chain[-1])
        }
        self.current_trxs = []
        self.chain.append(block)
        return block

    def new_trx(self, sender, recipient, amount):
        self.current_trxs.append(
            {'sender': sender, 'recipient': recipient, 'amount': amount})
        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    def valid_proof(self, last_proof, proof):
        this_proof = f"{proof}{last_proof}".encode()
        this_proof_hash = hashlib.sha256(this_proof).hexdigest()
        return this_proof_hash[:4] == '0000'

    @property
    def last_block(self):
        return self.chain[-1]


def hash_block(block):
    block_str = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_str).hexdigest()
