"""
Congratulations, the answer you gave to problem 10 is correct.

You are the 102812th person to have solved this problem.

Answer: 142913828922
"""

import time, math
comeco = time.time()
n = 2000000
res = 0
for x in range(n, 1, -1):
    maxn = int(math.floor(math.sqrt(x)))
    for k in range(maxn, 1, -1):
        if x%k==0:
            break
    else:
        res+=x
print res
print time.time()-comeco, 'segundos'
