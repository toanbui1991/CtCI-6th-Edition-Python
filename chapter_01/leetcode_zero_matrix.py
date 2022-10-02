"""
problem: given m*n matrix, do tranformation in that matrix which 
analyze: matrix is just a list of list
solution:
    you need set to keep index column and row index which 0 happend
"""
def zero_matrix(matrix):
    m = len(matrix) #column length
    n = len(matrix[0]) #row length
    #two set to keep tract of column and row index which o happend
    rows = set()
    cols = set()
    #find cols and rows
    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.add(x)
                cols.add(y)
    #using cols and row to assign 0 to matrix
    for x in range(m):
        for y in range(n):
            if (x in rows) or (y in cols):
                matrix[x][y] = 0

    return matrix