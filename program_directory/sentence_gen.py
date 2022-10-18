import random

from program_directory.data import *
import random
from time import sleep

delay = 1

def index(l):
    return random.choice(l)

def main():
    name = index(names)
    verb = index(verbs)
    mid = index(mids)
    end = index(ends)
    print(name, verb, mid, end)
    sleep(delay)

while True:
    main()