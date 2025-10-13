# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def listnode_to_list(node):
            result = []
            while node:
                result.append(node.val)
                node = node.next
            return result
        l1=listnode_to_list(l1)
        l2=listnode_to_list(l2)
        def list_to_listnode(lst):
            dummy = ListNode(0)
            current = dummy
            for val in lst:
                current.next = ListNode(val)
                current = current.next
            return dummy.next

        if len(l1)>len(l2):
            l1,l2=l2,l1

        for i in range(len(l1)):
            l2[i]=l1[i]+l2[i]
        for i in range(len(l2)):
            if l2[i]>9:
                try:
                    l2[i]=l2[i]-10
                    l2[i+1]+=1
                except IndexError:
                    l2.append(1)
        return list_to_listnode(l2)
        
