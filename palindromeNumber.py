class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            res = 0
            former, remainder = x // 10, x % 10
            res = res * 10 + remainder
            while former:
                former, remainder = former // 10, former % 10
                res = res * 10 + remainder
            return True if res == x else False


so = Solution()
assert so.isPalindrome(10) == False
assert so.isPalindrome(121) == True
assert so.isPalindrome(-121) == False
