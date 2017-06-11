class Rectangle:

    def __init__(self,top_left,bottom_right):
        self.rowst = top_left[0]
        self.colst = top_left[1]
        self.rowen = bottom_right[0]
        self.colen = bottom_right[1]
        self.top_left = self.colst,self.rowst
        self.bottom_right = self.colen,self.rowen


    def __str__(self):
        return str(self.rowst)+' '+str(self.rowen)+' '+str(self.colst)+' '+str(self.colen)