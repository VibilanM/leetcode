# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait 
# after the ith day to get a warmer temperature. If there is no future day for which this is possible, 
# keep answer[i] == 0 instead.

class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev = stack.pop()
                answer[prev] = i - prev
            
            stack.append(i)

        return answer