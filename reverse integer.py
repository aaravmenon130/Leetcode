#https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        flag = 0
        
        if x < 0:
            flag = 1
            x = x * -1
        dup = x
        lower_limit = (-2)**31
        upper_limit = (2**31) - 1

        while dup != 0:    
            rem = dup % 10
            res = res * 10 + rem
            dup = dup // 10
            if res < lower_limit or res > upper_limit:
                return 0

        if flag == 1:
            return res * -1
        return res
