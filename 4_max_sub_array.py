# Given an integer array nums, find the subarray which has the largest sum and return its sum.
from typing import List


def maxSubArray(nums: List[int]) -> int:
    currentSum = 0
    maxSum = nums[0]

    for num in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += num
        maxSum = max(maxSum, currentSum)

    return maxSum


assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert maxSubArray([1]) == 1
assert maxSubArray([5, 4, -1, 7, 8]) == 23
