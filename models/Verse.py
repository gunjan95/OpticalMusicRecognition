class Verse:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def setStart(self,position):
        self.start = position

    def setEnd(self,position):
        self.end = position

    def __eq__(self, other):
        return self.start == other.start and self.end<other.end

    def __lt__(self, other):
        if self.start != other.start:
            return self.start<other.start
        return self.end<other.start