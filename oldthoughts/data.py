import base64
from Crypto.Hash import SHA
class Data(object):
    """
    sensingRes:     sensing result from worker
    sig:            signature of the worker
    blackboxRes:    the blackbox Result of the sensing result
    """
    def __init__(self, sensingRes, sig, publicKey, blackboxRes):
        self._sensingRes = ''
        self._signature = sig # sig = hash (worker's public key | sensing res)
        self._publicKey = publicKey
        self._blackboxRes = blackboxRes
        digest = SHA.new()
        Msg = sensingRes + sig + publicKey + blackboxRes
        digest.update(Msg)
        self._hash = base64.b64encode(digest.digest())

    def getHash(self):
        return self._hash
          
    def getSensingRes(self):
        return self._sensingRes

    def getSignature(self):
        return self._signature

    def getPublicKey(self):
        return self._publicKey

    def equals(self, other):
        if other is None:
            print('object is empty')
            return False
        elif not isinstance(other, Data):
            return False
        elif not self._hash == other.getHash():
            return False
        else:
            return True