from os import *
from sys import *
from collections import *
from math import *
def iterative(weight,value,capacity,n,dp):
    for i in range(1,n+1):
        for j in range(0,capacity+1):
            profit1 = dp[i-1][j]
            profit2 = 0
            if j-weight[i-1] >= 0:
                profit2 = dp[i-1][j-weight[i-1]]+value[i-1]
            dp[i][j] = max(profit1,profit2)
    return dp[n][capacity]

def recursion(weight,value,capacity,n,dp):
    if capacity <= 0 or n <0:
        return 0
    if dp[n][capacity] != -1:
        return dp[n][capacity]
    profit1 = recursion(weight,value,capacity,n-1,dp)
    profit2 = 0
    if capacity-weight[n] >= 0:
        profit2 = recursion(weight,value,capacity-weight[n],n-1,dp)+value[n]
    dp[n][capacity] = max(profit2,profit1)
    return dp[n][capacity]

for _ in range(int(input())):
    n = int(input())
    weight = list(map(int,input().split()))
    value = list(map(int,input().split()))
    capacity = int(input())
    dp = []
    for i in range(n+1):
        l=[]
        for i in range(capacity+1):
            l.append(0)
        dp.append(l)
    print(iterative(weight,value,capacity,n,dp))