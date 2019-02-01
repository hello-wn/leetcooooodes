# reference links:
# https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).
# https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # initiate the dummy ListNode
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    def convert_list_to_listNode(self, list_: list):
        single_nodes = [ListNode(item) for item in list_]
        for index, node in enumerate(single_nodes):
            if index < len(single_nodes) - 1:
                single_nodes[index].next = single_nodes[index + 1]
        return single_nodes[0]

    def convert_listNode_to_list(self, list_node: ListNode):
        list_ = []
        while list_node:
            list_.append(list_node.val)
            list_node = list_node.next
        return list_


so = Solution()
l1, l2 = [1, 4, 6], [1, 2, 10]
ln1, ln2 = so.convert_list_to_listNode(l1), so.convert_list_to_listNode(l2)
res = so.mergeTwoLists(ln1, ln2)
assert so.convert_listNode_to_list(res) == sorted(l1 + l2)

