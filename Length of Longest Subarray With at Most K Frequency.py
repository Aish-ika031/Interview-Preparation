class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        st = -1

        mp = Counter()

        res =0

        for i in range(len(nums)):

            mp[nums[i]] += 1

            while mp[nums[i]] > k:

                st += 1

                mp[nums[st]] -= 1

            res = max(res , i - st)

        return res
