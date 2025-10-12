class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for n in range(len(nums[i+1::])):
                if(nums[i]+nums[i+n+1]) == target:
                    return [i,i+n+1]  

##test
'''
obj=Solution()
print(obj.twoSum(nums=[3,3],target=6))
'''
