def printer(m):
    for r in m:
        print(r)
    print()
    return

def no_unq_paths(m,n):
    grid = [[0 for j in range(n)] for i in range(m)]
    grid[0][0] = 1
    for i in range(m):
        for j in range(n):
            if j-1>=0 and i-1>=0:
                grid[i][j] += grid[i][j-1] + grid[i-1][j]
            elif j-1>= 0 and i-1<0:
                grid[i][j] += grid[i][j-1]
            elif j-1< 0 and i-1>=0:
                grid[i][j] += grid[i-1][j]
    return grid[m-1][n-1]


if __name__ == '__main__':
    m,n = 3,7
    print(no_unq_paths(m,n))
