#num=int(input())
#w=list(map(int,input().split()))
num=6
w=[1,4,5,2,7,8]
s=0
g=0
for i in range(num-1):
    print(i)
    maxi=max(w[i+1:])
    maxn=w.index(maxi)
    mini=min(w[maxn:])
    if w[i]<maxi and maxi>mini:
        print(i,5)
    elif w[i]<maxi and maxi<mini:
        print(i,10)
    else:
        print(15)


            