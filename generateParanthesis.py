def iterativeWay(n,dp):
    dp[n][n] = [""]
    for i in range(n-1,-1,-1):
        dp[n][i] = [")"*(n-i)]
    for open in range(n-1,-1,-1):
        for close in range(n,-1,-1):
            ans = []
            if(open<n):
                lst1 =  dp[open+1][close]
                for i in lst1:
                    ans.append("("+i)
            if(open>close):
                lst2 = dp[open][close+1]
                for i in lst2:
                    ans.append(")"+i)
            dp[open][close] = ans
    return dp[0][0]




def recursion(open,close,n,dp):
    if(open == n and close == n):
        return [""]
    print(open,close)
    if(dp[open][close] != -1):
        return dp[open][close]
    ans = []
    if(open<n):
        lst1 =  recursion(open+1,close,n,dp)
        for i in lst1:
            ans.append("("+i)
    if(open>close):
        lst2 = recursion(open,close+1,n,dp)
        for i in lst2:
            ans.append(")"+i)
    dp[open][close] = ans
    print("for the function f(",open,close,") the value is ",ans)
    return ans
n = 3
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
# print(recursion(0,0,n,dp))
print(iterativeWay(n,dp))