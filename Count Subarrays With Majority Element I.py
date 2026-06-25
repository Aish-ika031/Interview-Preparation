class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        
        cnt = 0 

        for i in range(len(nums)):

            res = 0

            for j in range(i , len(nums)):

                if nums[j] == target:

                    res +=1 

                else:

                    res -= 1

                if res > 0:

                    cnt += 1

        return cnt
