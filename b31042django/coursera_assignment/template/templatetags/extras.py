from atexit import register
from xmlrpc.client import Boolean
from django import template

register = template.Library()

@register.filter(name='inc')
def inc(value, arg):
  return int(value) + int(arg)

@register.simple_tag
def division(a, b, to_int=False):
  if to_int:
    frac = int(int(a) / int(b))
  else:
    frac = int(a) / int(b)
  return frac

