from multiprocessing import Pool
from os import system

times = int(input("Enter: "))

def x(i: int):
    print (f"{i:03}")
    system('./collatz')

times = 1000
Pool().map(x, range(1, times))