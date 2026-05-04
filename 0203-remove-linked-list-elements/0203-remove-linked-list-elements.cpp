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
    ListNode* removeElements(ListNode* head, int val) {

        ListNode* node1 = new ListNode(0);
        node1->next = head;

        ListNode* prev = node1;
        ListNode* current = head;

        while (current != nullptr) {
            if (current->val == val) {

                prev->next = current->next;

                ListNode* Delete = current;
                current = current->next;
                delete Delete;
            } else {

                prev = current;
                current = current->next;
            }
        }

        ListNode* newhead = node1->next;
        delete node1;

        return newhead;
    }
};