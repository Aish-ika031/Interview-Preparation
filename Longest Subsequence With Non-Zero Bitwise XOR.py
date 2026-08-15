class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        cur = 0

        status = True

        for i in range(len(nums)):

            cur = cur ^ nums[i]

            if cur > 0:

                status = False

        if cur > 0:

            return len(nums)

        if not status:

            return len(nums) - 1

        else:

            return 0
