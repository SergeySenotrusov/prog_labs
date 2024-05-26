while not (n := input("Enter the number: ")).isdigit() or int(n) <= 0: pass
n = int(n)

while n > 9:
    n = sum(int(digit) for digit in str(n))
print (n)