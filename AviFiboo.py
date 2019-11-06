#the first ten Fibonacci numbers#
a=0
b=1
print("first 10 fibonacci numbers are:", a,b)
for i in range(8):
    c = a + b
    print(c)
    a = b
    b = c
