def majorityElementII(arr):
    dt = dict()
    l = len(arr)
    if l == 1:
        return arr
    mj = []
    for n in arr:
        if n in dt:
            dt[n] += 1
            if dt[n] >= l//3:
                mj.append(n)
        else:
            dt[n] = 0
    print(dt)
    return mj

x = majorityElementII([3,2,2,1,5,2,3])
print(x)