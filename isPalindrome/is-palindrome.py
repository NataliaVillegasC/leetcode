class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        sol = True
        while left <= right:
            if not s[left].isalpha():
                left += 1
                continue
            if not s[right].isalpha():
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return sol


print(Solution().isPalindrome("No lemon, no melon"))