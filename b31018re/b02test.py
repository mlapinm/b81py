#b02test.py
import re

text= """
x=y+100ecbdfax=y-100adcefby+=10cfdabex-=-101abdecfx-=101febdac
"""
pattern = r"([abc])([+-])?=?([+-])?([abc])?([+-]?\d+)?"
res = re.findall(pattern, text)

text= """
x=y+100ecbdfax=y-100adcefby+=10cfdabex-=-101abdecfx-=101febdac
"""
pattern = r"([abc])([+-])?=([+-])?([abc])?([+-]?\d+)?"
res = re.findall(pattern, text)



print(res)
