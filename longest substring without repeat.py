#https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1892976834/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        j = 0
        n = len(s)
        max_len = 0
        s2 = set()
        while j != n and i != n:
            if s[j] not in s2:
                s2.add(s[j])
                j += 1
            else:
                while s[j] in s2:
                    s2.remove(s[i])
                    i += 1
            max_len = max(max_len, j - i)
        return max_len
