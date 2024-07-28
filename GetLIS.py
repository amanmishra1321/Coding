#print  longest increasing subsequence
def getLISLen(arr):
    n = len(arr)
    dp = [1]*(n)
    hashmap = [-1]
    
    for i in range(1,n):
        hashmap.append(i)
        for j in range(0,i):
            if(arr[j] < arr[i] and 1+dp[j] > dp[i]):
                dp[i] = 1+dp[j]
                hashmap[-1] = j
    
    maxVal,index = 1,n-1            
    for i in range(n-1,-1,-1):
        if maxVal<dp[i]:
            maxVal = dp[i]
            index = i
    ans = []
    while(index != -1):
        ans.append(arr[index])
        index = hashmap[index]
        
    return ans[::-1]

arr = [5,4,11,1,16,8]
print(getLISLen(arr))