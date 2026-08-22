class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        def cal(n):

            cur_sum , cur_prod = 0 , 1

            while n > 0:

                val = n %10

                cur_sum += val

                cur_prod *= val

                n //= 10

            return cur_sum + cur_prod

        res = cal(n)
        # print(res)

        return False if n % res else True
