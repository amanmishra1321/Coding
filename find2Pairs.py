from collections import defaultdict
def findPairs(arr, n): 
    hashMap = defaultdict(list)
    for i in range(n):
        for j in range(i+1,n):
            sum = arr[i]+arr[j]
            if(sum in hashMap):
                lists = hashMap[sum]
                for key in lists:
                    if( key[0] != i and key[1] != i and key[0] != j and key[1] != j):
                        return 1
                    else:
                        hashMap[sum].append((i,j))
            else:
                hashMap[sum] = [(i,j)]
    
    return 0
print(findPairs([20,20,7,16,6],5))


