kgram_array=[]
totalwords=[]
ch = []
i=0

docs = open("D.txt")

for l in docs:
    for ew in l.split():
        totalwords.append(ew)

print(totalwords)

for aw in range(len(totalwords)-1):
    kg = totalwords[aw],totalwords[aw+1]
    if kg not in kgram_array:
        kgram_array.append(kg)



print("k-grams list {}".format(kgram_array))
print("Number of k-grams {} ".format(len(kgram_array)))
