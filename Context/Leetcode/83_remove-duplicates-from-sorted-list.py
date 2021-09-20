from typing import List
# [Python Logic of ListNode in Leetcode](https://stackoverflow.com/questions/56515975/python-logic-of-listnode-in-leetcode)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

def list_to_LL(arr: List) -> ListNode:
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = head
        while head:
            if head.next:
                next_node = head.next
            else:
                break
            
            if next_node.val == head.val:
                head.next = next_node.next
            else:
                head = next_node
                
        return prev

def main():
    a = Solution()
    print(a.deleteDuplicates(list_to_LL(arr = [1,1,2,3,3])))



if __name__ == "__main__":
    main()