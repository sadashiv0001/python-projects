def min_max_product_of_two(nums):
    if len(nums) < 2:
        raise ValueError("List should contain at least two integers.")

    nums.sort()
    # print(nums[0],nums[1],nums[-1],nums[-2])

    # Product of two smallest numbers and two largest numbers
    min_product = nums[0] * nums[1]
    max_product = nums[-1] * nums[-2]  #since there is no -1 or -2 index hence it will go back to the last index

    return min_product, max_product

# Example usage:
numbers = [4, 2, 7, 5, 3]
min_result, max_result = min_max_product_of_two(numbers)

print(f"The minimum product of two integers is: {numbers[0]} x {numbers[1]} = {min_result}")
print(f"The maximum product of two integers is: {numbers[-2]} x {numbers[-1]} = {max_result}")