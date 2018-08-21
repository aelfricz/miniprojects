class Board:
    def __init__(self, data):
        self.data=data

    def get_neighbours(self, x, y):
        neighbours = [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),             (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1),
        ]
        return(neighbours)

    def count_no_neighbours(self, x, y):
        neighbours = self.get_neighbours(x, y)
        count = 0
        for i in neighbours:
            if i in self.data:
                count +=1
        return(count)

    def turn(self):
        death_count=0
        new_board=self.data.copy()
        for cell in self.data:
            # rule 1
            no_neighbours = self.count_no_neighbours(cell[0],cell[1])
            # rule 3 and 2
            if no_neighbours < 2 or no_neighbours > 3:
                new_board.remove(cell)
            neighbours = self.get_neighbours(cell[0],cell[1])
            # rule 4
            for nb_cell in neighbours:
                no_neighbours = self.count_no_neighbours(nb_cell[0],nb_cell[1])
                if nb_cell not in self.data and no_neighbours == 3:
                    new_board.append(nb_cell)
        self.data=new_board
