
class pair:
    def __init__(self):
        self.first = None
        self.second = None 

    def put(self, item):
        if(self.first == None):
            self.first = item
        else:
            self.second = item

    def getFirst(self):
        return self.first 
    def getSecond(self):
        return self.second
