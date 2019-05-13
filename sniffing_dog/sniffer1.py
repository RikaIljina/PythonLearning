

# make an array
# lay a random path in that array
# make a dog

# give it logic to walk randomly to the next field
# let it follow a trail out of the array

# when printing array, wrap it with walls
from random import *
import sys
sys.stdout.reconfigure(encoding='utf-8')

dog = chr(12125)
dog_pos = [9, 9]
print(dog_pos[1])
maze = [[chr(8857)]*20 for i in range(10)]
maze[dog_pos[0]][dog_pos[1]] = dog
trace = chr(10048)
seed()
rnd1 = randrange(0, 19)
trace_start = [0, rnd1]
rnd2 = rnd1+randrange(-1, 1) if rnd1 != 0 and rnd1 != 19 else (rnd1+randrange(0, 1) if rnd1 == 0 else rnd1+randrange(-1, 0))
trace_2 = [1, rnd2]
maze[trace_start[0]][trace_start[1]] = trace
maze[trace_2[0]][trace_2[1]] = trace

for row in maze:
    for cell in row:
        print(cell, end='')
    print('')





# chr_trace_tile = chr(1422)    # 129  10048
# print(chr_trace_tile)
# print(chr(10048))
# print(chr(1792))
# print(chr(4031))
# print(chr(5580))
# print(chr(8418))
# print(chr(9619))
# print(chr(9641))
# print(chr(12125))
# print(chr(9723))
# print(chr(8857))
# print(ord('⊙'))
#for i in range(1400,2000):
#    print(i, chr(i))

