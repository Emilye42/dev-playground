#nums=[1,2,3,4]
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        leftmost =0
        for i,num in enumerate(nums):
            leftmost+=num     

            leftmost1 = leftmost - num
            rightmost1 = total - num -leftmost1
            if leftmost1 == rightmost1:
                        return i

        return -1
            

