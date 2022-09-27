from typing import List


"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


class Solution:
    # The key of this solution is in use of hash maps such as dictionary or set
    # "in" operator for list has O(n) while hash maps have in average O(1) and worst is O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index_dict = dict()
        for index, num in enumerate(nums):
            the_other_pair = target - num
            if the_other_pair in value_to_index_dict:
                return [value_to_index_dict[the_other_pair], index]
            else:
                value_to_index_dict[num] = index


solution = Solution()

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
print(solution.twoSum([2, 7, 11, 15], 9))

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
print(solution.twoSum([3, 2, 4], 6))


# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
print(solution.twoSum([3, 3], 6))
