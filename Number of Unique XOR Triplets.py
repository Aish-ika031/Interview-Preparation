from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()

        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    seen.add(nums[i] ^ nums[j] ^ nums[k])

        return len(seen)
