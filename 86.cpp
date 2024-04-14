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
    ListNode* partition(ListNode* head, int x) {
        ListNode* less = new ListNode(-1);
        ListNode* Geq = new ListNode(-1);
        
        ListNode* curr_less = less;
        ListNode* curr_geq = Geq;
        ListNode* curr = head;
        while(curr){
            //ListNode* curr_node = new ListNode(curr->val);
            if(curr->val<x){
                curr_less->next = curr;
                curr_less = curr_less->next;
            }
            else{
                curr_geq->next = curr;
                curr_geq = curr_geq->next;
            }
            curr = curr->next;
        }
        curr_geq->next = nullptr;
        curr_less->next = Geq->next;
        /*ListNode* dummy = new ListNode(-1);
        ListNode* PrevLess = dummy;
        ListNode* PrevGre = nullptr;
        dummy->next = head;
        ListNode* curr = head;
        while(curr and PrevGre){
            if(curr->val>=x){
                PrevGre = curr;
            }
            else{
                ListNode* temp = curr->next;
                curr->next = PrevLess->next;
                PrevLess->next = curr;
                PrevGre->next = temp;
            }
        }
        return head;*/
        return less->next;
    }
};