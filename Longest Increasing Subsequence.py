def iterativeWay(arr,dp):
    n = len(arr)
    for index in range(n-1,-1,-1):
        for prevIndex in range(n,-1,-1):
            ans1,ans2 = 0,0
            ans1 = dp[index+1][prevIndex]
            if(prevIndex == 0 or arr[index] > arr[prevIndex-1]):
                ans2 = dp[index+1][index]+1
            dp[index][prevIndex] = max(ans1,ans2)
    print(dp)
    return dp[0][0]

def recursion(index,prevIndex,arr,dp):
    if index == len(arr):
        return 0
    if(dp[index][prevIndex] != -1):
        return dp[index][prevIndex]
    ans1,ans2 = 0,0

    ans1 = recursion(index+1,prevIndex,arr,dp)
    if(prevIndex == -1 or arr[index] > arr[prevIndex]):
        ans2 = recursion(index+1,index,arr,dp)+1
    dp[index][prevIndex] = max(ans1,ans2)
    return dp[index][prevIndex]

def lengthOfLIS(nums):
    n= len(nums)
    dp = [[-1 for i in range(n+1)] for _ in range(n+1)]
    # ans = recursion(0,-1,nums,dp)
    # print(dp)
    # return ans
    return iterativeWay(nums,dp)
# nums = [10,2,5,3,18]
nums = [7,7,7]
print(lengthOfLIS(nums))
        