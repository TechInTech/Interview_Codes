# -*- coding:utf-8 -*-

class LinkNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class CreateLink:
    def __init__(self, lyst):
        self.lyst = lyst
        self.length = len(lyst)

    def get_link(self):
        p = link = LinkNode()
        i = 0
        while i < self.length:
            node = LinkNode(self.lyst[i])
            p.next = node
            p = p.next
            i += 1
        # p = link.next
        # while p:
        #     val = p.val
        #     print(val)
        #     p = p.next
        return link.next

def Copy_Nodes(links):
    new_link = p = LinkNode()

    while links:
        node = LinkNode(links.val)
        p.next = node
        p = p.next
        links = links.next
    return new_link.next

if __name__ == "__main__":
    lyst = list(range(10))

    link = CreateLink(lyst)
    linkNode = link.get_link()
    copy_node = Copy_Nodes(linkNode)
    while copy_node:
        print("Copy: ",copy_node.val)
        copy_node = copy_node.next
