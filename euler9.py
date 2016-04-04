"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Answer:
	31875000
"""
import math
for x in range(1,1001):
        a = x
        for k in range(x,1001):
                b = k
                c = int(math.sqrt(a**2 + b**2))
                if a**2 + b**2 == c**2:
                        if a+b+c == 1000:
                                print a,b,c
                                print a*b*c
                                break
