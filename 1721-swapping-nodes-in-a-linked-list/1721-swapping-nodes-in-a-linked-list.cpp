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
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode *left = head, *right = head, *curr = head;

        for (int i = 1; i < k; i++) {
            curr = curr->next;
        }
        left = curr; 
        ListNode* temp = curr; 
        while (temp->next != nullptr) {
            temp = temp->next;
            right = right->next;
        }
        int Swap = left->val;
        left->val = right->val;
        right->val = Swap;

        return head;
    }
};