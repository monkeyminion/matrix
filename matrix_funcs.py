from fraction import Fraction 

class Matrix:
    def __init__(self,matrix):
        for row_index,row in enumerate(matrix):
            for col_index,item in enumerate(row):
                if not isinstance(item,Fraction):
                    matrix[row_index][col_index] = Fraction(item)
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) - 1

    def make_first_one(self,row,divnum):
        if self.matrix[row][0] == 1: return
        for index, col_value in enumerate(self.matrix[row]):
            try:
                if not isinstance(divnum,Fraction):
                    divnum = Fraction(divnum)
                self.matrix[row][index] = col_value / divnum
            except ZeroDivisionError:
                print('Divide by 0!')

    def swap(self, r1, r2):
        temp = self.matrix[r1]
        self.matrix[r1] = self.matrix[r2]
        self.matrix[r2] = temp

    def scale_subtract(self,r1,scale,r2):
        if not isinstance(scale,Fraction):
            scale = Fraction(scale) 
        self.matrix[r2] = [(value * scale) - self.matrix[r2][index]
                    for index,value in enumerate(self.matrix[r1])]
        
    def is_rowStart_zero(self,row_start, row_stop,col):
        row_range = list(range(row_start,row_stop+1))
        if self.matrix[row_start][col].numer == 0:
            for row in row_range:
                if self.matrix[row][col].numer != 0:
                    self.make_first_one(row,self.matrix[row][col])
                    self.swap(row_start,row)
                    break
        else:
            self.make_first_one(row_start,self.matrix[row_start][col])
    
    def __str__(self):
        return '\n'.join( '  '.join(frac.__str__() 
                for frac in row)
                for row in self.matrix)
    
    def get_item(self,row,col):
        return self.matrix[row][col]

    def compare_frac(self,row,col,other_frac):
        return self.matrix[row][col] == other_frac
# m = Matrix([[1,3,2],[3,4,Fraction(2,3)],[6,Fraction(2,4),6]])
# print(m)