import sys

def get_parametr(argv):
	num = 0
	text = "" if len(argv) < 2 else argv[1]
	if text.isdigit():
		num = int(text)
	return num

def print_stairs(val):
	for i in range(1, val + 1):
		s = ""
		for k in range(val - i):
			s += r' '
		for k in range(i):
			s += r'#'
		print(s)

num = get_parametr(sys.argv)
print_stairs(num)
