import json
import functools


def to_json(func):
	"""to json string"""
	@functools.wraps(func)
	def wrapped(*args, **kwargs):
		o = func(*args, **kwargs)
		s = json.dumps(o)
		return s
	return wrapped

@to_json
def get_data():
	return {
		'data': 42
	}


