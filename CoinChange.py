def coinChange(coins,Sum):
    dp = (Sum+1)*[0]
    dp[0]=1
    for i in coins:
        for index in range(1,len(dp)):
            print(index,i,dp)
            if(index%i == 0 or (index>=i and dp[index-i] != 0)):
                dp[index] += 1
    return dp[Sum]
    
print(coinChange([2,5,3,6],10))