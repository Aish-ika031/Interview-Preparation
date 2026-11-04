class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        
        res = []
        for i in range(0,len(nums)-1,2):

            res.append(int(str(nums[i])+str(nums[i+1])))

        print(res)

        return min(res)

