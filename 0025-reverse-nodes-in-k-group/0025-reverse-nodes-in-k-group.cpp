class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head;

        ListNode dummy(0);
        dummy.next = head;
        ListNode* prevGroup = &dummy;

        while (true) {
            ListNode* kth = prevGroup;

            // find kth node
            for (int i = 0; i < k && kth; i++) {
                kth = kth->next;
            }

            if (!kth) break;

            ListNode* groupNext = kth->next;
            ListNode* prev = groupNext;
            ListNode* curr = prevGroup->next;

            // reverse k nodes
            while (curr != groupNext) {
                ListNode* temp = curr->next;
                curr->next = prev;
                prev = curr;
                curr = temp;
            }

            // reconnect
            ListNode* temp = prevGroup->next;
            prevGroup->next = kth;
            prevGroup = temp;
        }

        return dummy.next;
    }
};