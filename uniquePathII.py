def totalUniqueWays(arr,dp): 
    n = len(arr)
    m = len(arr[0])  
    dp[0][0] = 1     
    # print("dp2",dp)
    for i in range(n):
        for j in range(m):
            if(i == 0 and j ==0):
                continue
            elif(arr[i][j] == 1):
                print(i,j)
                dp[i][j] = 0
                continue
            else:
                count1,count2 = 0,0
                if(i-1 >= 0):
                    count1 = dp[i-1][j]
                if(j-1 >= 0):
                    count2 = dp[i][j-1]
                dp[i][j] = count1+count2
                print(dp)
    return dp[n-1][m-1]

def uniquePathsWithObstacles(obstacleGrid):
    n = len(obstacleGrid)
    m = len(obstacleGrid[0])
    dp = []
    for i in range(n):
        l = []
        for j in range(m):
            l.append(-1)
        dp.append(l)

    # print("dp1",dp)
    return totalUniqueWays(obstacleGrid,dp)
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))


