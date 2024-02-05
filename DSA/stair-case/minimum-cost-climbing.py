# number of stairs are given
# each step has some cost defined
# if user jumps to the next step, the cost will be added
# find the wasy which has minimum cost


def number_of_ways(cost):
    steps = len(cost)

    prev1 = 0
    prev2 = 1
    current = prev1 + prev2

    print(current)
 
    # for i in range(2, steps):
  
    #     # minCost = min(current[i], current[i + 1])
    # return 1

cost = [10, 15, 20]
print("Enter cost array:")
print(f"The ways haing minimum cost is:", number_of_ways(cost))
    
