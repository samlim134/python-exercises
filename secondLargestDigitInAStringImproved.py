"""
Instead of using hashtable and frequency count to track unique digits, just use sets(no duplicates)

"""
class Solution:
    def secondHighest(self, s:str) -> int:
        lst = list(set(s))
        lst2 = []
        for i in lst:
            if i.isdigit():
                lst2.append(i)
        print(lst2)
        if (len(lst2) < 2): return -1
        else:
            lst2.sort()
            lst2.reverse()
            return lst2[1]

test = Solution()
print(test.secondHighest("ck077"))

#faster than 97% of other submissions