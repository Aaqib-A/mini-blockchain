
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        """Creates a new block and adds it to the chain"""
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'recipient': recipient,
            'amount': amount,
        })
        return self.current_transactions[-1]

    @staticmethod
    def hash(block):
        """Hashes a block"""
        pass

    @property
    def last_block(self):
        """Returns the last block in the chain"""
        pass

    