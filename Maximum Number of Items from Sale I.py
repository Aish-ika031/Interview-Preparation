
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        factors = [x[0] for x in items]
        prices = [x[1] for x in items]
        min_price = min(prices)
        ans = 0

        for mask in range(1 << n):
            cost = 0
            purchased = 0
            selected = []

            for i in range(n):
                if mask & (1 << i):
                    cost += prices[i]

                    if cost > budget:
                        break

                    purchased += 1
                    selected.append(i)

            else:
                free = 0

                for i in selected:
                    for j in range(n):
                        if i != j and factors[j] % factors[i] == 0:
                            free += 1

                remaining = budget - cost
                extra = remaining // min_price

                ans = max(ans, purchased + free + extra)

        return ans
