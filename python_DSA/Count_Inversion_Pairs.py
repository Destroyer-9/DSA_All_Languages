def ms(ar):
    if len(ar) > 1:
         m = (len(ar))//2

         l = ar[:m:]
         r = ar[m::]

         lp = ms(l)
         rp = ms(r)
        
         pair = lp + rp

         i =j = k =0

         while i < len(l) and j < len(r):

             if l[i] < r[j]:
                 ar[k] = l[i]
                 i += 1
             elif l[i] >= 2*r[j]:
                 ar[k] = r[j]
                 pair += len(l)-i
                 j += 1
             k += 1

         while i < len(l):
             ar[k] = l[i]
             i +=1
             k += 1

         while j < len(r):
             ar[k] = r[j]
             j += 1
             k += 1

         return pair
    return 0

arr = [1,3,2,3,1] #[ 1,4,3,2,1]

print(arr)

print(ms(arr))

print(arr)