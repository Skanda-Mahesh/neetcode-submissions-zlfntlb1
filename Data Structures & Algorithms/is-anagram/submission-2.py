class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if hashmap_s.get(s[i]):
                hashmap_s[s[i]] = hashmap_s.get(s[i]) + 1
            else: 
                hashmap_s[s[i]] = 1

            if hashmap_t.get(t[i]):
                hashmap_t[t[i]] = hashmap_t.get(t[i]) + 1
            else: 
                hashmap_t[t[i]] = 1

            
        if hashmap_s == hashmap_t:
            return True
        else:
            return False