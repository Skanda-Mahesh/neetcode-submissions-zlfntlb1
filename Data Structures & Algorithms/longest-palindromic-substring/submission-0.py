class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isp(val):
            if val == val[::-1]:
                return True
            return False

        
        ans = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and isp(s[l:r+1]):
                if (r-l+1) > len(ans):
                    ans = s[l:r+1]
                    print(ans)
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < len(s) and isp(s[l:r+1]):
                if (r-l+1) > len(ans):
                    print(ans)
                    ans = s[l:r+1]
                l -= 1
                r += 1
            
        return ans



        
