
# get the nth number from a fibonacci series
#  0,1,1,2,3,5,8,13 

##  method 1 : Dynamic Programming
# in this method Dynamic Programming is implemented 
# Bottom Up approach (Tabulation Method)
# when n = 4 , o/p = 3, when n = 5  , o/p = 5 and so on...
# time comlexity: O(n) and space comlexity: O(n)

def fibonacci(n):
    dp={}
    dp[1] = 1
    dp[0] = 0
    
    for i in range(2,n-1):
       dp[i] = dp[i-1] + dp[i-2]
    return dp[i]


n = int(input("Enter the number of n:"))
print(f"Fibonacci({n}) = ", fibonacci(n))