# this interface is simplified for a single task from a single requester
class Interface(object):
    def __init__(self):
        self._task = ''
        self._requester = None
        self._miners = []
        self._workers = []

    def __str__(self):
        return task

    def askPrivateKey(self):
        pkFile = raw_input("Please input the path of your privateKey file:")
        with open(pkFile) as f:
            privateKey = f.read()
            f.close()
        return privateKey
        
    def getTask(self, identity):
        if identity 
        return self._task

    def RequesterRegister(self, publicKey):
        if self._requester is not None:
            print "Already exist requester!"
        self._requester = 