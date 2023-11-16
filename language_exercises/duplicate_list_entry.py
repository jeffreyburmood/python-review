""" this script will return true if a number appears more than once in the list """

nums_duplicate = [1, 2, 5, 6, 2, 1]
nums_no_duplicate = [1, 2, 3, 4, 5, 6]

def anyDuplicates(nums: list) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False

print(anyDuplicates(nums_duplicate))
print(anyDuplicates(nums_no_duplicate))
