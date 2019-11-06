'''
 the function takes in three keyword arguments called good, bad, and ugly,
with default values 1, 2, and 3 respectively. now call adder(ugly=1,
good=5). Finally, generalise the function so that it can take an arbitrary numbers of keyword
arguments.
'''
def adder(good=1, bad=2, ugly=3):
    return good + bad + ugly
print(adder(ugly=1, good=5))
