import os, sys  # unused imports (flake8 F401)

def bad_function(x, y):
    if x > 0:
        if y > 0:
            if x > y:
                print("x bigger")
            else:
                if x == y:
                    print("equal")
                else:
                    print("y bigger")
    else:
        print("x not positive")  # Deep nesting → cyclomatic complexity

def unused_function():  # defined but never used
    return 42
