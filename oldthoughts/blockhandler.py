import blockchain
import block
class BlockHandler(object):
    """docstring for BlockHandler"""
    def __init__(self, blockChain):
        self._blockChain = blockChain

    '''
    myAddress:       miner's public key
    '''
    def createBlock(self, myAddress):
