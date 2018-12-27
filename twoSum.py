class Solution:

    # Runtime: 6620 ms
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length == 2 and sum(nums) == target:
            return [0, 1]
        elif length > 2:
            first = 0
            for i in range(first, length):
                for j in range(first+1, length):
                    if nums[i] + nums[j] == target:
                        return [i, j]
                first += 1
        return []
    
    # Better Solution
    # Runtime: 372 ms
    def twoSumBetter(self, nums, target):
        another = []
        for index, i in enumerate(nums):
            j = target - i
            if j in another:
                return [another.index(j), index]
            another.append(i)


so = Solution()
nums = [3, 3]
target = 6
res = so.twoSum(nums, target)
res2 = so.twoSumBetter(nums, target)
print(res2)
