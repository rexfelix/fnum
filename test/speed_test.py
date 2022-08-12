import time
from fnum import fibo, facto


def facto_py(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * facto(n - 1)


def fibo_py(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 1)


def speed_test(count):
    start = time.time()
    for i in range(count):
        n = facto(i)
        print(f"{n}", end=" ")
    end = time.time_ns()
    print(f"\nRust facto = {end - start}\n")

    start = time.time()
    for i in range(count):
        n = facto_py(i)
        print(f"{n}", end=" ")
    end = time.time_ns()
    print(f"\npython facto = {end - start}\n")

    start = time.time()
    for i in range(count):
        n = fibo(i)
        print(f"{n}", end=" ")
    end = time.time_ns()
    print(f"\nRust fibo = {end - start}\n")

    start = time.time()
    for i in range(count):
        n = fibo_py(i)
        print(f"{n}", end=" ")
    end = time.time_ns()
    print(f"\npython fibo = {end - start}\n")


if __name__ == "__main__":
    speed_test(15)
