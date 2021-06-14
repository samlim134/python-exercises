from typing import List

"""
o(n) solution instead of o(n^2)
Because we use Hashtable for quick lookup.
Loop through the list just 1 time, use hashtable to check if its complement exists in hashtable -> o(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for loop to fill the hashtable
        #key of hashtable: element itself
        #value of hastable: index of the element itself
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i

        #for loop to go through the list
        for i in range(len(nums)):
            complement : int = target - nums[i]
            if (complement in dict and i != dict[complement]):
                #found the combination
                return [i,dict[complement]]

#Improved version runs in 60ms, old version ran 9632ms