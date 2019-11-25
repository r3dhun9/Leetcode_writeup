class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        celebrity = 0
        for i in range(n):
            if knows(celebrity, i):
                celebrity = i
        for i in range(n):
            if knows(celebrity, i) and celebrity != i: return -1
            if not knows(i, celebrity): return -1
        return celebrity
