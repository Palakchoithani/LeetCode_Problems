class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')

        # best[i] = minimum length of a valid subarray
        # completely inside the first i elements
        best = [INF] * (n + 1)

        # prefix_sum -> latest index
        seen = {0: 0}

        prefix = 0
        answer = INF

        for i, x in enumerate(arr, 1):
            prefix += x

            # Initially, carry forward the previous best
            best[i] = best[i - 1]

            if prefix - target in seen:
                j = seen[prefix - target]
                length = i - j

                # Previous subarray must end at or before j
                if best[j] != INF:
                    answer = min(answer, best[j] + length)

                best[i] = min(best[i], length)

            seen[prefix] = i

        return -1 if answer == INF else answer