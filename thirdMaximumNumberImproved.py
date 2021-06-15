from typing import List
"""
This improved version should avoid doing sorting at all, .sort() -> O(nlogn)
Because we want to achieve o(n)

1) set up a list of size 3, containing 1st,2nd and 3rd largest integer
2) Initialize them to negative infinity
3) linear loop through the given list of integers, any integer bigger than the ones in the list of size 3 replace
them
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # remove duplicates
        lst_nums = list(set(nums))  # O(n)
        # a list of size 3
        lst = [float('-inf')] * 3  # O(1)
        # loop through lst_nums O(n)
        for i in lst_nums:
            # if i is the biggest
            if (i > lst[2]):
                lst[0] = lst[1]
                lst[1] = lst[2]
                lst[2] = i
            # if i bigger the 2nd but smaller than 1st
            elif (i > lst[1]):
                lst = [lst[1], i, lst[2]]  # Alternate shorter way of writing compared to the first if
            # if i is bigger than the smallest
            elif (i > lst[0]):
                lst[0] = i
        # lst_nums[0] is smallest , lst_nums[2] is biggest
        return lst[0] if lst[0] != float('-inf') else lst[2]