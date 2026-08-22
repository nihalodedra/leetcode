class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        L =0
        temp = head
        while temp is not None:
            L+=1
            temp = temp.next
        if L == n:
            new_head = head.next
            del head
            return new_head

        Node_prev = L-n
        temp = head
        count = 1
        while count < Node_prev:
            temp = temp.next
            count +=1
        temp.next = temp.next.next
        return head


     
