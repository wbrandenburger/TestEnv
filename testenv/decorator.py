from typing import Callable

def decorator(x: Callable):
    print(f"Input of function 'decorator' has type {type(x)}")
    print(f"Call input:")
    a = x("decorator")
    return x # Return value has to be callable

@decorator
def funct_with_decorator(client):
    print(f"Function with decorator and client {client} says: 'Hi'")
    return "Return Nothing"

if __name__ == '__main__': 
    funct_with_decorator("main")