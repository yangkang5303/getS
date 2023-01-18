import random
import time

def get_s(loop_time):
    cnt = 0
    for i in range(loop_time):
        x = random.uniform(0, 10)
        y = random.uniform(0, 10)
        
        if x * x + (y-10) * (y-10) >100 and (x-5) *(x-5) + (y-5) *(y-5) < 25 :
            cnt += 1
            # print(cnt)
        s = 200 * cnt / loop_time
    print(s)

for N in [ 10,100,1000,10000,100000,1000000 ]:
    start_time = time.perf_counter()
    get_s(N)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Time elapsed: ", elapsed_time)
