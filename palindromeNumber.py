"""
normally palindrome is solved using stacks and queues
stack will reverse the order, queue will main the order
pop() from stack and dequeue() from queue to check 1-by-1 if they are the same
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # initialize a stack
        stack: list = []
        # initiqlize a queue
        queue: list = []

        # for loop to populate the stack and queue
        str_x = str(x)
        for i in str_x:
            stack.append(i)
            queue.append(i)

        #for loop to compare every elements
        for i in range(len(str_x)):
            if (stack.pop() != queue.pop(0)):
                return False
        return True


testing = Solution()
print(testing.isPalindrome(1000021))



