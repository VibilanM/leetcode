# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

# Return the minimum number of operations to make all elements of nums divisible by 3.

class Solution(object):
    def minimumOperations(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] % 3 != 0:
                count += 1
        return count