#https://leetcode.com/problems/integer-to-roman/submissions/1904122376/

class Solution:
    def intToRoman(self, num: int) -> str:
        d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5,'V'), (4, 'IV'), (1, 'I')]
        res = []
        for val, symb in d:
            if num == 0:
                break
            count = num // val
            res.append(symb * count)
            num -= count * val
        return ''.join(res)
