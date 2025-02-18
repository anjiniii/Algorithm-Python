"""
#1480. Running Sum of 1D Array
1차원 배열의 누적 합 구하기

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        sum = 0
        for num in nums:
            sum += num
            result.append(sum)
        return result


class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        result.append(nums[0])
        for i in range(1, len(nums)):
            result.append(nums[i] + result[i - 1])
        return result