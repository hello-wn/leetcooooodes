class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        origin = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        split_nums = {}
        s_list = list(s)
        res, last_char = 0, 0
        while len(s_list):
            # pop the last roman char
            former_char = origin[s_list.pop()]
            if last_char <= former_char:
                res += former_char
            else:
                res -= former_char
            last_char = former_char
        return res

so = Solution()
assert so.romanToInt("III") == 3
assert so.romanToInt("IV") == 4
assert so.romanToInt("IX") == 9
assert so.romanToInt("LVIII") == 58
assert so.romanToInt("MCMXCIV") == 1994
assert so.romanToInt("MCDLXXVI") == 1476

