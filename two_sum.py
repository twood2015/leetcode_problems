# First Solution
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        value = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == value:
                return [i, j]

print(twoSum([2,7,11,15], 9))