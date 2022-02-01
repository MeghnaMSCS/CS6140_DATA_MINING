import numpy as np

kgram_array1=[]
totalwords1=[]
ch1 = []

docs1 = open("D.txt")

for l1 in docs1:
    for ew1 in l1.split():
        totalwords1.append(ew1)

print(totalwords1)

for aw1 in range(len(totalwords1)-1):
    kg1 = totalwords1[aw1],totalwords1[aw1+1]
    if kg1 not in kgram_array1:
        kgram_array1.append(kg1)

kgram_array2=[]
totalwords2=[]
ch2 = []


docs2 = open("D.txt")

for l2 in docs2:
    for ew2 in l2.split():
        totalwords2.append(ew2)

print(totalwords2)

for aw2 in range(len(totalwords2)-1):
    kg2 = totalwords2[aw2],totalwords2[aw2+1]
    if kg2 not in kgram_array2:
        kgram_array2.append(kg2)

num = len(set.intersection(*[set(kgram_array1),set(kgram_array2)]))
deno = len(set.union(*[set(kgram_array1),set(kgram_array2)]))
Jaccsim = num/deno

print("Jaccard Similarity = {}".format(Jaccsim))