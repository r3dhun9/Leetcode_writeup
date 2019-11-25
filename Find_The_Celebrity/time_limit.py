class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        know_list = [ 0 for x in range(n)]
        for i in range(n):
            for j in range(n):
                if knows(i,j): know_list[j] += 1
        for i in range(n):
            count = 0
            if know_list[i] == n:
                for j in range(n):
                    if knows(i,j) == 1: count += 1
                if count == 1: return i                   
        return -1
