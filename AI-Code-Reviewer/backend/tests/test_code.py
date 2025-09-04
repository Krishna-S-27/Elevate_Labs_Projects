import os
import sys


def bad_function():
    x = 1
    y = 2
    if x < y:
        print("x is less")
        if y > 0:
            if x == 1:
                print("nested too deep!")
    else:
        print("x is greater")


def another_func(a, b, c):
    if a > 10:
        if b < 5:
            if c == 0:
                print("bad nesting again")
    else:
        print("compressed if-else")
