#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        # CodeGenius
        if not head or n <= 0:
            return 0

        fast = head
        slow = head
        
        for _ in range(n):
            if fast:
                fast = fast.next
            else:
                return 0  # If n is greater than the number of nodes

        while fast:
            fast = fast.next
            slow = slow.next
        
        total_sum = 0
        while slow:
            total_sum += slow.data
            slow = slow.next
        
        return total_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0])
    for i in range(1, t + 1):
        arr = list(map(int, data[2 * i - 1].split()))
        n = int(data[2 * i])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        ob = Solution()
        print(ob.sumOfLastN_Nodes(head, n))

# } Driver Code Ends