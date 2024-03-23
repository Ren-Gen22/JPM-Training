# num=int(input())
# w=list(map(int,input().split()))
num = 6
w = [1, 4, 5, 2, 7, 8]
#w = [2, 3, 6, 4, 1]
#w=[1,4,5,4]
out = 0
for i in range(num-1):
    j = i+1
    g = j
    s = g
    while j < num-1:
        s = g+1
        if w[j] > w[g]:
            g = j
        if w[g] > w[j]:
            s = j
            break
        j += 1
    print(s, g, i, "|", w[s], w[g], w[i])

    if w[g] > w[i] and w[s] < w[g]:
        out+=5
    elif w[g] > w[i]:
        out+=10
    else:
        out+=15
out+=15

print(out)


"""
current i
greatest nxt g
smallest nxt s

5 - higher weight, small weight
10 - higher weight, no smaller weight
15 - no higher weight

1 4 5  2  7  8
5 5 10 10 10 15
"""
