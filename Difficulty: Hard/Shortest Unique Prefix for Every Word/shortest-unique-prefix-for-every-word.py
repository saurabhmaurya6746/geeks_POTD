class Solution:
    def findPrefixes(self, arr):
        # Trie node structure
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.freq = 0
        
        # Build Trie
        root = TrieNode()
        
        # Insert all strings into Trie
        for word in arr:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                node.freq += 1
        
        # Find unique prefix for each string
        result = []
        for word in arr:
            node = root
            prefix = ""
            for ch in word:
                node = node.children[ch]
                prefix += ch
                # If this node has frequency 1, it means only this string 
                # passes through this path, so we found the unique prefix
                if node.freq == 1:
                    break
            result.append(prefix)
        
        return result