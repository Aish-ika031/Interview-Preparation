class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        ans = []

        for i in range(1, 10):

            cur = i

            for j in range(i+1 , 10):

                cur = cur *  10 + j

                if low <= cur <= high:

                    ans.append(cur)

        ans.sort()

        return ans
