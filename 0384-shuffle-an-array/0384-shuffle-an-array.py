class Solution:
    def __init__(self, A):
        self.A = A
    def reset(self):
        '''
        Resets the array to its original configuration and return it.
        '''
        return list(self.A)
    def shuffle(self):
        '''
        Returns a random shuffling of the array.
        '''
        A = list(self.A)
        B = []
        while A:
            i           = random.randint( 0 , len(A) - 1 )
            A[i], A[-1] = A[-1], A[i]
            B.append( A.pop() )
        return B