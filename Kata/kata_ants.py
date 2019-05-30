def ant(grid, column, row, n, direction=0):
    # Start position of the ant
    pos = [column, row]

    # This function takes the current direction and the rotator value and returns the new direction
    def turn(direction, rotator):
        if 0 <= direction + rotator <= 3:
            print('going ', direction + rotator)
            return direction + rotator
        elif direction + rotator < 0:
            print('going 3')
            return 3
        else:
            print('going 0')
            return 0

    # This function determines the new position of the ant and expands the grid if necessary
    def walk(grid, direction, pos):
        columns = len(grid[0])
        rows = len(grid)

        # If going north:
        if direction == 0:
            # If ant's row position is already 0 (upper row) :
            if pos[1] == 0:
                # insert a new row at pos 0 of grid with the length of [columns]
                grid.insert(0, [0] * columns)
                # count 1 more row
                rows += 1
                # move the ant to row 0
                pos[1] = 0
            else:
                # if the ant is not in the upper row, move it one row higher
                pos[1] -= 1
        # if going east:
        elif direction == 1:
            # if ant's column position is already utmost right:
            if pos[0] == columns - 1:
                # go through every row
                for idx in range(rows):
                    # append a new element at the end, thus making a new column
                    grid[idx].append(0)
                # count 1 more column
                columns += 1
                # move ant to next column
                pos[0] += 1
            else:
                # if the ant is not in the utmost right column, move ant to next column
                pos[0] += 1
        # if going south:
        elif direction == 2:
            # if ant's row position is last row:
            if pos[1] == rows - 1:
                # append another row to the grid
                grid.append([0] * columns)
                # count another row
                rows += 1
                # move ant one row down
                pos[1] += 1
            else:
                # if ant is not in the last row, move ant one row down
                pos[1] += 1
        # if going west:
        elif direction == 3:
            # if ant already in first column:
            if pos[0] == 0:
                # go through each row
                for idx in range(rows):
                    # insert another 0 at the front, thus making a new column 0
                    grid[idx].insert(0, 0)
                # count another column
                columns += 1
                # move ant to first column
                pos[0] = 0
            else:
                # if ant is not in column 0, move it to the left
                pos[0] -= 1

        return pos, grid

    # this function flips the current cell
    def flip(grid, pos):
        if grid[pos[1]][pos[0]] == 1:
            # flip color
            grid[pos[1]][pos[0]] = 0
            return 1
        else:
            # flip color
            grid[pos[1]][pos[0]] = 1
            return -1

    # This function shows the grid with the ant
    def show(show_grid, pos):
        show_grid[pos[1]][pos[0]] = 8
        for el in show_grid:
            print(el)
        return

    # main body function: flip, turn, walk, show
    for i in range(n):
        rotator = flip(grid, pos)
        direction = turn(direction, rotator)
        pos, grid = walk(grid, direction, pos)
        show_grid = [x[:] for x in grid]
        show(show_grid, pos)

    return grid


result = ant([[1]], 0, 0, 50, 0)

