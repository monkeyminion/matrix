import gaussian_elimination as ge
import funcs as f
# 3x4 matrix
#    C0 C1 C2  C3   |    C0 C1 C2  C3 
# R0 a  b  c  |d    | R0 1  b  c  |d 
# R1 e  f  g  |h    | R1 0  1  g  |h
# R2 i  j  k  |m    | R2 0  0  1  |m

class GaussJordan_Eliminate():
    def __init__(self,matrix,inverse=False):
        print('gj elim init')
        self.matrix = matrix
        if inverse is True:
            self.matrix[0] += [1,0,0]
            self.matrix[1] += [0,1,0]
            self.matrix[2] += [0,0,1]
        self.gauss_elim()
        self.jordan_elim()
        
    def gauss_elim(self):
        print('rows',len(self.matrix),'cols',len(self.matrix))
        gauss = ge.Gauss_Eliminate(self.matrix,len(self.matrix),len(self.matrix))        
        self.matrix = gauss.get_matrix()
        f.make_frac(self.matrix)

    def jordan_elim(self):
        try:
            # assert self.matrix[0][0] == '1/1'
            # assert self.matrix[1][1] == '1/1'
            # assert self.matrix[2][2] == '1/1'  #assert that gauss_elim worked
            for i in range(len(self.matrix)):
                assert self.matrix[i][i] == '1/1'
        except AssertionError:
            print('AssertionError')
            print(self.matrix)
            exit()
        if self.matrix[0][1] != '0/1':   #if b is not 0
            # R0 = bR1 - R0
            f.scale_subtract(self.matrix,1,self.matrix[0][1],0)
        f.reduce_matrix(self.matrix)
        if self.matrix[0][2] != '0/1':  #if c is not 0
            # R0 = cR2 - R0
            f.scale_subtract(self.matrix,2,self.matrix[0][2],0)
        f.reduce_matrix(self.matrix)
        if self.matrix[1][2] != '0/1':
            # R1 = gR2 - R1
            f.scale_subtract(self.matrix,2,self.matrix[1][2],1)
        f.reduce_matrix(self.matrix)
        if self.matrix[0][0] != '1/1':
            f.make_first_one(self.matrix,0,self.matrix[0][0])
        if self.matrix[1][1] != '1/1':
            f.make_first_one(self.matrix,1, self.matrix[1][1])
        if self.matrix[2][2] != '1/1':
            f.make_first_one(self.matrix,2, self.matrix[2][2])
        f.cleanans(self.matrix)
        print('-----------')
        f.ans(self.matrix)
print('hi')
# GaussJordan_Eliminate([[2,-1,0],[-1,2,-1],[0,-1,2]],inverse=True)
GaussJordan_Eliminate([[1,5,7],[-2,-7,-5]])