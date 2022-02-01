kgram_array=[]
totalwords=[]
ch = []
i=0

docs = open("/Users/meghnamanjunatha/Downloads/D4.txt")

for l in docs:
    for ew in l:
        ch.append(ew)

print(ch)

for aw in range(len(ch)-1):
    kg = ch[aw],ch[aw+1]
    if kg not in kgram_array:
        kgram_array.append(kg)

print("k-grams list {}".format(kgram_array))
print("Number of k-grams {} ".format(len(kgram_array)))