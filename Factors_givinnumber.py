n = int(input("Enter a number: "))
num = n
# factors = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         factors = i
#         print(factors, "is a factor of", num)

# improved version of the above code

# factors = []
# for i in range(1, (num // 2) + 1):
#     if num % i == 0:
#         factors.append(i)
# factors.append(num)
# print("The factors of", num, "are:", factors)

#more optimized version of the above code

from math import sqrt

factors = []
for i in range(1, int(sqrt(num)) + 1):
    if num % i == 0:
        factors.append(i)
        if num // i != i:
            factors.append(num // i)
factors.sort()
print("The factors of", num, "are:", factors)