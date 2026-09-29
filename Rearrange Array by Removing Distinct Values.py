from collections import Counter

class Solution:
    def rearrangeArray(self, nums):
        freq = Counter(nums)
        ans = []

        while freq:
            for num in sorted(freq.keys()):
                ans.append(num)
                freq[num] -= 1

                if freq[num] == 0:
                    del freq[num]

        return ans
