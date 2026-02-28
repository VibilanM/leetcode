class Solution(object):
    def twoSum(self, nums, target):
        mapp = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapp:
                return [mapp[diff], i]
            mapp[n] = i
        return