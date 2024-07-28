def frogJumpWithK(n,heights,k):
    if n == 0:
        return 0
    minVal = float('inf')
    for i in range(1,k+1):
        if n-i>=0:
            minVal = min(frogJumpWithK(n-i,heights,k)+abs(heights[n] - heights[n-i]),minVal)
    return minVal
    
n,k = map(int,input().split())
heights = list(map(int,input().split()))
print(frogJumpWithK(n-1,heights,k))
