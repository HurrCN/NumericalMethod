#Developed by M Hurricane
#Finished June 13, 2021

import sys

A = [[5.,4.,3.,2.,1.],[4.,3.,2.,1.,5.],[3.,2.,9.,5.,4.],[2.,1.,5.,4.,3.],[1.,2.,3.,4.,5.]]
B = [[48],[38],[64],[43],[42]]
#A = [[5.,3.,1.],[3.,9.,4.],[1.,3.,5.]]
#B = [[9.0],[16.0],[9.0]]

def print_matrix(Title, M):
    print(Title)
    for row in M:
        print([round(x,3)+0 for x in row])
        
def print_matrices(Action, Title1, M1, Title2, M2):
    print(Action)
    print(Title1, '\t'*int(len(M1)/2)+"\t"*len(M1), Title2)
    for i in range(len(M1)):
        row1 = ['{0:+7.3f}'.format(x) for x in M1[i]]
        row2 = ['{0:+7.3f}'.format(x) for x in M2[i]]
        print(row1,'\t', row2)
        
def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC

def matrix_multiply(A,B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        print('Number of A columns must equal number of B rows.')
        sys.exit()

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

AM = copy_matrix(A)
n = len(A)
BM = copy_matrix(B)

print_matrices('Starting Matrices are:', 'AM Matrix', AM, 
               'BM Matrix', BM)
print()

indices = list(range(n)) # allow flexible row referencing ***
for fd in range(n): # fd stands for focus diagonal
    fdScaler = 1.0 / AM[fd][fd]
    # FIRST: scale fd row with fd inverse. 
    for j in range(n): # Use j to indicate column looping.
        AM[fd][j] *= fdScaler
    BM[fd][0] *= fdScaler
    
    # Section to print out current actions:
    string1  = '\nUsing the matrices above, '
    string1 += 'Scale row-{} of AM and BM by '
    string2  = 'diagonal element {} of AM, '
    string2 += 'which is 1/{:+.3f}.\n'
    stringsum = string1 + string2
    val1 = fd+1; val2 = fd+1
    Action = stringsum.format(val1,val2,round(1./fdScaler,3))
    print_matrices(Action, 'AM Matrix', AM, 'BM Matrix', BM)
    print()
    
    # SECOND: operate on all rows except fd row.
    for i in indices[0:fd] + indices[fd+1:]: # *** skip fd row.
        crScaler = AM[i][fd] # cr stands for "current row".
        for j in range(n): # cr - crScaler*fdRow.
            AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
        BM[i][0] = BM[i][0] - crScaler * BM[fd][0]
        
        # Section to print out current actions:
        string1  = 'Using matrices above, subtract {:+.3f} *'
        string1 += 'row-{} of AM from row-{} of AM, and '
        string2 = 'subtract {:+.3f} * row-{} of BM '
        string2 += 'from row-{} of BM\n'
        val1 = i+1; val2 = fd+1
        stringsum = string1 + string2
        Action = stringsum.format(crScaler, val2, val1, 
                                  crScaler, val2, val1)
        print_matrices(Action, 'AM Matrix', AM, 
                               'BM Matrix', BM)
        print()

print("Now we multiply the original A matrix times our solution for X, which is BM.")
print_matrix('If we get our starting X, our solution is proved.\n', matrix_multiply(A,BM))