import random

# Create list of 100 random numbers from 0 to 1000
rand_int = []
n = 100
for i in range(n):
    rand_int.append(random.randint(0, 1000))

# Sort list from min to max (without using sort())
list_len = len(rand_int)
for i in range(0, list_len):
    for j in range(i + 1, list_len):
        if rand_int[i] > rand_int[j]:
            rand_int[i], rand_int[j] = rand_int[j], rand_int[i]

# Calculate average for even and odd
even_num = []
odd_num = []

for num in rand_int:
    if num % 2 == 0:
        even_num.append(num)

for num in rand_int:
    if num % 2 != 0:
        odd_num.append(num)

if even_num:
    even_avg = sum(even_num) / len(even_num)
else:
    even_avg = 0

if odd_num:
    odd_avg = sum(odd_num) / len(odd_num)
else:
    odd_avg = 0

# Print both average result in console
print(f"Average for even numbers: {even_avg}")
print(f"Average for odd numbers: {odd_avg}")
