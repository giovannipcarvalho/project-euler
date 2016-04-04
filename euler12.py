import time
s=time.time()
n=1
while(True):
    tri = 0
    for x in range(n+1):
       tri += x
    n+=1
    if len([k for k in range(1,tri) if tri%k==0])>500:
        print tri
        break
print s-time.time(), 'segundos'
