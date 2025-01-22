#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
# class Solution:
#     def addTwoLists(self, num1, num2):
#         # code here
# class Node:
#     def __init__(self, data=0, next=None):
#         self.data = data
#         self.next = next

class Solution:
    def reverseList(self, head):
        curr = head
        prev = None
        next_node = curr.next if curr else None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def addTwoLists(self, num1, num2):
        num1 = self.reverseList(num1)
        num2 = self.reverseList(num2)
        carry = 0
        ans = Node(0)
        first = ans
        while num1 or num2 or carry:
            total = carry
            if num1:
                total += num1.data
                num1 = num1.next
            if num2:
                total += num2.data
                num2 = num2.next
            ans.data = total % 10
            carry = total // 10
            if num1 or num2 or carry:
                ans.next = Node(0)
                ans = ans.next
        self.reverseList(first)
        while ans.data == 0 and ans.next:
            ans = ans.next
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):

        arr1 = (int(x) for x in input().split())
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)

        arr2 = (int(x) for x in input().split())
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)

        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
        print("~")

# } Driver Code Ends