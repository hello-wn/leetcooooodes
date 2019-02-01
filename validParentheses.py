class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = True
        basic = {'(': ')', '{': '}', '[': ']'}
        index, left = 0, list()
        while index < len(s) and res:
            if s[index] in basic.keys():
                left.append(s[index])
            else:
                if left:
                    inner_left = left.pop()
                    if basic[inner_left] != s[index]:
                        res = False
                else:
                    res = False
            index += 1

        if res and left:
            res = False
        return res


so = Solution()
assert so.isValid('()') == True
assert so.isValid('()[]{}') == True
assert so.isValid('(]') == False
assert so.isValid('([)]')== False
assert so.isValid('{[]}') == True
