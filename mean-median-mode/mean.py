def mean(x):
    sumOfList = sum(x)
    size = len(x)
    result = sumOfList / size

    return result

x = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
result = mean(x)
print(result)