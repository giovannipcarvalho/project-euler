"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Answer:
	232792560
"""
##antigo
##n = 20
##while (True):
##    for x in range(1,21):
##        if n%x != 0:
##            break
##    else:
##        print n
##        break
##    n+=20

#novo
n = 20
while (True):
    for x in range(1,21):
        if n%x != 0:
            for j in range(1,21):
                if (n*j) % x == 0:
                    n *= j
                    break
    else:
        break
    n+=20
print n
