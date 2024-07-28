def partitionArray(arr,n):
    k = sum(arr)
    dp = []
    for i in range(0,n+1):
        l = []
        for i in range(0,k+1):
            l.append(False)
        dp.append(l)
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

    
    # return dp[n][k]
    mini = float('inf')
    for i in range(k+1):
        if(dp[n][i] == True):
            mini = min(mini,abs(i- (k-i)))
    return mini
    
arr = [8,6,5]
n = len(arr)
print(partitionArray(arr,n))