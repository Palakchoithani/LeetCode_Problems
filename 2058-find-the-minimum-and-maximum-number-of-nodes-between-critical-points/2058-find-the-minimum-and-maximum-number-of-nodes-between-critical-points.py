class Solution:
    def nodesBetweenCriticalPoints(self, head):
        positions = []

        prev = head
        curr = head.next
        pos = 1

        while curr and curr.next:
            if (prev.val < curr.val > curr.next.val) or \
               (prev.val > curr.val < curr.next.val):
                positions.append(pos)

            prev = curr
            curr = curr.next
            pos += 1

        if len(positions) < 2:
            return [-1, -1]

        min_dist = float('inf')

        for i in range(1, len(positions)):
            min_dist = min(
                min_dist,
                positions[i] - positions[i - 1]
            )

        max_dist = positions[-1] - positions[0]

        return [min_dist, max_dist]