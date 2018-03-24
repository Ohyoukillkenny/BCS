import cryptography

class requester(object):
    """docstring for requester"""
    def __init__(self, publicKey = ''):
        self._task = ''
        self._publicKey = publicKey

    def getTask(self):
        if len(self._task) == 0:
            print 'No task has been set.'
            return
        return self._task

    def setTask(self, taskDescript):
        if len(self._task) > 0:
            print 'Already Having Tasks!'
            return
        else:
            self._task = taskDescript

    def getPublicKey(self):
        return self._publicKey

    def equals(self, other):
        if other is None:
            return False
        elif not isinstance(other, requester):
            return False
        else:
            if self._publicKey == other.getPublicKey()
            return True