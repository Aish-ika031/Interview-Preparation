from collections import defaultdict

class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)

        ones1 = []
        ones2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    ones1.append((i, j))
                if img2[i][j]:
                    ones2.append((i, j))

        count = defaultdict(int)
        ans = 0

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                shift = (x2 - x1, y2 - y1)
                count[shift] += 1
                ans = max(ans, count[shift])

        return ans
