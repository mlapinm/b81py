import sys


digit_string = "" if len(sys.argv) < 2 else sys.argv[1]

def get_parametr(argv):
	return "" if len(argv) < 2 else argv[1]

def sum_digit(ss):
	""" get sum of sign"""
	sum = 0
	for a in ss:
		if a.isdigit():
			a = int(a)
			sum += a
	return sum			

digit_string = get_parametr(sys.argv)
sum = sum_digit(digit_string)

print(sum)