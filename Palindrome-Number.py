# Time to complete: 17:38 (got caught up in a silly approach trying to reverse up to the midpoint instead of the entire converted string)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
