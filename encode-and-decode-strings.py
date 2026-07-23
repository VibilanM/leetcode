# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

class Solution:

    def encode(self, strs):
        enc = ""
        for i in strs:
            enc += str(len(i)) + "#" + i

        return enc
        

    def decode(self, s):
        dec = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            try:
                n = int(s[i:j])
            except:
                pass
            
            dec.append(s[j+1:j+n+1])
            i = j + n + 1
        
        return dec
