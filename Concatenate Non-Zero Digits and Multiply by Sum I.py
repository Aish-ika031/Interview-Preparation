class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        n = list(str(n))

        cur = 0

        res = ""

        for i in n :

            if i != '0':

                res = res + i

                cur += int(i)

            print(res)

        val = int("".join(res) or "0") * cur
        return val
