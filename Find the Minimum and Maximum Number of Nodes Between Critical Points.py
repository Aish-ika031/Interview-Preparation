class Solution:
    def nodesBetweenCriticalPoints(self, head):
        if head is None or head.next is None:
            return [-1, -1]

        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        minDist = float('inf')

        while curr.next:
            nextNode = curr.next

            if ((curr.val > prev.val and curr.val > nextNode.val) or
                (curr.val < prev.val and curr.val < nextNode.val)):

                if first == -1:
                    first = index
                else:
                    minDist = min(minDist, index - last)

                last = index

            prev = curr
            curr = nextNode
            index += 1

        if first == last:
            return [-1, -1]

        maxDist = last - first

        return [minDist, maxDist]
