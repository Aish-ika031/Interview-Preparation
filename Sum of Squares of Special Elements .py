class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        n = len(nums)

        cur = 0
        
        for i in range(len(nums)):

            val = n % (i+1)

            if val == 0:

                cur += pow(nums[i] , 2)

        return cur
