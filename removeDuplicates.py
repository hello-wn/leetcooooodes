# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# In-place algorithm updates input sequence only through replacement or swapping of elements.


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ordered_index = 0
        if not nums:
            return ordered_index 
        for index, num in enumerate(nums):
           if not index:
               # when index == 0
               last_num = num
           else:
               if num > last_num:
                   ordered_index += 1
                   if ordered_index != index:
                       nums[ordered_index], nums[index] = num, nums[ordered_index]
                   last_num = num
               else:
                   continue
        return ordered_index + 1


so = Solution()
nums = [1, 2, 2, 3, 4]
res = so.removeDuplicates(nums)
assert res == 4
assert nums[:res] == [1, 2, 3, 4]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
res = so.removeDuplicates(nums)
assert res == 5
assert nums[:res] == [0, 1, 2, 3, 4]


