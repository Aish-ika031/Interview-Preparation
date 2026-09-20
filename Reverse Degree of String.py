class Solution:
    def reverseDegree(self, s: str) -> int:

        s= list(s)

        val = 0
        
        for i in range(len(s)):

            val += (122 - ord(s[i]) + 1) * (i+1)

        return val
