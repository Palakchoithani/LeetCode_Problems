import collections

kFactorCounts = {
    0: collections.Counter(),
    1: collections.Counter(),
    2: collections.Counter([2]),
    3: collections.Counter([3]),
    4: collections.Counter([2, 2]),
    5: collections.Counter([5]),
    6: collections.Counter([2, 3]),
    7: collections.Counter([7]),
    8: collections.Counter([2, 2, 2]),
    9: collections.Counter([3, 3]),
}


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        # Factorize t using only 2, 3, 5, 7
        need, possible = self.getPrimeCount(t)

        if not possible:
            return "-1"

        # Convert required prime factors into digits
        factors = self.getFactorCount(need)

        # If minimum required digits are already more than
        # the length of num, we need a longer answer
        if sum(factors.values()) > len(num):
            return self.construct(factors)

        # Count prime factors in num
        current = collections.Counter()

        for c in num:
            current += kFactorCounts[int(c)]

        # If num has no zero and already satisfies t
        if '0' not in num and all(
            current[p] >= need[p] for p in need
        ):
            return num

        # Position of first zero
        first_zero = num.find('0')

        if first_zero == -1:
            first_zero = len(num)

        # Try changing digits from right to left
        for i in range(len(num) - 1, -1, -1):

            d = int(num[i])

            # Remove current digit's factors
            current -= kFactorCounts[d]

            # Don't keep a prefix containing zero
            if i > first_zero:
                continue

            spaces = len(num) - 1 - i

            # Try making this digit slightly bigger
            for bigger in range(d + 1, 10):

                remaining = (
                    need
                    - current
                    - kFactorCounts[bigger]
                )

                # Negative values become zero
                for p in [2, 3, 5, 7]:
                    if remaining[p] < 0:
                        remaining[p] = 0

                required = self.getFactorCount(remaining)

                required_digits = sum(required.values())

                if required_digits <= spaces:

                    ones = spaces - required_digits

                    return (
                        num[:i]
                        + str(bigger)
                        + '1' * ones
                        + self.construct(required)
                    )

        # No answer of same length.
        # Make answer one digit longer.
        factors = self.getFactorCount(need)

        return (
            '1' * (
                len(num) + 1 - sum(factors.values())
            )
            + self.construct(factors)
        )

    def getPrimeCount(self, t):

        count = collections.Counter()

        for p in [2, 3, 5, 7]:

            while t % p == 0:
                t //= p
                count[p] += 1

        return count, t == 1

    def getFactorCount(self, count):

        # 2^3 = 8
        count8, rem2 = divmod(count[2], 3)

        # 3^2 = 9
        count9, rem3 = divmod(count[3], 2)

        # 2^2 = 4
        count4, count2 = divmod(rem2, 2)

        count6 = 0

        # 2 × 3 = 6
        if count2 == 1 and rem3 == 1:
            count2 = 0
            rem3 = 0
            count6 = 1

        # 4 × 3 = 12 = 2 × 6
        if rem3 == 1 and count4 == 1:
            count2 = 1
            count6 = 1
            rem3 = 0
            count4 = 0

        return {
            2: count2,
            3: rem3,
            4: count4,
            5: count[5],
            6: count6,
            7: count[7],
            8: count8,
            9: count9
        }

    def construct(self, factors):

        result = []

        for digit in range(2, 10):
            result.append(
                str(digit) * factors[digit]
            )

        return ''.join(result)