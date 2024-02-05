"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
 
Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
"""

"""

if start < end:
  # increment from the second digit
  # 1, 1+1, 1+1+1
else:
# decrement the first digit also
# 




"""
"""
first method
"""

def sequential_digits(low, high):
    result = []
    for digit in range(1, 9):  # Start from 1 to avoid leading zeros
        num = digit
        next_digit = digit + 1

        while num <= high and next_digit <= 9:
            if num >= low:
                result.append(num)

            num = num * 10 + next_digit
            next_digit += 1

    return sorted(result)

# Example 1
low1, high1 = 100, 300
print(sequential_digits(low1, high1))  # Output: [123, 234]

# Example 2
low2, high2 = 1000, 13000
print(sequential_digits(low2, high2))  # Output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]

"""
second method
"""
def sequential_digits(low, high):
    result = []
    for digit in range(1,9):
      num = digit
      next_digit = digit + 1

      while num <= high and next_digit <= 9:
          if num >= low:
              result.append(num)
          num = num * 10  + next_digit
          next_digit += 1

          if num > high:
              break
    return sorted(result)

# Example 1
low1, high1 = 100, 300
print(sequential_digits(low1, high1))  # Output: [123, 234]

# Example 2
low2, high2 = 1000, 13000
print(sequential_digits(low2, high2))  # Output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]



