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
        print('ge init')
        self.matrix = matrix
        self.rows = rows
        self.cols = cols
        m = self.core()
        print('hello')
    def core(self):
        print('core!')
        f.make_frac(self.matrix)
        for r in range(self.rows):
            try:
                assert self.matrix[r][r] == '1/1'
                print('ge assertion line 27')
            except AssertionError:   # pivot is NOT 1
                for i in range(r,self.rows):
                    if self.matrix[i][r] == '1/1':
                        print('ge line 31 AssertionError')
                        f.swap(self.matrix,r,i)
                try:
                    assert self.matrix[r][r] == '1/1'
                    print('ge assertion line 35 ')
                except AssertionError:   # pivot is not 1 and neither are any nums in the same col
                    print('ge line 37 AssertionError')
                    if self.matrix[r][r] == '0/1':
                        print('AE line 39 is_zero')
                        f.is_zero(self.matrix,r,self.rows,r) #ERROR
                    else:
                        print('AE line 42 make_first_one')
                        f.make_first_one(self.matrix,r,self.matrix[r][r])
                finally:
                    print('AssertionError handled, line 45 reduce_matrix')
                    f.reduce_matrix(self.matrix)
            finally:
                print('ge finally corresponds to line 27 assert')
                print('ge iter ',r)
                for i in range(r+1,self.rows):
                    if self.matrix[i][r] != '0/1':
                        print('line 52 scale_subtract')
                        f.scale_subtract(self.matrix,r,self.matrix[i][r],i)
                print('iter',r,'reduce matrix')
                f.reduce_matrix(self.matrix)

        print(self.matrix)
        f.cleanans(self.matrix)
        print(self.matrix)
        print('-----------')
        f.ans(self.matrix)
        return self.matrix

    def get_matrix(self):
        return self.core()
Gauss_Eliminate([[1,2,-2,2,-1,3,0],[2,-1,3,1,-3,2,17],[1,3,-2,1,-2,-3,-5],[3,-2,1,-1,3,-2,-1],[-1,-2,1,2,-2,3,10],[1,-3,1,3,-2,1,11]],6,6)
