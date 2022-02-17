import sys

def get_parametr(argv):
	responce = [0, 0, 0]
	print(argv)
	for i, e in zip(range(len(argv)), argv):
		if 0 < i < 4:
			try:
				responce[i-1] = float(e)
			except:
				responce[i-1] = 0
	return (responce)

def test (a, b, c, x):
	print(a*x*x + b*x + c)

def decision(a, b, c):
	if a == 0:
		print("{} {} {} This is not quadratic equation".format(a, b, c))
		return
	d = b**2 - 4*a*c
	if d < 0:
		print("{} {} {} no roots".format(a, b, c))
		return
	x1 = (-b - pow(d, 1/2) ) / (2 * a)
	x2 = (-b + pow(d, 1/2) ) / (2 * a)
	print(int(x2))
	print(int(x1))

if __name__ == "__main__":
	a, b, c = get_parametr(sys.argv)
	decision(a, b, c)

