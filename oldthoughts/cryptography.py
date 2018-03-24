__author__      = "Kenny"
__copyright__   = "MIT"
__email__ = "kenny_kong@foxmail.com"

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

'''
self._bits:     the key size (in bits) of the RSA modulus is set to be 1024 
                (it must be a multiple of 256, and no smaller than 1024.)
createKeyPair(Dir=None):    create key pairs for users, dir is the path of saved keypair
encryptMsg(PK, msg):        encrypt the message by using the public key of the recipient
decryptMsg(pk, cryptMsg):   decrypt the message by using personal private key
signatureMsg(pk, msg):      signate the message by using private key
verifySig(sig, PK, msg):    verify one's signature by comparing the signature with the hash result of public key and message
'''
class cryptography(object):

    def __init__(self):
        self._bits = 1024
    
    def createKeyPair(self, Dir=None):
        rsa = RSA.generate(self._bits)
        privateKey = rsa.exportKey()
        publicKey = rsa.publickey().exportKey()
        return (privateKey, publicKey)

    def encryptMsg(self, PK, Msg):
        publicKey = RSA.importKey(PK)
        cipher = Cipher_pkcs1_v1_5.new(publicKey)
        cipher_text = base64.b64encode(cipher.encrypt(Msg))
        return cipher_text

    def decryptMsg(self, pk, cryptMsg):
        privateKey = RSA.importKey(pk)
        cipher = Cipher_pkcs1_v1_5.new(privateKey)
        text = cipher.decrypt(base64.b64decode(cryptMsg), self._bits)
        return text

    def signatureMsg(self, pk, Msg):
        rsakey = RSA.importKey(pk)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(Msg)
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
        return signature

    def verifySig(self, sig, PK, Msg):
        rsakey = RSA.importKey(PK)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        # Assumes the data is base64 encoded to begin with
        digest.update(Msg)
        is_verify = verifier.verify(digest, base64.b64decode(sig))
        return is_verify

def main():
    myCrypt = cryptography()
    (B_pk, B_PK) = myCrypt.createKeyPair()
    print B_PK
    message = "Hello, Bob! I am Alice!"
    encryptText = myCrypt.encryptMsg(B_PK, message)
    print encryptText
    print myCrypt.decryptMsg(B_pk, encryptText)
    msg = "this message is sig by Bob"
    sig = myCrypt.signatureMsg(B_pk, msg)
    print myCrypt.verifySig(sig, B_PK, msg)

if __name__=="__main__":
    # main()
    pass
