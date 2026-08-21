class Solution:
    def transform(self, s1, s2):
        # If lengths are different, transformation is impossible
        if len(s1) != len(s2):
            return -1
    
        # Check if both strings have same character frequency
        from collections import Counter
        if Counter(s1) != Counter(s2):
            return -1
    
        # Two pointers from the end
        i = len(s1) - 1  # pointer for s1
        j = len(s2) - 1  # pointer for s2
        matched = 0
    
        while i >= 0 and j >= 0:
            if s1[i] == s2[j]:
                matched += 1
                i -= 1
                j -= 1
            else:
                i -= 1
    
        # Minimum operations = length - matched characters
        return len(s1) - matched
            