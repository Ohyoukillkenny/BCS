'''
This file is to simulate requester's behavior
'''
import cryptography as cp
import blockchain as bc
import block as b
def initKeypair():
    myCrypt = cp.cryptography()
    (privateKey, publicKey) = myCrypt.createKeyPair()
    fw = open('privateKey.pem', 'w')
    fw.write(privateKey)
    fw.close()
    fw = open('publicKey.pem', 'w')
    fw.write(publicKey)
    fw.close()
    print 'Saved keys in local file.'
    return privateKey, publicKey

if __name__=="__main__":
    # myBlockchain = blockchain()
    # myBlockchain.query()
    pk, PK = initKeypair()
    UserInterface.RequesterRegister(PK)
    myTask = 'Sense WiFi Signal!'

