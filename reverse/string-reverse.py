def stringReverse(s):

    try:
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        if not s:
            return s
        else:
            return s[-1] + stringReverse(s[:-1])
    except Exception as e:
        print(f"Error: {e}")


def test_cases():
    test_case = [
        ("hello", "olleh"),
        ("python", "nohtyp"),
        ("world", "dlrow"),
        ("", ""),
        ("a", "a"),
        ("12345", "54321"),
        ("abc123", "321cba"),
    ]

#run tests
    
    for input_str, expected_output in test_case:
        try:
            result = stringReverse(input_str)
            assert result == expected_output, f"Error for input '{input_str}': expected '{expected_output}', got '{result}'"
        except Exception as e:
            print(f"Error for input '{input_str}': {e}")

    print("All tests completed!")
           
        
test_cases()