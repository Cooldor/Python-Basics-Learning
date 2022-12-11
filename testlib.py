'''
String of documentation.
For example of work with modules and import options.
'''


def raise_to_power(base_num, pow_num):
	'''
	Raise to power function
	Takes 2 random int arguments
	'''
	result = 1
	for index in range(pow_num):
		result = result * base_num
	return result


'''Random variables in modules also could be'''

k = 8
k2 = ['list', 'of', 'strings']
# with this (if) check input function will work only when this file is the main , but never when it will be
# used as module for importing to another file to leave room of variation as a module
if __name__ == '__main__':
	print(raise_to_power((int(input("Base_num: "))), int(input(" Raise to (Pow_num): "))))


