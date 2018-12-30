import fraction_operations as fo

def make_frac(matrix):
    '''Convert a matrix with integers into a matrix with strings'''  #---
    for a,b in enumerate(matrix):
        for c,d in enumerate(b):
            if type(d) is str:
                pass
            elif d != 0:
                matrix[a][c] = f'{d}/1'
            else:
                matrix[a][c] = '0/1'

def make_first_one(matrix,row,divnum):
    '''Make the first digit of a row 1 ('1/1')'''  #---
    # Note: divnum is a String
    print('make_first_one')
    for a in range(len(matrix[row])):
        try:
            matrix[row][a] = fo.divtwofrac(matrix[row][a],divnum)
        except AssertionError:
            print("No solution")
            cleanans(matrix)
            ans(matrix)
            exit()

def swap(matrix,r1,r2):
    '''Swap two rows of a matrix, r1 and r2'''  #---
    stored = matrix[r1]
    matrix[r1] = matrix[r2]
    matrix[r2] = stored

def scale_subtract(matrix,r1,scale,r2):
    '''Multiply r1 by scale, then subtract r2. Put back in r2'''
    print('scale subtract')
    matrix[r2] = [fo.addfrac(fo.multtwofrac(b,scale),matrix[r2][a],add=False)
                  for a,b in enumerate(matrix[r1])]

    #reduce_matrix(matrix)

def is_zero(matrix,r_start,r_stop,col):  #Appears to work
    '''At each row of the rows in the range of
    rstart and rstop, is_zero will check if the
    number in the specified column is 0'''
    lst = list(range(r_start,r_stop+1))
    if matrix[r_start][col].replace('-','')[0] == '0':
        for i in lst[1::]:
            if matrix[i][col][0].replace('-','')[0] == '0': # If numerator is 0
                continue
            else:
                make_first_one(matrix,i,matrix[i][col])
                swap(matrix,r_start,i)
                break
    else:
        make_first_one(matrix,r_start,matrix[r_start][col])


def reduce_matrix(matrix):
    '''Reduce each fraction in the matrix to its simplest form''' ### ---
    for rownum,row in enumerate(matrix):
        for col,item in enumerate(row):
            matrix[rownum][col] = fo.reduce(item)

def cleanans(matrix):
    print('cleanans')
    for rownum, rowlist in enumerate(matrix):
        for col,item in enumerate(rowlist):
            denom = int(item[item.find('/')+1::])
            numer = int(item[:item.find('/'):])
            if denom == 1:
                matrix[rownum][col] = int(numer)
            elif numer == 0:
                matrix[rownum][col] = 0
def ans(matrix):
    for a in matrix:
        print(*a)