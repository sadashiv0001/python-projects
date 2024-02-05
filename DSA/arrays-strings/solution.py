"""
Question: Given an array of integers, find two numbers such that they add up to a specific target number.
Optimized Solution: Use a hash table to store the difference between the target and each element. 
Traverse the array and check if the current element's complement is already in the hash table.
"""

def two_sum(nums, target):
    #define an empty dictionary

    complement_dict = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in complement_dict:

            return [complement_dict[complement], i] 
        #or
            retun [nums[complement_dict[complement]], num]
            #  return [(complement_dict[complement], nums[complement_dict[complement]]), (i, num)]
          
        complement_dict[num] = i
    return None

# Example
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1] as indice and actual output as [2,7]