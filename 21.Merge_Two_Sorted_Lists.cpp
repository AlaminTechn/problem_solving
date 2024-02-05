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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1 || !list2) {
            return list1 ? list1 : list2;
        }

        if (list1-> val > list2-> val)
            swap(list1, list2);
        list1->next = mergeTwoLists(list1->next, list2);
        return list1;
    }
};


// With Python

// class Solution:
//   def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
//     if not list1 or not list2:
//       return list1 if list1 else list2
//     if list1.val > list2.val:
//       list1, list2 = list2, list1
//     list1.next = self.mergeTwoLists(list1.next, list2)
//     return list1