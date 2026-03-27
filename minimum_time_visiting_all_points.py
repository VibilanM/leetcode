class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        res = 0
        x0, y0 = points.pop()
        while points:
            x1, y1 = points.pop()
            res += max(abs(y1-y0), abs(x1-x0))
            x0, y0 = x1, y1
        return res