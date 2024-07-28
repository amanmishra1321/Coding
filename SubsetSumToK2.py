for i in range(1,n+1):
        for j in range(1,k+1):
            if(j>=arr[i-1]):
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    mini = float('inf')
    for i in range(k+1):
        if(dp[n][i] == True):
            mini = min(mini,abs(i- (k-i)))
    return mini