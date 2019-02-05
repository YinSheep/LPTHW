#This script is a practice for ex13
from sys import argv
# read the WYSS section for how to run this
s, a, b, c, d, e = argv

print(a, "beat", b, "beat", c, "beat", d,
"beat", e)
print("Who beat", a, end = " " )
beatA = input()
print("Who beat", b, end = " " )
beatB = input()
print("Who beat", c, end = " " )
beatC = input()

print(f"{a} beat {b} beat {c} beat {d} beat {e}")
print("{beatA} beat {beatB} beat(beatC)" )
