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
    int getListSize(ListNode* head) {
        int count = 0;
        while (head) {
            count++;
            head = head->next;
        }
        return count;
    }

    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int l = getListSize(head);
        
        if (n == l) {
            ListNode* newHead = head->next;
            delete head; 
            return newHead;
        }
        ListNode* temp = head;
        for (int i = 0; i < l- n - 1; i++) {
            temp = temp->next;
        }
        ListNode* Deletenode = temp->next;
        temp->next = temp->next->next; 
        
        delete Deletenode;
        
        return head;
    }
};