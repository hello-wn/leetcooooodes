class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        for stone in S:
            if stone in J:
                res += 1
        return res

so = Solution()
J, S = "aA", "aAAbbbb"
assert so.numJewelsInStones(J, S) == 3
J, S = "b", "BB"
assert so.numJewelsInStones(J, S) == 0 
