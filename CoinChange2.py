class Solution:
    def recursion(self,arr,amount,index,dp):
        if index == 0:
            return int(amount % arr[0] == 0)
        if dp[index][amount] != -1:
            return dp[index][amount]
        count2 = self.recursion(arr,amount,index-1,dp)
        count1 = 0
        if(amount-arr[index] >= 0 ):
            count1 = self.recursion(arr,amount-arr[index],index,dp)
        dp[index][amount] = count1+count2
        return dp[index][amount]

    def iterativeWay(self,arr,val,dp):
        n = len(arr)
        for amount in range(val+1):
            dp[0][amount] = int(amount % arr[0] == 0)
            
        for index in range(1,n):
            for amount in range(val+1):
                    count2 = dp[index-1][amount]
                    count1 = 0
                    if(amount-arr[index] >= 0 ):
                        count1 = dp[index][amount-arr[index]]
                    dp[index][amount] = count1+count2
        return dp[n-1][val]        
                



    def change(self, amount: int, coins: List[int]) -> int:
        dp = []
        for i in range(len(coins)):
            l=[]
            for j in range(amount+1):
                l.append(-1)
            dp.append(l)
        return self.iterativeWay(coins,amount,dp)