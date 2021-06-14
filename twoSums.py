"""
1) no repeated elements in the array
2) exactly 1 combination that adds up to target
3) always have 1 combination
"""

def main():
    nums_str : list = input().split()
    nums_int : list = [None]*len(nums_str)
    target : int = int(input())

    #to create a list of integers from user
    for i in range(len(nums_str)):
        nums_int[i] = int(nums_str[i])

    #O(n^2) algorithm
    hasFound : bool = False
    for i in range(len(nums_int)):
        for j in range(len(nums_int)):
            if (j == i):
                pass #skip
            elif (nums_int[i] + nums_int[j] == target):
                hasFound = True
                print([i,j])
                break
        if hasFound:
            break


if __name__ == "__main__":
    main()

