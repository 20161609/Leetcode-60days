# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        front, rear = 1, n
        if guess(front) == 0:
            return front
        elif guess(rear) == 0:
            return rear
        else:
            while True:
                mid = (front+rear)//2
                g = guess(mid)
                if g < 0:
                    rear = mid
                elif g > 0:
                    front = mid                    
                else:
                    return mid
                
        return 0