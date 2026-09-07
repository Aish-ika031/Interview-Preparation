class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        half = n // 2

        total = sum(nums)

        window = sum(nums[:half])

        ans = 0

        for i in range(n):
            if window > total - window:
                ans += 1

            window -= nums[i]
            window += nums[(i + half) % n]

        return ans
