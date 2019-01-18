class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        if not strs:
            return res
        str_nums = len(strs)
        if str_nums == 1:
            return strs[0]
        else:
            last_str = strs.pop()
            common = True
            min_length = min([len(each) for each in strs])
            for index in range(1, min_length + 1):
                for each in strs:
                    if last_str[:index] != each[:index]:
                        common = False
                        break
                if common:
                    res = last_str[:index]
                else:
                    break
            return res
    
    # another solution
    def longestCommonPrefix_another(self, strs):
        res = ''
        if not strs:
            return res
        last_str = strs.pop()
        common, i = True, 1
        for i in range(1, len(last_str) + 1):
            for each in strs:
                if not each.startswith(last_str[:i]):
                    common = False
            if not common:
                break
        res = last_str[:i] if common else last_str[:i-1]
        print(i, res)
        return res



so = Solution()
assert so.longestCommonPrefix(["c","acc","ccc"]) == ""
assert so.longestCommonPrefix(["aaa","aa","aaa"]) == "aa"
assert so.longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert so.longestCommonPrefix(["dog","racecar","car"]) == ""
assert so.longestCommonPrefix(["c","c"]) == "c"

