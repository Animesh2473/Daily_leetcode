1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        d = {}
4        for num in nums:
5            if num in d:
6                return True
7            d[num] = True
8        return False