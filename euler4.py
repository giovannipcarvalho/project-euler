"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer:
	906609 
"""
n1 = 100

def palindromo(num):
    num = str(num)
    x=len(num)-1
    num2=""
    while (x>=0):
        num2+=num[x]
        x-=1
    return num2 == num

palindromos = []
    
while (n1 <= 999):
    n2 = n1
    while (n2 <= 999):
        #print n1, "x", n2
        n2+=1
        res = n1 * n2
        if palindromo(res):
            palindromos+=[res]
    n1+=1

def maiorlista(lista):
    maior = lista[0]
    for x in lista:
        if x > maior:
            maior = x
    return maior

print maiorlista(palindromos)
