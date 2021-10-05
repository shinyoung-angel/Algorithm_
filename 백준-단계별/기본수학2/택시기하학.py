

import math
import sys

n = int(sys.stdin.readline())

a = round(n**2*math.pi, 6)
b = round(2 * n * n, 6)
print('{:.6f}'.format(a))
print('{:.6f}'.format(b))