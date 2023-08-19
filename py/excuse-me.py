
'''
    For a good excuse we need 3 things:

    1 - Introduction
    2 - Blaming entity
    3 - Raised exception

    Example:
    "Wow, I'd really wanted to go, but ...
        my Grandmother ...
            just got into flames due to spontaneous combustion."
'''
import random
import linecache
import os

def f_intro():
    file = os.path.join( os.getcwd(), 'excusables', 'intro.txt' )
    with open(file, "r") as f:
        size = len(f.readlines())
        line = linecache.getline(file, random.randint(1, size) )
        return line.replace('\n', ' ')

def f_blame():
    file = os.path.join( os.getcwd(), 'excusables', 'blame.txt' )
    with open(file, "r") as f:
        size = len(f.readlines())
        line = linecache.getline(file, random.randint(1, size) )
        return line.replace('\n', ' ')

def f_absurd():
    file = os.path.join( os.getcwd(), 'excusables', 'excep.txt' )
    with open(file, "r") as f:
        size = len(f.readlines())
        line = linecache.getline(file, random.randint(1, size) )        
        return line.replace('\n', ' ')

def main(): # I like C, complain as you wish
    print(  f_intro() +\
            f_blame() +\
            f_absurd())

main()






