class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        idx = 0

        for i in range(len(nums)):

            if idx == 0 or idx == 1 or nums[idx-2] != nums[i]:

                nums[idx] = nums[i]

                idx += 1

        return idx
