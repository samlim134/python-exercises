"""
1) no repeated elements in the array
2) exactly 1 combination that adds up to target
3) always have 1 combination
"""

def main():
    nums_int = list(map(int, input().strip(' []').split(',')))
    #user will straight away input an integer list already, no need manually use loop to convert it
    target : int = int(input())

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

