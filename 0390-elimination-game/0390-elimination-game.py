class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True  # flag to keep track of left-to-right or right-to-left elimination
        remaining = n  # keep track of the remaining numbers
        step = 1  # keep track of the step size
        head = 1  # keep track of the head of the remaining numbers
        while remaining > 1:
            # if we're going from left to right or from right to left with an odd number of remaining elements
            # or from right to left with an even number of remaining elements, then we need to update the head
            if left or remaining % 2 == 1:
                head += step
            step *= 2  # double the step size
            remaining //= 2  # divide the remaining elements by 2
            left = not left  # flip the flag

        return head