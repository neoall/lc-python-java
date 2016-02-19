/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return helper(l1, l2, 0);
    }
    
    private ListNode helper(ListNode l1, ListNode l2, int carry) {
        if (l1 == null && l2 == null && carry == 0) {
            return null;
        }
        carry += l1 == null ? 0 : l1.val;
        carry += l2 == null ? 0 : l2.val;
        ListNode ret = new ListNode(carry % 10);
        ret.next = helper(l1 == null ? null : l1.next, l2 == null ? null : l2.next, carry / 10);
        return ret;
    }
}
