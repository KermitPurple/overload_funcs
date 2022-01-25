#!/usr/bin/env python3
from overload import overload

@overload
def f(a: int, b: int) -> int:
    return a + b

@f.load
def f(a: float, b: float) -> float:
    return a - b

@f.load
def f(a: str, b: int) -> str:
    return a * b

def main():
    '''Driver Code'''

    print(f(1, 2))
    print(f(10.0, 2.5))
    print(f("Hi! ", 10))

if __name__ == '__main__':
    main()

