class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []

        for word in words:
            total_weight = 0

            for ch in word:
                total_weight += weights[ord(ch) - ord('a')]

            rem = total_weight % 26
            
            result.append(chr(ord('z') - rem))

        return ''.join(result)
