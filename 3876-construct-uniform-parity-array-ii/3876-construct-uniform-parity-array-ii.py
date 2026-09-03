class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        min_odd = float('inf')

        # Find the smallest odd number
        for x in nums1:
            if x % 2 == 1:
                min_odd = min(min_odd, x)

        # If there is no odd number,
        # all numbers are already even.
        if min_odd == float('inf'):
            return True

        # Every even number must be >= smallest odd number.
        # Otherwise it cannot be changed into an odd number.
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False

        return True