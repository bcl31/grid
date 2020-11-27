
# filename is a string representing the name of a file

# Create a nested list based on the data given in a file
def create_grid(filename):
    grid = []
    grid_info = open(filename, "r")

    # find grid dimensions
    row_number = int(grid_info.readline())
    row_width = int(grid_info.readline())

    # for each row, create a blank list then add row_list amount of values from the grid info file as ints
    for row_location in range(row_number):
        row = []
        for item_pos in range(row_width):
            row.append(int(grid_info.readline()))

    # append the row list to the grid list before the row list is cleared
        grid.append(row)
    return grid


# grid is a two dimensional nested list

# Display the grid as seen in the screenshot.
def display_grid(grid):
    for row in grid:

        # create a copy of the row with string values instead of ints
        row_str = [str(value) for value in row]

        # add blank items at beginning and end of list to allow for side barriers
        row_str.insert(0, "")
        row_str.append("")

        # create a string out of the list with vertical lines between entries and print it
        row_str = " | ".join(row_str)
        print(row_str)


# row_index is an int representing the row index
# col_index is an int representing the column index
# gris is a two dimensional nested list

# Find all the neighbors of a particular cell in the grid.
def find_neighbors(row_index, col_index, grid):

    # find the range of indexes around the provided tile
    row_range = range(row_index - 1, row_index + 2)
    col_range = range(col_index - 1, col_index + 2)

    # check each index around the tile, if it is valid and not the index of the initial tile, add it's value to the list
    neighbors = []
    for row in row_range:
        if 0 <= row < len(grid):
            for column in col_range:
                if 0 <= column < len(grid[0]):
                    if row != row_index or column != col_index:
                        neighbors.append(grid[row][column])
    return neighbors


# grid is a two dimensional nested list

# Uses the find_neighbors(row_index, col_index, grid) function to return a new two dimensional nested list
# that depicts the sum of neighbors in each cell respectively.
def sum_of_neighbors(grid):
    sum_grid = []

    # go through each tile in the grid
    for row_index in range(len(grid)):
        row = []
        for column_index in range(len(grid[0])):

            # find the neighbors of the tile, then the sum of those neighbors and append it to the row list
            neighbors = find_neighbors(row_index, column_index, grid)
            neighbor_sum = sum(neighbors)
            row.append(neighbor_sum)

        # once a row is finished, append it to the grid
        sum_grid.append(row)
    return sum_grid


def main():
    file_name = "data_1.txt"
    grid = create_grid(file_name)
    print("This is our grid: ")
    display_grid(grid)
    print("\n This is our newly calculated grid: ")
    sum_grid = sum_of_neighbors(grid)
    display_grid(sum_grid)


main()
