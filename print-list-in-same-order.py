

numbers = [100,99,98,97,1, 2, 3, 2, 4, 5, 1]
new_numbers = []


for i in range(len(numbers)):
    if numbers[i] != numbers[i+1]:
        new_numbers.append(numbers[i])
    else:
        i += 1
    print(new_numbers)


# unique_numbers = list(set(numbers))
# print(unique_numbers)

# [1,2,3,4,5]
    


# 


