from time import perf_counter
from time import sleep


def timer():
    start = perf_counter()
    def inner():
        sleep(5)
        return perf_counter()- start
    return inner
    
a= timer()
print(a())
