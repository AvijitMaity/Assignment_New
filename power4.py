L=[1,2,4,8,16,32,64]
X=5
for k in L:
    if 2 ** X == k:
        print('at index', L.index(k))
        break
else:
    print(X, 'not found')