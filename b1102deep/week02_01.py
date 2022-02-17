# import sys
import argparse
import json
import tempfile
import os


def get_argv():
	"""return (key, val)"""
	parser = argparse.ArgumentParser()
	parser.add_argument("--key")
	parser.add_argument("--val")
	args = parser.parse_args()
	return (args.key, args.val)

def read_json():
	"""return object"""
	o = {}
	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
	if not os.path.isfile(storage_path):
		return o
	with open(storage_path, "r") as f:
		s = f.read()
		if s:
			o = json.loads(s)
	return o

def write_json(o):
	"""write object"""
	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
	with open(storage_path, "w") as f:
		s = json.dumps(o, sort_keys = True, indent = 2)
		f.write(s)


def get_val(key, val):
	"""change, write object[key] += val to file
	print object[key]"""

	if not key and not val:
		return
	o = read_json()
	if not val:
		items = o.get(key, "")
		items = list( map(lambda a: str(a), items) ) 
		if items:
			ss = ", ".join(items)
			print(ss)
		return

	item =  o.get(key, [])
	item.append(val)
	o[key] = item

	write_json(o)

if __name__ == "__main__":
	key, val = get_argv()
	get_val(key, val)




