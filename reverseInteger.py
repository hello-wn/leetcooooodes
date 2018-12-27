class Solution:
    # 84 ms
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        limit = pow(2, 31)
        if x < 0:
            x, positive = -x, False 
        else:
            positive = True
        rev_x = int(str(x)[::-1])
        if positive and rev_x < limit:
            return rev_x
        elif not positive and rev_x <= limit:
            return -rev_x
        else:
            return 0 

    # 120 ms
    def official_reverse(self, x):
        max_value_limit = int((2 ** 31 - 1) / 10)
        min_value_limit = int(- 2 ** 31 / 10)

        rev = 0
        while x != 0:
            pop = x % 10 if x > 0 else x % -10
            x = int(x / 10)
            if rev > max_value_limit or (rev == max_value_limit and pop > 7):
                return 0
            elif rev < min_value_limit or (rev == min_value_limit and pop < -8):
                return 0
            else:
                rev = rev * 10 + pop
        return rev

so = Solution()
for x in [123, -123, 120, 1534236469]:
    # print(so.reverse(x))
    print(so.another_reverse(x))
