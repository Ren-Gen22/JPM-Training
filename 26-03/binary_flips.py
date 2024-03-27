inp=list(input())
n=len(inp)
nxt=0
sw=0
strt=[0 for _ in range(n)]
for i in range(n):
    if inp[i]=='1' and nxt==1:
        strt[i]=1
        nxt=0
        sw+=1
    elif inp[i]=='0' and nxt==0:
        strt[i]=0
        nxt=1
        sw+=1
print(sw)
