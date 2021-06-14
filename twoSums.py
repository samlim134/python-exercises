from typing import List #for python 3.9 and above, no need to import this anymore
"""
1) no repeated elements in the array
2) exactly 1 combination that adds up to target
3) always have 1 combination
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #O(n^2) algorithm
        hasFound : bool = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (j == i):
                    pass #skip
                elif (nums[i] + nums[j] == target):
                    hasFound = True
                    return [i,j]
                    break
            if hasFound:
                break

