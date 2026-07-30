class Solution:
    def minimumPushes(self, word: str) -> int:

        cnt = 0
        
        for i in range(len(word)):

            cnt += i//8 + 1

        return cnt
