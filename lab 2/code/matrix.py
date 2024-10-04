import numpy as np
from excep import *

class matrix :
    __data = []
    __rows = 0
    __cols = 0

    def __init__(self,rows,cols,fill_random=False,min_val=0,max_val=10):
        self.rows = rows
        self.cols = cols
        if (fill_random):
            self.__data = [[ int(np.random.uniform(min_val,max_val)) for j in range(cols)] for i in range(rows)]
        else:
            self.__data = [[ 0 for j in range(cols)] for i in range(rows)]

    def __str__(self):
        longest = 0
        for i in self.__data:
            for j in i:
                longest = len(i) if len(i)>longest else longest#запис аналогичная: if len(i)>longest:len(i) else:longest
        result = ""
        for i in self.__data:
            for j in i:
                result += ("%10s"%str(j))+' '
            result +='\n'
        return result
    
    def __add__ (self,other_matrix):
        if ((self.cols!=other_matrix.__cols)or (self.rows!=other_matrix.__rows)):
            raise MatrixDemensionError(self,other_matrix)
        result = matrix(self.__cols,self.__rows)
        for i in range(self.__data):
            for j in range (self.__data[0]):
                result[i][j]=self[i][j]+other_matrix[i][j]
        return result
    
    def __sub__(self,other_matrix):
        if ((self.cols!=other_matrix.__cols)or (self.rows!=other_matrix.__rows)):
            raise MatrixDemensionError(self,other_matrix)
        result = matrix(self.__cols,self.__rows)
        for i in range(self.__data):
            for j in range (self.__data[0]):
                result[i][j]=self[i][j]-other_matrix[i][j]
        return result
    
    def __mul__(self,other_matrix): ##todo сделать позже
        pass
    
    def __getitem__(self,k):
        return self.__data[k]
    
