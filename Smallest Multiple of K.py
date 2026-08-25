class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        vis = set(nums)

        res = k

        while res in vis:

            res += k

        return res
