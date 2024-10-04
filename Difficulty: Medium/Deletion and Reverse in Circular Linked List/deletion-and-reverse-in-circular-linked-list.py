#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        if head is None or head.next == head:
            return head

        prev = None
        curr = head
        next_node = None

        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

            if curr == head:
                break

        head.next = prev
        head = prev
        return head
        
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        if head is None:
            return None

        # If the node to be deleted is the head node
        if head.data == key:
            # If the list has only one node
            if head.next == head:
                return None

            # Find the last node
            last = head
            while last.next != head:
                last = last.next

            # Point the last node to the next of head node
            last.next = head.next
            head = head.next
            return head

        # For non-head nodes
        prev = None
        curr = head
        while curr.next != head:
            if curr.data == key:
                prev.next = curr.next
                return head
            prev = curr
            curr = curr.next

        return head
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if head is None:
        print("empty")
        return

    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        key = int(input())

        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        tail.next = head  # Make the list circular

        ob = Solution()
        head = ob.deleteNode(head, key)
        head = ob.reverse(head)
        printList(head)

# } Driver Code Ends