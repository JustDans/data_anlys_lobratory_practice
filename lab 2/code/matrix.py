from random import *

class matrix :
    def __init__(self,rows,cols,fill_random=False,min_val=0,max_val=0):
        self.rows = rows
        self.cols = cols
        self.data = []
        if (fill_random):
            self.data = [[ int(random.uniform(min_val,max_val)) for j in range(cols)] for i in range(rows)]
        else:
            self.data = [[ 0 for j in range(cols)] for i in range(rows)]


    def __str__(self):
        pass