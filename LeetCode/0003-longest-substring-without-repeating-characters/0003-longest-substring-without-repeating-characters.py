class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {}
        start = 0
        result = 0

        for i in range(len(s)):
            if s[i] in index and index[s[i]] >= start:
                start = index[s[i]] + 1

            index[s[i]] = i
            result = max(result, i - start + 1)

        return result