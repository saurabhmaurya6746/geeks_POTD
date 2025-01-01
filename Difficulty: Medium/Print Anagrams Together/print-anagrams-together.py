#User function Template for python3


class Solution:

    def anagrams(self, arr):
        '''
        words: list of words
        return: list of groups of anagrams
        '''
        from collections import defaultdict

        # Dictionary to group words by their sorted character tuple
        anagram_map = defaultdict(list)

        for word in arr:
            # Sort the word to form the key
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        # Extract the groups in order of appearance in input
        result = list(anagram_map.values())
        
        return result

 
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends