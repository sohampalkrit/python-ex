def move(input_list):
    x=input_list[0][0]
    y=input_list[0][1]
    s1=input_list[1]
    n=len(s1)
    i=0
    while i<n:
        if s1[i]=='R':
            x=x+1
        elif s1[i]=='L':
            x=x-1
        elif s1[i]=='U':
            y=y+1
        elif s1[i]=='D':
            y=y-1
        i+=1
    return tuple([x,y])

