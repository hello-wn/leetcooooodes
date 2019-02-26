class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif needle not in haystack:
            return -1
        else:
            needle_len = len(needle)
            for i in range(len(haystack)):
                if needle == haystack[i: i + needle_len]:
                    return i


so = Solution()
index = so.strStr('hello', 'll')
assert index == 2

index = so.strStr('wonderful', 'fucccc')
assert index == -1

index = so.strStr('wininin', '')
assert index == 0

