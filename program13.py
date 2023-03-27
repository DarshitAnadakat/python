num_list = []

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        num_list.append(num)

print("Numbers between 2000 and 3200 (both included) that are divisible by 7 but not a multiple of 5:")
print(num_list)