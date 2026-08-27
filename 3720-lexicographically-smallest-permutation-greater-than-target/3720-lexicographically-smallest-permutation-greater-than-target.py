class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        n = len(s)
        ans = []

        # Try to make prefix equal to target
        for i in range(n):
            x = ord(target[i]) - ord('a')

            if cnt[x] > 0:
                cnt[x] -= 1
                ans.append(target[i])
            else:
                # Cannot match target[i].
                # Try the smallest character > target[i].
                for c in range(x + 1, 26):
                    if cnt[c] > 0:
                        cnt[c] -= 1

                        return ''.join(ans) + chr(c + ord('a')) + ''.join(
                            chr(j + ord('a')) * cnt[j]
                            for j in range(26)
                        )

                # No larger character possible here,
                # so we must backtrack.
                break

        # Backtrack and increase an earlier character
        for i in range(len(ans) - 1, -1, -1):
            old = ord(ans[i]) - ord('a')
            cnt[old] += 1

            target_char = ord(target[i]) - ord('a')

            for c in range(target_char + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    return (
                        ''.join(ans[:i])
                        + chr(c + ord('a'))
                        + ''.join(
                            chr(j + ord('a')) * cnt[j]
                            for j in range(26)
                        )
                    )

        return ""