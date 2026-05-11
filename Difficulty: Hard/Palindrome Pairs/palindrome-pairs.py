class Solution:
    def palindromePair(self, arr):
        def is_palindrome(s):
            return s == s[::-1]
        
        word_map = {word[::-1]: idx for idx, word in enumerate(arr)}
        
        for idx, word in enumerate(arr):
            for cut in range(len(word) + 1):
                prefix, suffix = word[:cut], word[cut:]
                
                # Case 1: prefix palindrome, suffix reversed exists
                if is_palindrome(prefix) and suffix in word_map and word_map[suffix] != idx:
                    return True
                # Case 2: suffix palindrome, prefix reversed exists
                if is_palindrome(suffix) and prefix in word_map and word_map[prefix] != idx:
                    return True
        return False