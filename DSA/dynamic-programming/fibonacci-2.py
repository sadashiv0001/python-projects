
# get the nth number from a fibonacci series
#  0,1,1,2,3,5,8,13 

##  method 1 : Dynamic Programming
# in this method Dynamic Programming is implemented 
# Top-Bottom approach (DP + Memoization)
# when n = 4 , o/p = 3, when n = 5  , o/p = 5 and so on...
# time comlexity: O(n) and space comlexity: O(n) + O(n) ~ O(n)


def fibonacci(n, dp={}):

    #base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    

    # check if the result already exists in the memo (maybe already memoized)
    if n not in dp:
        dp[n] = fibonacci(n-1, dp) + fibonacci(n-2, dp)
    return dp[n]

n = int(input("Enter the value of n:"))
print(f"The ({n}) th value in the fibonacci series is:", fibonacci(n))

