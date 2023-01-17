mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n = 3
for i in range(n):
    for j in range(i):
        if i != j:
            mat[i][j],mat[j][i] = mat[j][i], mat[i][j]
    for r in mat:
        print(r)
    print()    

for r in mat:
    r.reverse()
    print(r)