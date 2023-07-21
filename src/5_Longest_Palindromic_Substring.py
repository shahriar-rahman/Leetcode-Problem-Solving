# Runtime 707ms
# Memory 16.55mb

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, res_length = "", 0
        for i in range(len(s)):
            res, res_length = palindrome(i, i, s, res, res_length)
            res, res_length = palindrome(i, i+1, s, res, res_length)
        return res


def palindrome(left, right, string, res, res_length): 
    while left >= 0 and right < len(string) and string[left] == string[right]:
        if (right - left + 1) > res_length:
            res = string[left:right+1]
            res_length = right - left + 1
        left -= 1
        right += 1
    return [res, res_length]