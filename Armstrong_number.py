n = int(input("Enter a number: "))
num = n
total = 0

length = len(str(n))
while(num > 0):
    ld = num % 10
    total = (total +(ld ** length))
    num = num // 10
if total == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")