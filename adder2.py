'''
the adder function to add an arbitrary number of arguments.
'''
def adder(*args):
	s = args[0]
	for i in range(1,len(args)):
		s = s+args[i]
	return s
print(adder("1","2","3","4","5","6","7"))
