# Mode is the most frequently occurring value among all the values.
list1 = [12,25,25,67,87, 16, 20, 20, 20, 12, 34, 30, 25, 23, 24, 20, 21,25,25,25,25,25,25,25,25]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(mode)