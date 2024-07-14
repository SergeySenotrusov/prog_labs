def ways(n):
    if n == 0: return 1
    elif n == 1: return 1
    else: return ways(n - 1) + ways(n - 2)

print(ways(int(input("Enter the number of steps: "))))