"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Answer:
	6857
"""
import math
def getfactors(num = 600851475143):
        num2 = int(math.floor(math.sqrt(num)))
        factors = []
        for e in range(num2, 1, -1):
                if num % e == 0:
                        factors += [e]
                        
        return factors

def primefactors(lista):
        primos = []
        for num in lista:
                maxnum = int(math.floor(math.sqrt(num)))
                primo = True
                for x in range(maxnum,1,-1):
                    if num%x==0:
                        primo = False
                        break
                if primo:
                    primos += [num]
        return primos

divisoresprimos = primefactors(getfactors())
print divisoresprimos[0]
