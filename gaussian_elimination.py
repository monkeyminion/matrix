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
import funcs as f
from funcs import *
class Gauss_Eliminate():
    def __init__(self,matrix,rows,cols):
        self.matrix = matrix
        self.rows = rows
        self.cols = cols
        m = self.core()
    def core(self):
        f.make_frac(self.matrix)
        for r in range(self.rows):
            try:
                assert self.matrix[r][r] == '1/1'
            except AssertionError:   # pivot is NOT 1
                for i in range(r,self.rows):
                    if self.matrix[i][r] == '1/1':
                        f.swap(self.matrix,r,i)
                        break
                try:
                    assert self.matrix[r][r] == '1/1'
                except AssertionError:   # pivot is not 1 and neither are any nums in the same col
                    if self.matrix[r][r] == '0/1':
                        f.is_zero(self.matrix,r,self.rows - 1,r) 
                    else:
                        f.make_first_one(self.matrix,r,self.matrix[r][r])
                finally:
                    f.reduce_matrix(self.matrix)
            finally:
                for i in range(r+1,self.rows):
                    if self.matrix[i][r] != '0/1':
                        f.scale_subtract(self.matrix,r,self.matrix[i][r],i)
                f.reduce_matrix(self.matrix)

        print(self.matrix)
        f.cleanans(self.matrix)
        print(self.matrix)
        print('-----------')
        f.ans(self.matrix)
        return self.matrix

    def get_matrix(self):
        return self.core()
# PASS test cases: https://www.matesfacil.com/english/high/solving-systems-by-Gaussian-Elimination.html
# Gauss_Eliminate([[5,2,3],[-3,3,15]],2,2)
# Gauss_Eliminate([[3,-1,2],[-6,2,-4]],2,2)
# Gauss_Eliminate([[-5,1,0],[1,'-1/5',-3]],2,2)
# Gauss_Eliminate([[5,2,0,2],[2,1,-1,0],[2,3,-1,3]],3,3)
# Gauss_Eliminate([[2,-1,3,5],[2,2,3,7],[-2,3,0,-3]],3,3)
# Gauss_Eliminate([[1,2,3,1],[-3,-2,-1,2],[4,4,4,3]],3,3)
# Gauss_Eliminate([[1,2,-3,-1,0],[0,-3,2,6,-8],[-3,-1,3,1,0],[2,3,2,-1,-8]],4,4)
   
# PASS
Gauss_Eliminate([[3,-1,7,1],[5,0,1,2]],2,3)# System 7
# System 8 skip, cannot handle sqrts yet

