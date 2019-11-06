# Function for nth fibonacci number - Space Optimisataion
# Taking 1st two fibonacci numbers as 0 and 1
import timeit as t
def fibonacci(n):
    a=0
    b=1
    print("first",n, "fibonacci numbers are:", '\n',a,'\n', b)
    for i in range(n-2):
        c = a + b
        print(c)
        a = b
        b = c
fibonacci(100)
print("time taken by the program to run= " ,t.timeit())