#!/usr/bin/python3
def modular_inverse(a, b): #extended euclidean
    original_b = b # store original b for taking remainder at the very end
    sum1, sum2 = 0, 1 # variables for extended euclidean algorithm
    while(a > 1):
        sum1, sum2 = sum2, sum1 - sum2*(b//a) #extension part of extended euclidean
        a, b = b%a, a #euclidean algorithm proper
    if a == 0: return 'None' #return 'None' if gcd is 0 (coprime means no modular inverse)
    
    #sometimes this algorithm returns negative so we mod it again at
    #the end to turn it positive. note that python is relatively unique
    #in having a proper mod behaviour for negative numbers
    #that is, (-x)%n should be (n-x)%n for 0 <= x <= n
    #rather than -(x%n)
    return sum2%original_b

#input loop
while(1): print(modular_inverse(*tuple([int(x) for x in input().split()])))
# for i in range(17):
   # print(f'Working on input {i}...')
   # filenum = str(i).zfill(2)
   # with open(f'input/input{filenum}.txt', 'r') as f:
       # inputs = [int(x) for x in f.readline().split()]
   # out = modular_inverse(inputs[0], inputs[1])
   # with open(f'output/output{filenum}.txt', 'w+') as f:
       # f.write(str(out))
