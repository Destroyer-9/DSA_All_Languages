def no_unq_paths(r,c,m,n):
        if r < 0 or r > m-1 or c < 0 or c > n-1:
            return 0
        elif r == m-1 and c == n-1:
            return 1
        
        R = no_unq_paths(r,c+1,m,n)
        D = no_unq_paths(r+1,c,m,n)

        return R + D
        
m,n = 2,3
nop = no_unq_paths(0,0,m,n)
print(nop)