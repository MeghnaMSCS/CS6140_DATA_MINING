import timeit
import random
import matplotlib.pyplot as plots

def bdaypdx(n,m,tt):


    begin = timeit.default_timer()
    notrs = []

    for i in range(m):
        nt=0
        f='FALSE'
        a=[]
        while f=='FALSE':
            nt+=1
            a.append(random.randint(1,n))
            if len(a) !=len(set(a)):
                f='TRUE'
                notrs.append(nt)
    comp = timeit.default_timer()-begin
    tt.append(comp)

    before_coll = sum(notrs)/m

    return notrs,before_coll,tt

#Plotting
tt=[]
notrs=[]
nostp=[]
m=10000
n_most = 1000001
for i in range(1,n_most+1,100000):
    [notrs,before_coll,tt]=bdaypdx(i,m,tt)
    print(i)
    nostp.append(i)

print('Range of n {}'.format(i))
print("Trials %d" %len(notrs))
print('Collision trials {:.2f}'.format(before_coll))
print('Time taken to Execute totally {:.4f}'.format(sum(tt)))
print('Time for execution',tt)

plots.plot(nostp,tt)
plots.ylim()
plots.xlabel(" n = Domain Size")
plots.ylabel(" time ")
plots.title( "Trials m={}".format(m) )
plots.grid(True)
plots.show()




