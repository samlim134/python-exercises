from typing import List
"""
there can be repeated integers
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = set(nums)
        lst_nums = list(set_nums) #This is a list without any duplicates
        lst_nums.sort(reverse = True)
        if (len(lst_nums) < 3): return lst_nums[0]
        else:
            return lst_nums[2]

#faster than 88% of the community, but this solution is O(n log N) because of TimSort from .sort() method
#list(set()) is O(n)
#This problem can be solved in O(n)
