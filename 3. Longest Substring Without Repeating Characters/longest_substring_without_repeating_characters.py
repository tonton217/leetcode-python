class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        result = 0
        charIndex = {}
        for j in range(len(s)):
            if (s[j] in charIndex):
                i = max(charIndex[s[j]], i)
            result = max(result, j - i + 1)
            charIndex[s[j]] = j + 1
        return result

if __name__ == "__main__":
    s = "abcabcbb"
    result = Solution().lengthOfLongestSubstring(s)

    print(result)
