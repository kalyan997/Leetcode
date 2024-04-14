/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;

        ListNode* prevNode = dummy;
        ListNode* curr = head;
        while(curr and curr->next){
            ListNode* FirstNode = curr;
            ListNode* SecondNode = curr->next;
            
            prevNode->next = SecondNode;
            FirstNode->next = SecondNode->next;
            SecondNode->next = FirstNode;
            
            prevNode = FirstNode;
            curr = FirstNode->next;
        }
        return dummy->next;
    }
};