def evklid(a, b):
    if b == 0: return a
    else: return evklid(b, a % b)

print (evklid(int(input("Введите первое число: ")), int(input("Введите второе число: "))))