"""
extract and append all the [U N I Q U E]numerical digits into a list
if length of list <2, return -1
else, reverse order the list and list[1] is the solution

To find only the unique digits, use a hashtable to track frequency
"""
class Solution:
    def secondHighest(self, s:str) -> int:
        res : int = -1
        dict = {}
        lst = []
        for i in range(len(s)):
            elem = s[i]
            if (elem.isnumeric()):
                #if in dictionary
                if (elem in dict):
                    dict[elem] += 1
                #if not in dictionary
                else:
                    dict[elem] = 1
                    lst.append(int(elem))
        lst.sort()
        lst.reverse()
        print(lst)
        if (len(lst) < 2):
            return res
        else:
            res = lst[1]
            return res


test = Solution()
print(test.secondHighest(input()))

#Accepted, ran faster than 89% of the people
