# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# In-place algorithm updates input sequence only through replacement or swapping of elements.


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ordered_index = 0
        for index, num in enumerate(nums):
            if num != val:
                if ordered_index != index:
                    nums[ordered_index], nums[index] = nums[index], nums[ordered_index]
                ordered_index += 1
        return ordered_index 


so = Solution()
nums = [3, 2, 2, 3]
res = so.removeElement(nums, 3)
assert res == 2 
assert nums[:res] == [2, 2]

nums = [0, 1, 2, 2, 3, 0, 4, 2] 
res = so.removeElement(nums, 2)
assert res == 5
assert nums[:res] == [0, 1, 3, 0, 4]

