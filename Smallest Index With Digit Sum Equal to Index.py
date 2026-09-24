class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        def digitsum(n):

            cur = 0

            while n > 0:

                cur += n % 10

                n = n // 10

            return cur

        mn = float("inf")

        for i in range(len(nums)):

            if i == digitsum(nums[i]):

                mn = min(mn , i)

        return mn if mn != float("inf") else -1
