while not (n := input("Enter the altitude: ")).isdigit() or int(n) <= 0: pass
[print(' ' * (int(n) - i - 1) + '*' * (2 * i + 1)) for i in range(int(n))]