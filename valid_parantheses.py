class Solution(object):
    def isValid(self, s):
        l = {')': '(', ']': '[', '}': '{'}
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