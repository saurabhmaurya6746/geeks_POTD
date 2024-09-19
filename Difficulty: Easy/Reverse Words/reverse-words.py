# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
      def reverseWords(self, s: str) -> str:
        words = s.split('.')  # Split the string by '.'
        reversed_words = words[::-1]  # Reverse the list of words
        return '.'.join(reversed_words)  # Join the reversed words with '.'


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends