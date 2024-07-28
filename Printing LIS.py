def PrintLIS(nums):
    n = len(nums)
    dp = [1]*n 
    hashMap = [None]*n
    for i in range(1,n):
        for j in range(0,i):
            if(nums[i] > nums[j] and dp[j]+1 > dp[i]):
                dp[i] = dp[j]+1
                hashMap[i] = j
    maxVal = 1
    maxIndex = n-1
    for i in range(n-1,-1,-1):
        if maxVal < dp[i]:
            maxVal = dp[i]
            maxIndex = i
    ans = []
    while(maxIndex != None):
        ans.append(arr[maxIndex])
        maxIndex = hashMap[maxIndex]
    return ans[::-1]
# arr = [10,9,2,5,3,7,101,18]
# arr = [0,1,0,3,2,3]
arr= [7,7,7,7,7]
print(PrintLIS(arr))