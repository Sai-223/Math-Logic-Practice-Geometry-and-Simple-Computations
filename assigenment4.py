n = int(input("Enter how many Fibonacci numbers: "))
fib = []
a, b = 0, 1
while len(fib) < n:
    fib.append(a)
    a, b = b, a + b
print(fib)

limit = int(input("Enter the limit for the sum of primes: "))
total = 0
for num in range(2, limit):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if not is_prime:
        continue
    total = total + num
print(total)

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = list(map(int, input("Enter row " + str(i + 1) + ": ").split()))
    matrix.append(row)
transposed = []
for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transposed.append(new_row)
print(transposed)

height = int(input("Enter the triangle height: "))
lines = []
for i in range(1, height + 1):
    lines.append(" " * (height - i) + "*" * i)
print(lines)
for line in lines:
    print(line)

items = list(map(int, input("Enter numbers separated by spaces: ").split()))
counts = {}
duplicates = set()
for item in items:
    if item in counts:
        counts[item] = counts[item] + 1
    else:
        counts[item] = 1
    if counts[item] > 1:
        duplicates.add(item)
print(duplicates)