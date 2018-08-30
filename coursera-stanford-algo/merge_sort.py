# use divide and conquer to merge_sort a large group of numbers
# to return a sorted list and count the number of inversion
# the max number of inversion for a given set of number is n choose 2. E.g. for 6 numbers is 15

count = 0

def merge_sort(x):
    global count
    xlen = len(x)

    if xlen > 2:
        output = []
        mid = int(xlen//2)

        # recursion call
        left_merge = merge_sort(x[:mid])
        right_merge = merge_sort(x[mid:])

        # main combination loop
        i = j = 0
        while i < mid and j < xlen-mid:
            if left_merge[i]<right_merge[j]:
                output.append(left_merge[i])
                i += 1
            else:
                output.append(right_merge[j])
                count += mid-i
                j += 1

        # end cases
        if i < mid:
            output.extend(left_merge[i:])
        if j < xlen-mid:
            output.extend(right_merge[j:])

        return(output)

    elif xlen == 2 and x[0]>x[1]:
        count +=1
        return ([x[1],x[0]])
    else:
        return (x)

with open("IntegerArray.txt") as f:
    lines = [int(line.rstrip('\n')) for line in f]

merge_sort(lines)

#print(merge_sort([37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18,
# 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]))
print(count)
