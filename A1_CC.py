import timeit
import random
import matplotlib.pyplot as plots
import numpy as np

def cc(n,nfull,m,tt):
    begin = timeit.default_timer()
    notrs = []

    for r in range(m):
        nt = 0
        f='FALSE'
        a=[]
        while f=='FALSE':
            nt+=1
            a.append(random.randint(1,n))
            if len(set(a)) == n:
                f='TRUE'
                notrs.append(nt)

    comp = timeit.default_timer() - begin
    tt.append(comp)
    fullsets = sum(notrs)/m
    return notrs,fullsets,a,nt,tt

m=2000
nfull = 500

tt=[]
notrs=[]
nostp = []

for r in range(1,nfull+2, 50):
    [notrs, fullsets,a,nt,tt]=cc(r,nfull,m,tt)
    print(r)
    nostp.append(r)

print('Range of n:{}'.format(r))
print("No. of repeats m %d" %len(notrs))
print('No. of random set l {}'.format(nt))
print('Time taken to Execute totally  {:.4f}'.format(sum(tt)))
print('Time for execution',tt)

#plotting
plots.plot(nostp,tt)
plots.ylim((0))
plots.xlabel("n")
plots.ylabel("time")
plots.title("Trials m={}".format(m))
plots.grid(True)
plots.show()

dim=len(notrs)
coll = sorted(set(notrs))
app = np.append(coll,coll[-1]+1)
ct,apps = np.histogram(notrs,bins=app,density=False)
cts = ct.astype(float)/dim
cdistf=np.cumsum(cts)

plots.plot(apps[0:-1],cdistf,linestyle='-.',marker='o',color='r')
plots.ylim((0))
plots.xlabel("No. of trials")
plots.ylabel("Cumulative Distributive Function")
plots.show()












