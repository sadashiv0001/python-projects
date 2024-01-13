def findMissingNumber(n):
    numbers = set(n)
    size = len(numbers)

    # create an empty conatainer to store the missing numbers
    result = []

    #iterate through the input list and find the number and if number is not prepsent already, 
    # store it in the result container
    for i in range(1, n[-1]):
        if i not in numbers:
            result.append(i)
    return result


listNumberInput = [1,2,3,5,7,9,10,11,12,13,17,18,19,20,22,25]
print (findMissingNumber(listNumberInput))