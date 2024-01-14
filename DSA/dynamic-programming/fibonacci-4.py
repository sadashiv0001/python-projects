
# get the nth number from a fibonacci series
#  0,1,1,2,3,5,8,13 

##  method 1 : Dynamic Programming
# in this method Dynamic Programming is implemented 
# Space Optimization without memoization
# when n = 4 , o/p = 3, when n = 5  , o/p = 5 and so on...
# time comlexity: O(n) and space comlexity: O(1)

def fibonacci(n):
    prev1 = n-1
    prev2 = n-2
    current = prev1 + prev2

    for i in range(2,n-1):
        prev2 = prev1
        current = prev2
    return current


n = int(input("Enter the number of n:"))
print(f"Fibonacci({n}) = ", fibonacci(n))