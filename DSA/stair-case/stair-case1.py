def countStairs(n, steps):
    # here steps is the number of steps we are going to jump
    # n = number of stairs
    # either we can jump 1 stairs or we can jump 2 stairs at a time
    # hence if we are given number of steps as "steps", we can add both the steps wrt n
    # formula: f(n) = f(n+1) + n(n+2)
    # time complexity = O(n) and space complexity O(1)
    
    if steps == n:
        return 1
    # elif steps == 0:
    #     return 0
    elif steps > n:
        return 0
    
    return countStairs(n, (steps+1)) + countStairs(n, (steps+2))


def wayToClimb(n):
    result = countStairs(n, 0)
    return result

n = int(input("Enter the number of stairs you want to:"))
print(f"Number of ways to climb ({n})stairs are:", wayToClimb(n))