class Solution(object):
    def findDisappearedNumbers(self, nums):
        sol = []
        sn = set(nums)
        for i in range(1, len(nums)+1):
            if i not in sn:
                sol.append(i)
        return sol