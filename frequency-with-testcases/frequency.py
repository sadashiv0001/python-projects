"""
 to find the frequency of a character in a given string

"""

def char_frequency(input_string, target_string):
    try:
        count = 0
        for char in input_string:
            if char == target_string:
                count += 1
        return count
    
    except Exception as e:
        print("Error:", e)

def run_test_case(test_case, input_string, target_string, expected_output):
    try:
        result = char_frequency(input_string, target_string)
        assert result == expected_output, f"Test Case:{test_case} failed: Expected {expected_output}, for {result}"
        print(f"Test Case:{test_case} passed")
    except AssertionError as ae:
        print("Error:", ae)

# Test Cases
input_string_1 = "Hello, World!"
target_character_1 = 'l'
expected_output_1 = 3

input_string_2 = "Python is fun!"
target_character_2 = 'o'
expected_output_2 = 1

input_string_3 = "Programming"
target_character_3 = 'g'
expected_output_3 = 2

input_string_4 = "Test123Test123"
target_character_4 = 'T'
expected_output_4 = 2

input_string_5 = ""
target_character_5 = 'a'
expected_output_5 = 0

input_string_6 = "aaaaa"
target_character_6 = 'a'
expected_output_6 = 5

input_string_7 = "AbCdEfG"
target_character_7 = 'x'
expected_output_7 = 0

# Add more test cases as needed

# Run Test Cases
run_test_case(1, input_string_1, target_character_1, expected_output_1)
run_test_case(2, input_string_2, target_character_2, expected_output_2)
run_test_case(3, input_string_3, target_character_3, expected_output_3)
run_test_case(4, input_string_4, target_character_4, expected_output_4)
run_test_case(5, input_string_5, target_character_5, expected_output_5)
run_test_case(6, input_string_6, target_character_6, expected_output_6)
run_test_case(7, input_string_7, target_character_7, expected_output_7)



# input_string = "Hello World"
# target_string = "l"
# result = char_frequency(input_string, target_string)
# print(result)
