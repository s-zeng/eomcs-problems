#!/usr/bin/python3.6
import random
for i in range(3, 17):
    rows = min(2**i - 1, 1500)

    filenum = str(i).zfill(2)
    print(f'Working on case {filenum}...')
    with open(f'input/input{filenum}.txt', 'w+') as out:
        out.write(str(rows))
        for m in range(rows + 1):
            for n in range(m):
                out.write(str(int(random.random()*(2*rows))) + ' ')
            out.write('\n')
# prints out 7273
