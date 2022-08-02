# First Solution
def containsDuplicate(nums: list[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True

# Second Solution
def containsDuplicate2(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

print(containsDuplicate([1, 2, 3, 1]))

print(containsDuplicate2([1, 2, 3, 1]))