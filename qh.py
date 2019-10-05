
# focus on upper right half, so c > r always
def remove_rc(matrix, r, c):
    matrix.pop(c)
    matrix.pop(r)
    for i in range(r):
        matrix[i].pop(c)
        matrix[i].pop(r)
    return matrix

def max_paths(matrix, n):
    #print("max_paths: {} {}".format(matrix, n))
    # base
    if n < 2:
        return 0

    # edge case of 0 and n-1 vertices together
    if matrix[0][n-1]:
        return 1 + max_paths(remove_rc(matrix,0,n-1), n-2)

    # else
    i = 1
    while i < n:
        j = 0
        while j+i < n:
            #print(j, j+i)
            if matrix[j][j+i]:
                return 1 + max_paths(remove_rc(matrix,j,j+1), n-2)
            j += 1
        i += 1

    # no more paths, abort
    return 0

if __name__ == "__main__":
    n = int(input()) # size of matrix
    matrix = [None for i in range(n)]
    for i in range(n):
        line = list(input().split(' '))
        matrix[i] = [int(num) for num in line]
    print(max_paths(matrix, n))

