class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        ans = 0

        for i in range(n // 2):
            ans -= nums[i] * nums[i]
            ans += nums[n - 1 - i] * nums[n - 1 - i]

        if n % 2:
            ans += nums[n // 2] * nums[n // 2]

        return ans
