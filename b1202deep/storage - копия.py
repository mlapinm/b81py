import sys

def get_argv(argv):
	e = []

	try:
		if argv[1] == '--key':
			e.append(argv[2])
		if argv[3] == '--val':
			e.append(argv[4])
	except Exception as ex:
		pass
	return e

def get_val(d):
	if len(d) == 0:
		return
	elif len == 1:
		return
	else:

		return


	print(d)

if __name__ == "__main__":
	e = get_argv(sys.argv)
	get_val(e)
	print(e)
