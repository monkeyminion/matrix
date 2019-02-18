# 3x4 matrix
#    C0 C1 C2  C3
# R0 a  b  c  |d
# R1 e  f  g  |h
# R2 i  j  k  |m
# is: [[a,b,c,d],[e,f,g,h],[i,j,k,m]]
# after make_frac: [['a/1','b/1','c/1','d/1'],
#                    ['e/1','f/1','g/1','h/1']
#                       ['i/1','j/1','k/1','m/1']]
# 'a/1'[0] = 'a', [1] = '/', [2] = '1'
import matrix_funcs, fraction
from matrix_funcs import Matrix
from fraction import Fraction
class Gauss_Eliminate():
    def __init__(self,matrix):
        self.matrix = Matrix(matrix)
        self.rows = self.matrix.rows
        self.cols = self.rows

    def main(self):
        for row in range(self.rows):
            if not self.matrix.compare_frac(row,row,1): # If pivot is not 1
                for row_sIndex in range(row,self.rows): 
                    # If nums in subsequent rows,same col are 1
                    if self.matrix.compare_frac(row_sIndex,row,1): 
                        self.matrix.swap(row,row_sIndex)
                        break
                        break
                #if not self.matrix.compare_frac(row,row,1):  # pivot is not 1,nor are any nums in the same col
                if self.matrix.compare_frac(row,row,0): # if pivot is 0
                    self.matrix.is_rowStart_zero(row,self.rows - 1,row) 
                else: 
                    self.matrix.make_first_one(row,self.matrix.get_item(row,row))
            # for nums in same col below pivot, make zero
            for later_rows in range(row+1,self.rows):
                if not self.matrix.compare_frac(later_rows,row,0):
                    self.matrix.scale_subtract(row,self.matrix.get_item(later_rows,row),later_rows)
        return self.matrix

if __name__ == '__main__':
    g = Gauss_Eliminate([[3,-1,7,1],[5,0,1,2]])
    print(g.main())

#  test cases: https://www.matesfacil.com/english/high/solving-systems-by-Gaussian-Elimination.html
# Gauss_Eliminate([[5,2,3],[-3,3,15]]) p
# Gauss_Eliminate([[3,-1,2],[-6,2,-4]]) p
# Gauss_Eliminate([[-5,1,0],[1,'-1/5',-3]]) p
# Gauss_Eliminate([[5,2,0,2],[2,1,-1,0],[2,3,-1,3]]) p
# Gauss_Eliminate([[2,-1,3,5],[2,2,3,7],[-2,3,0,-3]]) p
# Gauss_Eliminate([[1,2,3,1],[-3,-2,-1,2],[4,4,4,3]]) p 
# Gauss_Eliminate([[1,2,-3,-1,0],[0,-3,2,6,-8],[-3,-1,3,1,0],[2,3,2,-1,-8]])p
   
# PASS
# Gauss_Eliminate([[3,-1,7,1],[5,0,1,2]])# System 7 p
# System 8 skip, cannot handle sqrts yet

