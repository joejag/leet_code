# Given an integer array nums, return an array answer such that answer[i] is equal to the product of
#  all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    result = [1] * len(nums)

    left_side = 1
    for idx, num in enumerate(nums):
        result[idx] = left_side
        left_side = left_side * num

    right_side = 1
    for idx, num in reversed(list(enumerate(nums))):
        result[idx] = result[idx] * right_side
        right_side = right_side * num

    return result


assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
