#https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = defaultdict(int)
        for i in range(n):
            if target - nums[i] not in d:
                if nums[i] in d:
                    continue
                else:
                    d[nums[i]] = i
            else:
                return [i, d[target - nums[i]]]
