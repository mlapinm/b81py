#b12hello %new username%
import sys
who = 'world' if len(sys.argv) < 2 else sys.argv[1]

print("hello, %s" % who)




