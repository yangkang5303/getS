import random
import time

def get_s(loop_time):
    cnt = 0
    for _ in range(loop_time):
        x = random.uniform(0, 10)
        y = random.uniform(0, 10)
        
        x_square = x * x
        y_minus_10_square = (y - 10) * (y - 10)
        x_minus_5_square = (x - 5) * (x - 5)
        y_minus_5_square = (y - 5) * (y - 5)

        if x_square + y_minus_10_square > 100 and x_minus_5_square + y_minus_5_square < 25:
            cnt += 1
            
    s = 200 * cnt / loop_time
    print(s)

for N in [10, 100, 1000, 10000, 100000, 1000000]:
    start_time = time.perf_counter()
    get_s(N)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Time elapsed for {N}: {elapsed_time:.6f} seconds")

