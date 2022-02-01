import numpy as np
import random
import timeit

ts = timeit.default_timer
te = []

kgram_array1=[]
totalwords1=[]
ch1 = []


docs1 = open("D1.txt")

for l1 in docs1:
    for ew1 in l1:
        ch1.append(ew1)

print(ch1)

for aw1 in range(len(ch1)-1):
    kg1 = ch1[aw1],ch1[aw1+1]
    if kg1 not in kgram_array1:
        kgram_array1.append(kg1)
u1 = len(set(kgram_array1))
kgram_array2=[]
totalwords2=[]
ch2 = []


docs2 = open("D2.txt")

for l2 in docs2:
    for ew2 in l2:
        ch2.append(ew2)

print(ch2)

for aw2 in range(len(ch2)-1):
    kg2 = ch2[aw2],ch2[aw2+1]
    if kg2 not in kgram_array2:
        kgram_array2.append(kg2)
u2 = len(set(kgram_array2))

maxt = 10000
comp = np.zeros((maxt,u2))
open('opt.txt','w').close()
file = open('opt.txt','w')
for tm in range(maxt):
    random.shuffle(kgram_array1)
    random.shuffle(kgram_array2)
    for j in range(u2):
        if kgram_array1[j] == kgram_array2[j]:
            comp[tm][j] = 1
            file.write(repr(comp[tm][j])+'\n')
        else:
            comp[tm][j]=0
            file.write(repr(comp[tm][j])+'')

file.close()

jacsim = (1/maxt)*np.sum(comp)
print('Jaccard Dimilarity',jacsim)
elp = timeit.default_timer() - ts
te.append(elp)
print('Time',te)