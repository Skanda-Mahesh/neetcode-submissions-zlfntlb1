class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        seen = set()
        for r in s: 
            if r in seen:
                while r in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(r)
            longest = max(len(seen), longest)

        return longest