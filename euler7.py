"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Answer:
	104743
"""
primos = [2,3]
x=4
while (len(primos) != 10001):
    for p in primos:
        if x%p==0:
            break
    else:
        primos+=[x]
    x+=1
print primos[-1]
