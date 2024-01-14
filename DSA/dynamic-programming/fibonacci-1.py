
# get the nth number from a fibonacci series
#  0,1,1,2,3,5,8,13 

##  method 1
# in this method simple recursion is implemented
# when n = 4 , o/p = 3, when n = 5  , o/p = 5 and so on...
# time comlexity: O(n) and space comlexity: O(n)

def fibonacci(n):
# base case
    if n == 1:
        return 1  

    elif n == 0:
        return 0
    else:
        n = fibonacci(n-1) + fibonacci(n-2)
        return n

n = int(input("Enter the value of n: "))
print(f"Fibonacci({n}) =", fibonacci(n))







