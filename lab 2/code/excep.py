
class MatrixDemensionError(Exception):
    def __init__(self, matrix1,matrix2):
        self.rows1 = matrix1.rows
        self.rows2 =matrix2.rows
        self.cols1 = matrix1.cols
        self.cols2 = matrix2.cols
    
    def __str__(self):
        return f"add error:rows and cols of first and second matrix is equal /rows :{self.rows1,self.rows2} /cols :{self.cols1,self.cols2}"