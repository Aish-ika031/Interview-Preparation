class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        res = []

        st = -1
        
        d = dict(knowledge)

        for i in range(len(s)):

            if s[i] == "(":

                st = i

            elif s[i] == ")":

                cur = s[st+1 : i]

                st = -1

                if cur in d:

                    res.append(d[cur])

                else:

                    res.append("?")

            elif st < 0:
                
                res.append(s[i])

        return "".join(res)
