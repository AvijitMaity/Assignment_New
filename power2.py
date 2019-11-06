L = [1]
for i in range(1,7):
	L.append(2**i)
if(2**5 in L):
	print(2**5," found at index",L.index(2**5))
else:
	print("not found")
