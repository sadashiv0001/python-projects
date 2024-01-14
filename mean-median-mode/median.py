# Median

# formula for Even Count Median : [(n/2)th term + (n/2 + 1)th term] /2
# formula for Odd Count Median : [(n/2)th term] /2 (Note: if index starts from zero make it [(n+1/2)th term] /2)

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20, 16, 20, 20, 12, 30, 25, 23]  #odd counting = 17
 
list2 = [12, 16, 12, 30, 25, 23, 24, 16] #even counting = 8 

list1.sort()  #sort it in ascending order
list2.sort() #sort it in ascending order

# method 1 (referring the odd count list)
if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1[len(list1)//2]
print(median)

# method 2 (referring the Even count list)
if len(list2) % 2 == 0:
    m1 = list2[len(list2)//2]
    m2 = list2[len(list2)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1[len(list2)//2]
print(median)