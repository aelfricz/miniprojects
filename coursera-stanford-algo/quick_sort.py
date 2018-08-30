count=0

def find_median_pos(x):
    a=x[0]
    lenx=len(x)
    b=x[lenx-1]
    cpos = int((lenx+lenx%2)/2-1)
    c=x[cpos]

    ans=[a,b,c]
    ans.sort()
    if ans[1] == a:
        return 0
    elif ans[1] == b:
        return lenx-1
    else:
        return cpos

def swap(list,x,y):
    list[x],list[y] = list[y],list[x]

def quick_sort(x, type="first"):
    p=0
    i=1
    lenx = len(x)
    global count
    count+=lenx-1
    if type == "last":
        swap(x,0,lenx-1)
    elif type == "median":
        median_pos_x = find_median_pos(x)
        if median_pos_x != 0:
            swap(x,0,median_pos_x)

    # main swap loop
    for j in range(1,lenx):
        if x[j]<x[p]:
            if j>i:
                swap(x,i,j)
            i+=1
    swap(x,p,i-1)

    # recursive calls
    if i-1>1:
        x[:i-1]=quick_sort(x[:i-1], type)
    if lenx-1>i:
        x[i:]=quick_sort(x[i:], type)
    return(x)


with open("quicksortarray.txt") as f:
    lines = [int(line.rstrip('\n')) for line in f]

#print(lines2)
quick_sort(lines, type="median")
print(count)
