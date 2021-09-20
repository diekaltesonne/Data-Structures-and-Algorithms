class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr=None
        result=None
        while l1 or l2:
            if l1 and (not l2 or l1.val<l2.val):
                temp=l1
                l1=l1.next
            else:
                temp=l2
                l2=l2.next
            if not ptr:
                ptr=temp
                result=ptr
            else:
                ptr.next=temp
                ptr=ptr.next

        return result
class Solution_not_work:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1
        
        dummy_head = ListNode(0)
        curr = dummy_head
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 or l2
        return dummy_head.next
