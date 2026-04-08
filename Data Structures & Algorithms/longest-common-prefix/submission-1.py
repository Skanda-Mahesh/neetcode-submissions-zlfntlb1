class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        print(len("") < len("abc"))
        for i in strs:
            if i == "":
                longest = ""
                return longest
            for char in range(len(i)):
                if char < len(longest) and i[char] != longest[char]:
                    longest = longest[:char]
                if len(i) < len(longest):
                    longest = longest[0:len(i)]
                    print(longest)
        return longest