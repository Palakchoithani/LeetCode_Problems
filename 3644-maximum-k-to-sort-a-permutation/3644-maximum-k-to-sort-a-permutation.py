class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        ans = -1

        for i, num in enumerate(nums):
            if i != num:
                ans &= num

        return max(ans, 0)