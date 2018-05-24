"""
* Coin - chain of signatures
* Chain - seq. of hash of (block + prev hash)
* Block - header (prev hash, nonce, hash) + transactions
* Proof of work - Create value when hash starts with zeros
* Transactions - Contains multiple inputs and outputs
"""
class Amount:

    def __init__(self, uuid, amount):
        self.uuid = uuid
        self.amount = amount

    def todict(self):
        """Convert class to serializable dictionary."""
        return {'uuid': self.uuid,
                'amount': self.amount}
