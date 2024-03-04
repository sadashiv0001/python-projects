# def first_non_repeating_character(s):
#     fi = [-1] * 256

#     # Sets all repeating characters to -2 and non-repeating characters
#     # contain the index where they occur
#     for i in range(len(s)):
#         if fi[ord(s[i])] == -1:
#             fi[ord(s[i])] = i
#         else:
#             fi[ord(s[i])] = -2

#     res = float('inf')

#     for i in range(256):
#         # If this character is not -1 or -2 then it
#         # means that this character occurred only once
#         # so find the min index of all characters that
#         # occur only once, that's our first index
#         if fi[i] >= 0:
#             res = min(res, fi[i])

#     # If res remains infinity, it means there are no
#     # characters that repeat only once or the string is empty
#     if res == float('inf'):
#         return -1
#     else:
#         return res


# string_input = "aadddfrfggtreee"
# first_index = first_non_repeating_character(string_input)

# if first_index == -1:
#     print("Either all characters are repeating or the string is empty")
# else:
#     print("First non-repeating character is " + str(string_input[first_index]))
def first_non_repeating_character(s):
   char_frequency ={}

   for char in s:
    char_frequency[char] = char_frequency.get(char, 0) + 1
    
    for i in range (len(s)):
        if char_frequency[s[i]] == 1:
            return i
    return -1




# Example usage:
input_str = "aasdddfreertyt"
result = first_non_repeating_character(input_str)

if result != -1:
    print(f"The first non-repeating character is '{input_str[result]}' at index {result}.")
else:
    print("Either all characters are repeating or the string is empty.")



# # Test cases
# test_cases = [
#     {
#         "input": "abacddbec",
#         "expected": "e"
#     },
#     {
#         "input": "aabbaccddbeec",
#         "expected": "NONE"
#     },
#     {
#         "input": "1234",
#         "expected": "Characters only"
#     },
#     {
#         "input": "aabbc",
#         "expected": "NONE"
#     },
#     {
#         "input": "",
#         "expected": "NONE"
#     },
#     {
#         "input": "aabcc",
#         "expected": "b"
#     },
#     {
#         "input": "aabbcc",
#         "expected": "NONE"
#     },
# ]

# # Function to run test cases
# def run_test_cases():
#     for test_case in test_cases:
#         input_str = test_case["input"]
#         expected_output = test_case["expected"]
#         result = optimized_first_non_repeat_char(input_str)
#         assert result == expected_output, f"For input '{input_str}', expected '{expected_output}', but got '{result}'"
#     print("All test cases passed!")

# # Run the test cases
# run_test_cases()
