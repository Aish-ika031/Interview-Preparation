class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        diff = 0
        q = 0

        for i, ch in enumerate(num):
            if ch == '?':
                q += 1 if i < n // 2 else -1
            else:
                diff += int(ch) if i < n // 2 else -int(ch)

        return diff * 2 != -9 * q
