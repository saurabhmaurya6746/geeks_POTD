#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    
    # Function to perform inorder traversal and store the result in a list.
    def inorder(self, root, res):
        if root is None:
            return
        self.inorder(root.left, res)
        res.append(root.data)
        self.inorder(root.right, res)

    # Function to merge two sorted lists.
    def mergeSortedArrays(self, list1, list2):
        mergedList = []
        i, j = 0, 0
        n1, n2 = len(list1), len(list2)

        # Merging two sorted lists.
        while i < n1 and j < n2:
            if list1[i] <= list2[j]:
                mergedList.append(list1[i])
                i += 1
            else:
                mergedList.append(list2[j])
                j += 1

        # Append the remaining elements.
        while i < n1:
            mergedList.append(list1[i])
            i += 1
        while j < n2:
            mergedList.append(list2[j])
            j += 1

        return mergedList

    # Function to return a list of integers denoting the node values of both the BSTs in a sorted order.
    def merge(self, root1, root2):
        # Lists to store inorder traversals of both BSTs.
        list1, list2 = [], []
        
        # Perform inorder traversals of both trees.
        self.inorder(root1, list1)
        self.inorder(root2, list2)
        
        # Merge the two sorted lists.
        return self.mergeSortedArrays(list1, list2)


#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == 'N':
        return None
    
    # Creating list of strings from input string after splitting by space
    ip = s.split()
    
    # Create the root of the tree
    root = Node(int(ip[0]))
    
    # Push the root to the queue
    queue = [root]
    
    # Starting from the second element
    i = 1
    while queue and i < len(ip):
        # Get and remove the front of the queue
        currNode = queue.pop(0)
        
        # Get the current node's value from the string
        currVal = ip[i]
        
        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.left)
        
        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]
        
        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.right)
        i += 1
    
    return root



def main():
    t = int(input())
    for _ in range(t):
        s = input()
        root1 = buildTree(s)
        s = input()
        root2 = buildTree(s)
        obj = Solution()
        vec = obj.merge(root1, root2)
        print(" ".join(map(str, vec)))

if __name__ == "__main__":
    main()

# } Driver Code Ends