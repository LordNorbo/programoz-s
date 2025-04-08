def MyFunc():
    print("Hello!")

MyFunc()

def greet(name):
    print(f"Hello, {name}!")
greet("John")
 


def fib(n):
    a, b=0, 1
    while a<n:
        print(a, end=" ")
        a, b= b, a+b
    print()

fib(2000)
print(fib(2000))

def fib2(n):
    result=[]
    a, b = 0, 1
    while a< n:
        result.append(a)
        a, b = b, a+b
    return result

f100=fib2(100)
print(f100)



def ask_ok(prompt, retries=4, reminder="Please try again!"):
    """Ask OK"""
    while True:
        reply= input(prompt)
        if reply in {"y","ye","yes"}:
            return True
        if reply in {"n","no","nop","nope"}:
            return False
        retries=retries-1
        if retries<0:
            raise ValueError("invalid user response")
        print(reminder)

ask_ok("Doy you really want to quit?")
ask_ok("OK to overwrite the file?", 2)
ask_ok("OK to overwrite the file?",2,"Come on, only yes or no!")


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))












