class DataPool(object):
    """docstring for DataPool"""
    def __init__(self, dPool = {}):
        if len(dPool) > 0:
            self._H = {}
        else: 
            self._H = dPool.getH()

    def getH(self):
        return self._H

    def addData(self, data):
        hashkey = data.getHash()
        if hashkey in self._H:
            print('Already exist data in data pool or hash collision.')
            return False
        self._H[hashkey] = data
        return True


    def removeData(self, dataHash):
        rm = self._H.pop(dataHash, None)
        if rm is None:
            return False
        else:
            return True

    def getData(self, dataHash):
        if dataHash in self._H:
            return self._H[dataHash]
        else:
            print('This data is not in data pool.')
            return None

    def getDataList(self):
        dataList = []
        for k,v in self._H.iteritems():
            dataList.append(v)
        return dataList

