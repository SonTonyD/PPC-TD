from multiprocessing import Process
 
def fibonacci():

    fib0 = 0
    fib1 = 1
    for i in range(7):
        fib = fib0 + fib1
        print("Pour n = ",i, " fib = ", fib)
        fib0 = fib1
        fib1 = fib
        
 
if __name__ == "__main__":
    p = Process(target=fibonacci)
    p.start()
    p.join()