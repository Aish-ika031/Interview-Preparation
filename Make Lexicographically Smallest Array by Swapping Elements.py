class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        arr = sorted((num, i) for i, num in enumerate(nums))

        ans = nums[:]
        i = 0

        while i < n:
            j = i

            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            values = [arr[k][0] for k in range(i, j + 1)]

            indices = sorted(arr[k][1] for k in range(i, j + 1))

            for idx, value in zip(indices, values):
                ans[idx] = value

            i = j + 1

        return ans
