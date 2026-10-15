class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        cnt = 0

        for i in range(len(nums)):

            for j in range(i+1, len(nums)):

                res = nums[i:j+1]

                # print(res)

                val = len(set(res))

                cnt += val * val

        return cnt + len(nums)
