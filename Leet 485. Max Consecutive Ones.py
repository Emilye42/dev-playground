class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        consecutive = [0]
        n = 0
        for i in nums:
            if i ==1 :
                consecutive[n]+=1
            else:
                n+=1
                consecutive.append(0)
        return max(consecutive)
