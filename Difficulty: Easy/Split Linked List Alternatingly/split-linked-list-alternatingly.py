#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        if head is None:
            return [None, None]
        
        # Initialize two lists
        one = Node(head.data)
        if head.next is None:
            return [one, None]
        
        tmpOne = one
        two = Node(head.next.data)
        tmpTwo = two
        head = head.next.next
        
        flag = True
        while head is not None:
            if flag:
                tmpOne.next = Node(head.data)
                tmpOne = tmpOne.next
            else:
                tmpTwo.next = Node(head.data)
                tmpTwo = tmpTwo.next
            head = head.next
            flag = not flag
        
        # Terminate both lists
        tmpOne.next = None
        tmpTwo.next = None
        
        return [one, two]
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends