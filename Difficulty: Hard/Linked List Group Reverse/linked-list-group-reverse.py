"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        if not head:
            return head

        curr = head
        prev = None
        next_node = None
        count = 0

        # Reverse first k nodes
        while curr and count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1

        # Recursive call for the next part
        if next_node:
            head.next = self.reverseKGroup(next_node, k)

        return prev









#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())  # Number of test cases
    while t > 0:
        llist = LinkedList()

        # Read list values and push them to the LinkedList
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)

        k = int(input())  # Size of the group for reversal
        ob = Solution()
        new_head = ob.reverseKGroup(llist.head, k)
        llist.head = new_head
        llist.printList()  # Print the modified linked list
        t -= 1

        print("~")

# } Driver Code Ends