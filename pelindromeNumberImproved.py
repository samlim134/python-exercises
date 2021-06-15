"""
Problem is solvable wihtout stack and queue
The challenge is to solve without converting the integer to string
Solving without string will mean we have to consider negative also

__Algorithm__
1) Since we are not using strings, we can compare between original and reverted integers
2_ However, assuming int_max is 1234, and original integer is 1099, the reverted integers can be 9901, overflow
3) To prevent overflowing, only revert half the integers, compare this half reverted integers with the remaining
original integers
4) To revert integers, modulus %10 will retrieve last digit, to add this last digit to first digit, multiply *10.
Everytime we add a last digit to first digit, keep multiplying by 10
5) To know we have reached the half way point, since we always remove 1 digit from original integer, and we always
adding 1 digit to reverted integer, when original integer < reverted integer, we reached half way
6) It doesn't matter if original integer is odd or even, even if it is odd, it will not matter palindrome. Because
the middle element will not matter
Eg. 12321, after the algorithm, original integer = 12, reverted integer = 123, we simply remove last digit of reverted
integer, compare the original with the remaining
"""
class Solution:
    def isPalindrome(self,x :int) -> bool:
        #reverted integer
        z : int = 0
        #make a copy of original integer to manipulate
        y : int = x

        #Has to consider edge case, like x = 10, x = 100, anything that ends with 0, things like 1002, 10000012 still ok
        #Also, as long as the integer is negative, it won't be palindrome at all
        #This hasn't stepped into the while loop, hence this if statement is checking the entire original integer,
        #whether the last digit is 0 or not
        if (y < 0 or (y%10==0 and y!=0) ):
            return False
        #revert half the integer
        while (y > z): #not half-way yet
            z += y%10
            z *= 10
            y //= 10
        #first time breaking out of the loop z will have 1 additional 0, remove it
        z //= 10

        #check if z has 1 more digit than y
        if (z>y):
            z//=10
        elif (y>z):
            y//=10
        #compare for polindrome
        return z==y

