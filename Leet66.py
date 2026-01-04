class Solution(object):
    def __init__(self, digits):
        self.digits = digits
    def plusOne(self):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        length_d = len(self.digits)
        if length_d == 1:
            return self.digits+1
        sum = 0
        for i in range(length_d):
            sum+=10**(length_d-i-1)*self.digits[i]
        sum+=1
        li = []
        for i in str(sum):
            li.append(int(i))
        return li
'''
digits = [1,2,3,4]
lend=len(digits)
sum=0
for i in range(lend):
            sum+=10**(lend-i-1)*digits[i]
            print(sum)

print(sum)'''
digits = [1,2,3,4]
digits = Solution(digits)
print(digits.plusOne())
