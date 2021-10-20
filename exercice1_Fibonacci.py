from multiprocessing import Process
import os
 
def fibonacci(n):
    fib0 = 0
    fib1 = 1
    for i in range(n):
        fib = fib0 + fib1
        print(" fib",i+2,"= ", fib)
        fib0 = fib1
        fib1 = fib
 
if __name__ == "__main__":
    p = Process(target=fibonacci, args = (20,))
    p.start()
    p.join() #fonction de sycnchro Pour que le process Père attende le fils
    print(os.getpid())
    print(os.getppid())