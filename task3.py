n= int(input("Enter the range:"))
a=0
b=1
sum=0
count=1
print("Fibonacci series:")
while(count <= n):
    a = b
    b = sum
    sum = a + b
    print(sum, end=" ")
    count += 1

