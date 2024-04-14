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
    ListNode* rotateRight(ListNode* head, int k) {
        int LL_Size = 0;
        ListNode* curr = head;
        if(head==nullptr){
            return nullptr;
        }
        while(curr){
            LL_Size++;
            curr = curr->next;
        }
        if(LL_Size==1 || k%LL_Size==0){
            return head;
        }
        k = k%LL_Size;
        cout<<LL_Size<<" "<<k<<"\n";
        int front_size = LL_Size-k;
        cout<<front_size<<"\n";
        curr = head;
        while(curr and front_size){
            front_size--;
            curr = curr->next;
        }
         cout<<front_size<<"\n";
        ListNode* new_head = curr;
        front_size = LL_Size-k;
        curr = head;
        while(curr and front_size>1){
            front_size--;
            curr = curr->next;
        }
        curr->next = nullptr;
        
        curr = new_head;
        while(curr and curr->next){
            curr = curr->next;
        }
        if(curr){
            curr->next = head;
        }
        
        return new_head;
    }
};