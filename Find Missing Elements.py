class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        mx , mn = max(nums) , min(nums)

        nums = set(nums)

        ans = [i for i in range(mn , mx + 1) if i not in nums]

        return ans

