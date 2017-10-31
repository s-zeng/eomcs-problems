import random
# Ns = [0, 3, 4, 5, 10, 15, 20, 30, 50, 75, 100, 125, 150, 175, 200, 200]
Ns = [0, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 10, 12, 15, 20]
for i in range(1, 16):
    filenum = str(i).zfill(2)
    N = Ns[i]
    # C = []
    # for j in range(N):
        # C.append(round(random.random()*1000, 2))
    C = random.sample(range(1, 5000*N), N)
    C.sort()
    V = random.randrange(C[-1], 5000*N)/100
    while(1):
        for i, x in enumerate(C):
            if V%x == 0.0:
                C[i] += 0.01
        break
    cstr = ' '.join(str(x/100) for x in C)
    out = f'{N} {V}\n{cstr}'
    with open(f'input/input{filenum}.txt', 'w+') as f:
        f.write(out)

