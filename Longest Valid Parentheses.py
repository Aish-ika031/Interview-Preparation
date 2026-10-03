class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        cnt = 0

        st = [-1]

        for i in range(len(s)):

            if s[i] == "(":

                st.append(i)

            else:

                if len(st) > 0:

                    st.pop()

                    if len(st) == 0:

                        st.append(i)

                    else:

                        cnt = max(cnt , i - st[-1])

        return cnt
