asd="asd"

def func1():
    a=1
    print(a)
    try:
        print(b)
    except NameError:
        print("b is not defined")

def func2():
    b=2
    print(b)
    try:
        print(a)
    except NameError:
        print("a is not defined")


func1()
func2()

try:
    print(a)
    print(b)
except NameError:
    print("a and b are not defined")

a,b=3,4

print(a)
print(b)

def outer_func():
    x=10
    def inner_func():
        nonlocal x
        print(x)
        x=11
        print(x)
    inner_func()

outer_func()

try:
    print(x)
except NameError:
    print("x is not defined")

x=11
print(f"1 - main x: {x}")

def outer_func2():
    x=15
    print(f"nonlocal - x in outer_func: {x}")
    def inner_func():
        x=25
        print(f"nonlocal inner_func - x in outer_func after inner_func: {x}")
    inner_func()
    print(f"nonlocal x in outer_func after inner_func: {x}")

outer_func2()
print(f"2 - main x: {x}")

def outer_func3():
    x=150
    print(f"global - x in outer_func after inner_func: {x}")
    def inner_func():
        global x
        x=250
        print(f"global_inner_func - x in outer_func after inner_func: {x}")
    inner_func()
    print(f"global - x in outer_func after inner_func: {x}")

outer_func3()

print(f"3 - main x: {x}")

x="xyz"
print(f"4 - main x: {x}")

import math

print(math.e)
e=10
print(e)

import random

def create_account(accounts):
    account_number=input("Banszámla száma: ")
    account_holder=input("Számla tulajdonosa: ")
    if account_number in accounts:
        print("Ez a számla már létezik")
    else:
        accounts[account_number] = {"Tulajdonos": account_holder,"Egyenleg":0}
        print("A számla sikeresen létrehozva!")

def remove_account(accounts):
    account_number=input("Bankszámla száma: ")
    if account_number in accounts:
        del accounts[account_number]
        print("A bankszámla sikeresen törölve")
    else:
        print("A számla nem található")
    
def update_account_holder(accounts):
    account_number = input("Bankszámla száma: ")
    if account_number in accounts:
        new_holder = input("Számla új tulajdonosa:  ")
        accounts[account_number]["holder"] = new_holder
        print("Számla tulajdonos neve sikeresen megváltozott!")
    else:
        print("A számla nem található")

def list_accounts(accounts):
    if accounts:
        print("\nSzámlák listája: ")
        for account_number, details in accounts.items():
            print(f"Számla száma: {account_number}, Számla tulajdonosa: {details['holder']}, Egyenleg: {details['balance']}")
    else:
        print("A számla nem található")












