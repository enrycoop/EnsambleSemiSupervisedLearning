"""
Some function utilities.
"""
import numpy as np


def avg(l):
    return np.array(l).mean()


def geo_avg(l):
    prod = 1
    for i in l:
        prod *= i
    return pow(prod, division(1, len(l)))


def harm_avg(l):
    prod = 0
    for i in l:
        prod += 1/i
    return division(len(l)/prod)


def division(x, y):
    try:
        return x / y
    except:
        return 0
