#!/usr/bin/python3

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

    def new_trx(self):
        pass

    @property
    def last_block(self):
        pass


def hash_block(block):
    pass
