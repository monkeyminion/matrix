import gauss_elim,fraction,exceptions
from gauss_elim import Gauss_Eliminate as gauss
from fraction import Fraction
from exceptions import *
# 3x4 matrix
#    C0 C1 C2  C3   |    C0 C1 C2  C3 
# R0 a  b  c  |d    | R0 1  b  c  |d 
# R1 e  f  g  |h    | R1 0  1  g  |h
# R2 i  j  k  |m    | R2 0  0  1  |m

class GaussJordan_Eliminate(gauss):
    def __init__(self,matrix,inverse=False):
        print('gj elim init')
        super().__init__(matrix)
        # if inverse is True:
        #     self.matrix[0] += [1,0,0]
        #     self.matrix[1] += [0,1,0]
        #     self.matrix[2] += [0,0,1]
        
    def jordan_main(self):
        self.main()
        # make sure gauss_elim worked
        for row in range(self.rows):
            if not (self.matrix.compare_frac(row,row,1) or \
            self.matrix.compare_frac(row,row,0)):
                raise exceptions.GaussFailedException
        # for all non-pivots, make them 0
        for row in range(self.rows):
            for col in range(row + 1,self.cols):
                print(self.cols)
                if not self.matrix.compare_frac(row,col,0):
                    self.matrix.scale_subtract(col,self.matrix.get_item(row,col),row)
        # make sure all pivots are 1
        # if not, make it so. 
        # This does not affect non-pivots as their value is 0
        for row in range(self.rows):
            if not self.matrix.compare_frac(row,row,1):
                self.matrix.make_first_one(row,self.matrix.get_item(row,row))
        return self.matrix

    
if __name__ == "__main__":
    g = GaussJordan_Eliminate([[1,2,-3,-1,0],[0,-3,2,6,-8],[-3,-1,3,1,0],[2,3,2,-1,-8]])
    print(g.jordan_main())
# PASS test cases: https://www.matesfacil.com/english/high/solving-systems-by-Gaussian-Elimination.html
# GaussJordan_Eliminate([[5,2,3],[-3,3,15]]) p
# GaussJordan_Eliminate([[3,-1,2],[-6,2,-4]]) p
# GaussJordan_Eliminate([[-5,1,0],[1,Fraction(-1,5),-3]])p
# GaussJordan_Eliminate([[5,2,0,2],[2,1,-1,0],[2,3,-1,3]])p
# GaussJordan_Eliminate([[2,-1,3,5],[2,2,3,7],[-2,3,0,-3]])p
# GaussJordan_Eliminate([[1,2,3,1],[-3,-2,-1,2],[4,4,4,3]]) p
# GaussJordan_Eliminate([[1,2,-3,-1,0],[0,-3,2,6,-8],[-3,-1,3,1,0],[2,3,2,-1,-8]])p
# GaussJordan_Eliminate([[3,-1,7,1],[5,0,1,2]]) p #System 7
#Not tested
# Pass Test cases from https://www.cliffsnotes.com/study-guides/algebra/linear-algebra/linear-systems/gaussian-elimination
# GaussJordan_Eliminate([[1,1,3],[3,-2,4]]) eg1
# GaussJordan_Eliminate([[1,-1,1,-1,1],[2,1,-3,0,2],[5,-2,0,-3,5]]) eg8
# GaussJordan_Eliminate([[1,1,-3,0],[2,1,-1,0],[3,2,-4,0]]) eg10