import data
import base64
from Crypto.Hash import SHA

class genesisBlock(object):
    """This block is created by the requester."""
    def __init__(self, arg):
        self.arg = arg

class block(object):
    """
    byte prevHash, 
    PublicKey address (Miner's publickey)
        (RSA.importKey(PK)), PK is str
    """
    def __init__(self, prevHash, address, nonce):
        self._prevBlockHash = prevHash
        # self.COINBASE = 25.0
        self._nonce = nonce
        self._address = address
        self._dataList = [] # list [Data]
        self._hash = None

    # def getCoinbase(self):
    #     return self._coinbase

    def getHash(self):
        return self._hash

    def getPrevBlockHash(self):
        return self._prevBlockHash

    def getDataList(self):
        return self._dataList

    def getData(self, index):
        return self._dataList[index]

    def addData(self, data):
        self._dataList.append(data)

    # might have problem here since SHA in python, the type(raw) is str
    def getRawBlock(self):
        raw = self._prevBlockHash
        raw += base64.b64encode(self._address)
        raw += base64.b64encode(self._nonce)
        for data in self._dataList:
            raw += base64.b64encode(data.getRawData())
        return raw # byte


    def finalize(self):
        try:
            digest = SHA.new()
            Msg = base64.b64decode(self.getRawData()) # str
            digest.update(Msg)
        else:
            print 'Block cannot be hashed!'
            return False
        self._hash = base64.b64encode(digest.digest()) # byte
        return True

        