import random
cnt = 0
for N in [ 10,100,1000,10000,100000,1000000,10000000 ]:
    cnt = 0
    for i in range(N):
        x = random.uniform(0, 10)
        y = random.uniform(0, 10)
        if x * x + (y-10) * (y-10) >100 and (x-5) *(x-5) + (y-5) *(y-5) < 25 :
            cnt += 1
        s = 200 * cnt / N
    print(s)
