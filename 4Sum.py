class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        # print(nums)

        res=set()

        for i in range(0 , len(nums)):

            for j in range(i+1 , len(nums)):

                curr = nums[i] + nums[j]

                low , high = j+1 , len(nums) - 1

                while low < high:

                    if curr + nums[low] + nums[high] == target:

                        res.add((nums[i] , nums[j] , nums[low] , nums[high]))

                        low += 1

                        high -= 1

                    else:

                        diff = target - (curr + nums[low] + nums[high])

                        # print(diff)

                        if diff > 0:

                            low += 1

                        elif diff < 0:

                            high -= 1

        return list(res)
