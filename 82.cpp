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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* prev = dummy;
        ListNode* curr = head;
        while(curr){
            if(!curr->next){
                prev = prev->next;
                curr = curr->next;
                //continue;
            }
            else if(curr->next and curr->next->val != curr->val){
                prev = prev->next;
                curr = curr->next;
                //continue;
            }
            else{
                while(curr->next and curr->next->val == curr->val){
                    curr = curr->next;
                }
                
                 prev->next = curr->next;
                //prev = curr;
                curr = curr->next;
            }
            
        }
        return dummy->next;
    }
};