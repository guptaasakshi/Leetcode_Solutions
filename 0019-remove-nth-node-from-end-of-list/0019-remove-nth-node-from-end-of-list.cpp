class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode* fast = dummy;
        ListNode* slow = dummy;

        // Step 1: fast ko n steps aage le jao
        for (int i = 0; i <= n; i++) {
            fast = fast->next;
        }

        // Step 2: dono move karo
        while (fast != NULL) {
            fast = fast->next;
            slow = slow->next;
        }

        // Step 3: delete node
        ListNode* del = slow->next;
        slow->next = slow->next->next;
        delete del;

        return dummy->next;
    }
};