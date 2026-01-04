nums = [1,2,3,4,5,6,7]
k = 3

def rotate( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        n = nums.pop()
        nums = [n]+ nums
    return nums

print(rotate(nums,k))
