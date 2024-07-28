def iterativeWay(n,k,arr,dp):
    for i in range(n+1):
        dp[i][0] = True
    
    for i in range(1,k+1):
        dp[0][i] = False
    # print(dp)
    for i in range(1,n+1):
        for j in range(1,k+1):
            # 3- arr[0]=1
            # dp[][] = dp[0][1] 
            if(j-arr[i-1] >= 0):
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
        # print("i=",i,dp)
    return dp[n][k]

def subsetSumToK(n,k,arr,dp):
    if(k<0 or n <0):
        return False
    elif(k == 0):
        return True
    elif(dp[n][k] != -1):
        return dp[n][k]
    dp[n][k] = subsetSumToK(n-1,k,arr,dp) or subsetSumToK(n-1,k-arr[n],arr,dp)
    return dp[n][k]


arr = [11,82,91,97,87,42,80,10,42,42] 
n = len(arr)
k = 45
dp = []
for i in range(0,n+1):
    l = []
    for i in range(0,k+1):
        l.append(-1)
    dp.append(l)

print(iterativeWay(n,k,arr,dp))