def recursion(arr,index,prev,dp):
    print(dp)
    if(index == 0):
        maximum = 0
        for i in range(0,3):
            if prev != i:
                maximum = max(arr[0][i],maximum)
        return maximum 
    maxi = 0
    for i in range(0,3):
        if(prev != i):
            if(dp[index-1][i] != -1):
                sum = dp[index-1][i]+arr[index][i]
            else:
                sum = arr[index][i]+recursion(arr,index-1,i,dp)
            maxi = max(maxi,sum)
    dp[index][i] = maxi
    return maxi


def ninjaTraining(n, points):
    dp = []
    for i in range(n+1):
        dp.append([-1,-1,-1])
    return recursion(points,n-1,3,dp)
    
for i in range(int(input())):
    arr = []
    size = int(input())
    for j in range(size):
        l = list(map(int,input().split()))
        arr.append(l)
    print(ninjaTraining(size,arr))