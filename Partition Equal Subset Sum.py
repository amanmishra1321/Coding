
def iterativeWay(nums,n,sum,dp):
    for i in range(n+1):
        dp[i][0] = True
    for i in range(0,n+1):
        for j in range(1,sum+1):
            if(i-1< 0 or j < nums[i]):
                dp[i][j] = False
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        print("i=",i,dp)
        print()
    return dp[n][sum]

def canPartition(nums):
    n = len(nums)
    sum1 = sum(nums)
    dp = []
    for i in range(n):
        l = []
        for j in range((sum1//2)+1):
            l.append(-1)
        dp.append(l)
    if(sum1 % 2 ):
        return False
    return iterativeWay(nums,n-1,sum1//2,dp)


def checkPartition(nums,n,sum,dp):
    if(sum == 0):
        return True
    if n<0 or sum <0:
        return False
    if(dp[n][sum] != -1):
        return dp[n][sum]
    dp[n][sum] = checkPartition(nums,n-1,sum,dp) or checkPartition(nums,n-1,sum-nums[n],dp) 
    return dp[n][sum] 
    
print(canPartition([9,1,2,4,10]))

    
