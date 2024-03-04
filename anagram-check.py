def anagram_check(str1, str2):
    try:
        # convert the string is having space and make it in lower case
        str1 = str1.replace(" ", "").lower()
        str2 = str2.replace(" ", "").lower()

        # check whether length of the given string is Equal or not 
        if len(str1) != len(str2):
            return False
        
        # sort the string
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)

        return sorted_str1 == sorted_str2
           
    except Exception as e:
        print("Error", e)


str1 = "listen"
str2 = "silent"

result = anagram_check(str1, str2)
if result:
     print("Given strings are anagrams.")
else:
    print("Given strings are not anagrams.")

