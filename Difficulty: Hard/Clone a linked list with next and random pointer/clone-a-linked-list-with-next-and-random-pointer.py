#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.random=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''
class Solution:
    def copyList(self, head):
        # Step 1: Insert copied nodes in between original nodes
        if head is None:
            return head
        
        temp = head
        while temp:
            new_node = Node(temp.data)
            new_node.next = temp.next
            temp.next = new_node
            temp = new_node.next
        
        # Step 2: Assign random pointers to the copied nodes
        temp = head
        while temp:
            if temp.random is None:
                temp.next.random = None
            else:
                temp.next.random = temp.random.next
            temp = temp.next.next
        
        # Step 3: Separate the original and copied lists
        temp = head
        new_head = head.next
        while temp:
            copied_node = temp.next
            temp.next = copied_node.next
            if copied_node.next:
                copied_node.next = copied_node.next.next
            temp = temp.next
        
        return new_head

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None
        self.random = None


class LinkedList:

    def __init__(self):
        self.head = None


def insert(tail, data):
    tail.next = Node(data)
    return tail.next


def setrandom(head, a, b):
    h = head
    i = 1
    while i < a and h:
        h = h.next
        i += 1
    an = h

    h = head
    i = 1
    while i < b and h:
        h = h.next
        i += 1

    if an:
        an.random = h


def validation(head, res):

    headp = head
    resp = res

    d = {}

    while head and res:
        if head == res:
            return
        if head.data != res.data:
            return

        if head.random:
            if not res.random:
                return

            if head.random.data != res.random.data:
                return

        elif res.random:
            return
        if head not in d:
            d[head] = res
        head = head.next
        res = res.next

    if not head and res:
        return
    elif head and not res:
        return

    head = headp
    res = resp
    while head:
        if head == res:
            return
        if head.random:
            if head.random not in d:
                return
            if d[head.random] != res.random:
                return
        head = head.next
        res = res.next

    return True


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        # __n,__m = list(map(int, input().strip().split()))
        __nodes = list(map(int, input().strip().split()))
        __arandom = list(map(int, input().strip().split()))
        __n = len(__nodes)
        __m = len(__arandom)
        __ll = LinkedList()
        __ll2 = LinkedList()
        __ll.head = Node(__nodes[0])
        __ll2.head = Node(__nodes[0])
        __tail = __ll.head
        __tail2 = __ll2.head

        for x in __nodes[1:]:
            __tail = insert(__tail, x)
            __tail2 = insert(__tail2, x)

        for i in range(0, len(__arandom), 2):
            setrandom(__ll.head, __arandom[i], __arandom[i + 1])
            setrandom(__ll2.head, __arandom[i], __arandom[i + 1])

        obj = Solution()
        __res = obj.copyList(__ll.head)
        if validation(__ll.head, __res) and validation(__ll2.head, __res):
            print("true")
        else:
            print("false")

# } Driver Code Ends