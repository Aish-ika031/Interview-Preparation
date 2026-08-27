class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        count = Counter(s)
        prefix = []

        for i in range(n):
            if count[target[i]] > 0:
                prefix.append(target[i])
                count[target[i]] -= 1
                continue

            bigger = [c for c in count if c > target[i] and count[c] > 0]

            if bigger:
                c = min(bigger)
                prefix.append(c)
                count[c] -= 1
                return ''.join(prefix) + ''.join(sorted(
                    c for c in count for _ in range(count[c])
                ))

            break

        for i in range(len(prefix) - 1, -1, -1):
            count[prefix[i]] += 1

            bigger = [c for c in count if c > target[i] and count[c] > 0]

            if bigger:
                c = min(bigger)
                count[c] -= 1

                result = prefix[:i] + [c]

                suffix = []
                for ch in sorted(count):
                    suffix.extend([ch] * count[ch])

                return ''.join(result + suffix)

            prefix.pop()

        return ""
