# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input 
# string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        l = {')': '(', ']':'[', '}': '{'}
        stak = []
        
        for i in s:
            if i in l.values():
                stak.append(i)
            elif i in l:
                if stak == []:
                    return False
                if stak[-1] == l[i]:
                    stak.pop()
                else:
                    return False

        if stak == []:
            return True
        else:
            return False