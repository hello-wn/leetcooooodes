class Solution:
    def countAndSay(self, n: int) -> str:
        res = []
        for string_index in range(n):
            if not string_index:
                res.append('1')
                continue
            prev_char, count = None, 0
            res.append('')
            for char in res[string_index - 1]:
                # for the first char
                if not prev_char:
                    prev_char = char
                    count += 1
                    continue
                if char == prev_char:
                    count += 1
                else:
                    res[string_index] += str(count) + prev_char
                    prev_char, count = char, 1
            res[string_index] += str(count) + prev_char
        return res[n - 1]


so = Solution()
res_list = []
for i in range(1, 11):
    res_list.append(so.countAndSay(i))
assert res_list == ['1', '11', '21', '1211', '111221', '312211', '13112221', '1113213211', '31131211131221', '13211311123113112211'] 


