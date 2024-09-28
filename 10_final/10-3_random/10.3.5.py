import sys
import random

random.seed(1)
lst_in = list(map(str.split, sys.stdin.readlines()))
lst_zip = list(zip(*lst_in))
random.shuffle(lst_zip)
lst_out = list(zip(*lst_zip))
[print(*i, sep = " ") for i in lst_out]