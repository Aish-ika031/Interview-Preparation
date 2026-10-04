class Solution:
    def checkValidString(self, s: str) -> bool:
        
        c1 , c2 = 0 , 0

        for i in range(len(s)):

            if s[i] == "(" or s[i] == "*":

                c1 += 1

            else:

                c1 -= 1

            if s[len(s) - i - 1] == ")" or s[len(s) - i - 1] =="*":

                c2 += 1

            else:

                c2 -= 1
        
            if c1 < 0 or c2 < 0:

                return False

        return True
