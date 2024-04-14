# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            preHead = ListNode(-1)
            prev = preHead
            if list1 == None:
                return list2
            elif list2 == None:
                return list1
            else:
                while list1!=None and list2!=None:
                    if list1.val<=list2.val:
                        prev.next = list1
                        list1 = list1.next
                    else:
                        prev.next = list2
                        list2 = list2.next
                    prev = prev.next
                if list1==None:
                    prev.next = list2
                else:
                    prev.next = list1
            return preHead.next
        
        amount = len(lists)
        interval = 1
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1)<len(lists) else None
                mergedLists.append(mergeTwoLists(list1, list2))
            lists = mergedLists

        return lists[0] if amount > 0 else None