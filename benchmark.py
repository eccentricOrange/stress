from multiprocessing import Pool
from os import system

times = int(input("Enter: "))

def x(i: int):
    print (f"{i:03}")
    system('./benchmark')

Pool().map(x, range(1, times))