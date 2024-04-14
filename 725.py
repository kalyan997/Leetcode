# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        num_nodes = 0
        curr = head

        while curr:
            num_nodes += 1
            curr = curr.next
        
        print(num_nodes)

        min_group_count = num_nodes//k
        max_group_count = ceil(num_nodes/k)

        if num_nodes%k == 0:
            min_group_count = max_group_count

        curr_groups = 0
        extra_groups = num_nodes % k
        res = []
        curr = head

        while extra_groups > 0:
            curr_group_count = 0
            curr_group_head = ListNode()
            curr_group = curr_group_head
            while curr_group_count < max_group_count:
                curr_group.next = ListNode(curr.val)
                curr_group = curr_group.next
                prev = curr
                curr = curr.next
                curr_group_count += 1
            prev.next = None
            extra_groups -= 1
            curr_groups += 1
            res.append(curr_group_head.next)

        prev =  ListNode()
        while curr_groups < k:
            curr_group_count = 0
            curr_group_head = ListNode()
            curr_group = curr_group_head
            while curr_group_count < min_group_count:
                curr_group.next = ListNode(curr.val)
                curr_group = curr_group.next
                prev = curr
                curr = curr.next
                curr_group_count += 1
            prev.next = None
            curr_groups += 1
            res.append(curr_group_head.next)

        return res