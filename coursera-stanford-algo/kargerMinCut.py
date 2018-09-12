import random


with open("kargerMinCut.txt") as f:
    lines = [list(map(int, line.split())) for line in f]


def indexing(element):
    header = [item[0] for item in lines]
    return header.index(element)


def random_edge_value():
    line_index = random.choice(range(0,len(lines)-1))
    element_index = random.choice(range(1,len(lines[line_index])-1))
    vertice = lines[line_index][0]
    edge = lines[line_index][element_index]
    alt_line_index = indexing(edge)

    #swap order
    if vertice > edge:
        vertice, edge = edge, vertice
        line_index, alt_line_index = alt_line_index, line_index

    return vertice, edge, line_index, alt_line_index


def contraction(vertice, edge, line_index, alt_line_index):
    #remove edge
    lines[line_index].remove(edge)
    lines[alt_line_index].remove(vertice)

    # combine vertices
    lines[line_index].extend(lines[alt_line_index][1:])
    del lines[alt_line_index]

    # rename pointers
    #print("renaming "+str(edge)+" to "+str(vertice))
    for line in range(0,len(lines)):
        lines[line] = [vertice if item==edge else item for item in lines[line]]

    # removing self loops
    y2 = list(filter(lambda a: a != vertice, lines[line_index][1:]))
    y1 = [lines[line_index][0]]
    lines[line_index] = y1+y2
    #print(lines[line_index])


def contraction_loop():
    while len(lines)>2:
        x = random_edge_value()
        contraction(x[0],x[1],x[2],x[3])
    return(len(lines[0])-1)


print(contraction_loop())
