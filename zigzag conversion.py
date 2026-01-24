# https://leetcode.com/problems/zigzag-conversion/submissions/1895095405/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lst = [[] for _ in range(numRows)]
        i = 0 
        d = 1
        for j in s:
            lst[i].append(j)
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d
        ret = ''
        for i in range(numRows):
            ret += ''.join(lst[i])
        return ret
