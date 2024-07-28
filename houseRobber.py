class Solution:
    def houseRob(self,n,house,sum):
        if n == -1:
            return sum
        if n < -1:
            return 0
        sum1 = self.houseRob(n-1,house,sum)
        sum2 = self.houseRob(n-2,house,sum+house[n-1])
        return max(sum1,sum2)

    def rob(self, nums: List[int]) -> int:
        return self.houseRob(len(nums)-1,nums,0)