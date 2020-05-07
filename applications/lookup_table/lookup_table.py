import sys 
sys.path.append('../../hashtable')
from hashtable import HashTable

import math
import random

slowfun_table = HashTable(50001)

def slowfun(x, y):
    r = slowfun_table.get(str((x, y)))
    if r is None:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        slowfun_table.put(str((x,y)), v)
        return v
    return r
    # TODO: Modify to produce the same results, but much faster
    # v = math.pow(x, y)	   
    # v = math.factorial(v)	     
    # v //= (x + y)	      
    # v %= 982451653
    # return v
# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
