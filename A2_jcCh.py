import numpy as np

kgram_array1=[]
totalwords1=[]
ch1 = []


docs1 = open("/Users/meghnamanjunatha/Downloads/D4.txt")

for l1 in docs1:
    for ew1 in l1:
        ch1.append(ew1)

print(ch1)

for aw1 in range(len(ch1)-1):
    kg1 = ch1[aw1],ch1[aw1+1]
    if kg1 not in kgram_array1:
        kgram_array1.append(kg1)

kgram_array2=[]
totalwords2=[]
ch2 = []


docs2 = open("/Users/meghnamanjunatha/Downloads/D4.txt")

for l2 in docs2:
    for ew2 in l2:
        ch2.append(ew2)

print(ch2)

for aw2 in range(len(ch2)-1):
    kg2 = ch2[aw2],ch2[aw2+1]
    if kg2 not in kgram_array2:
        kgram_array2.append(kg2)

num = len(set.intersection(*[set(kgram_array1),set(kgram_array2)]))
deno = len(set.union(*[set(kgram_array1),set(kgram_array2)]))
Jaccsim = num/deno

print("Jaccard Similarity = {}".format(Jaccsim))