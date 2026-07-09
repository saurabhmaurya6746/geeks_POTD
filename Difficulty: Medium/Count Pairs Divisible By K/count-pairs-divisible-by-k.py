class Solution:
    def countKdivPairs(self, arr, k):
        # Remainder frequencies को स्टोर करने के लिए dictionary
        rem_freq = {}
        
        # हर एलिमेंट के रिमाइंडर की फ्रीक्वेंसी काउंट करना
        for num in arr:
            rem = num % k
            rem_freq[rem] = rem_freq.get(rem, 0) + 1
            
        ans = 0
        
        # Case 1: वो नंबर्स जिनका रिमाइंडर 0 है (k से पूरी तरह डिविजिबल हैं)
        # उनके आपस में बनने वाले pairs = n * (n - 1) // 2
        if 0 in rem_freq:
            n = rem_freq[0]
            ans += (n * (n - 1)) // 2
            
        # Case 2: वो नंबर्स जिनका रिमाइंडर k/2 है (अगर k इवन है)
        # उनके आपस में बनने वाले pairs = n * (n - 1) // 2
        if k % 2 == 0 and (k // 2) in rem_freq:
            n = rem_freq[k // 2]
            ans += (n * (n - 1)) // 2
            
        # Case 3: बाकी सारे Remainder pairs (i, k - i)
        # Pairs = freq[i] * freq[k - i]
        # duplicate counting से बचने के लिए i < k // 2 तक ही लूप चलाएंगे
        limit = (k - 1) // 2 if k % 2 == 0 else k // 2
        for i in range(1, limit + 1):
            if i in rem_freq and (k - i) in rem_freq:
                ans += rem_freq[i] * rem_freq[k - i]
                
        return ans