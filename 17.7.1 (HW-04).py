multipl = 1
for num in range(1, 11):
    if num % 2 == 0:
        continue
    multipl *= num
print("Произведение нечетных чисел от 1 до 10 (при помощи цикла for):", multipl)
print()

multipl = 1
num = 1
while num <= 10:
    if num % 2 != 0:
        multipl *= num
    num += 1
print("Произведение нечетных чисел от 1 до 10 (при помощи цикла while):", multipl)