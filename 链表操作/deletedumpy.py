# 单链表定义如下：
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def removeDuplicates(self, head):
        """
        :type head: ListNode
        """
        # 在这里编写代码
        if not head or not head.next:
            return head
        head_list = ListNode(None)
        head_list.next = head

        cur = head
        last = head_list
        while cur and cur.next:
            if cur.val != cur.next.val:
                cur = cur.next
                last = last.next
            else:
                val = cur.val
                counts = 2
                while cur and cur.val == val:
                    if counts > 0:
                        cur = cur.next
                        last = last.next
                    else:
                        cur = cur.next
                    counts -= 1
                last.next = cur
        return head_list.next
# def generateListNode(self, item):




if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    head = ListNode(None)
    h1 = head
    for i in nums:
        node = ListNode(i)
        h1.next = node
        h1 = h1.next

    s1 = Solution()
    h3 = s1.removeDuplicates(head.next)
    h3 = h3
    while h3:
        print(h3.val, end=' ')
        h3 = h3.next
