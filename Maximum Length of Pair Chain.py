def iterativeWay(arr,n,dp):
    for index in range(n-1,-1,-1):
        for prevIndex in range(index-1,-2,-1):
            ans1, ans2 = 0, 0
            # print("prevIndex",prevIndex,dp[index+1][prevIndex])
            ans1 = dp[index + 1][prevIndex]
            if prevIndex == -1 or (arr[prevIndex][1] < arr[index][0]):
                ans2 = dp[index + 1][index] + 1
            dp[index][prevIndex] =  max(ans1, ans2)
    print(dp)
    return dp[index][prevIndex]               
    

def recursion(index, prevIndex, arr, n,dp):
    if index == n:
        return 0
    if dp[index][prevIndex] != -1:
        return dp[index][prevIndex]

    ans1, ans2 = 0, 0
    ans1 = recursion(index + 1, prevIndex, arr, n,dp)
    if prevIndex == -1 or (arr[prevIndex][1] < arr[index][0]):
        ans2 = recursion(index + 1, index, arr, n,dp) + 1
    dp[index][prevIndex] =  max(ans1, ans2)
    return dp[index][prevIndex]

def findLongestChain(pairs):
    n = len(pairs)
    pairs.sort(key=lambda x: [x[0], x[1]])
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    # return recursion(0, -1, pairs, n,dp)
    return iterativeWay(pairs,n,dp)


arr = [[1,2],[2,3],[3,4]]
print(findLongestChain(arr))