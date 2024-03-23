    # num,constM=map(int,input().split())  #num of deliver ppl &  btwn how many house they wrk
    # l=list()
    num = 3
    l = [[3,5],[2,4],[6,7]]

    # for _ in range(num):
    #     a, b = map(int, input().split())o
    #     l.append([a, b])
    l.sort()
    print(l)
    srt=False
    stps=0
    for i in range(num-1):
        if l[i+1][0] in range(l[i][0]-1,l[i][1]+1) and srt==False:
            start=l[i][0]
            print("s",start)
            srt=True
        elif l[i+1][0] not in range(l[i][0]-1,l[i][1]+1) and srt==True:
            srt=False
            print("ending",l[i][1])
            stps+=l[i][1]-start
        else:
            print("skip",l[i][1]-l[i][0])
            stps+=l[i][1]-l[i][0]
    stps+=l[num-1][1]-l[num-1][0]
    print(stps)    

        

    """ 
    3 devery person with 2 house each
    2 4
    3 5
    6 7

    1 2 3 4 5 6 7 

    2
    2
    1

    houses located at equal distances  in a row
    each houe has unique number
    n delivery people 
    stops on required house
    two houses by each person
    if same house visit then more order


    """
