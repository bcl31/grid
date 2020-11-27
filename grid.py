
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


def main():
    grid = create_grid("data_1.txt")
    display_grid(grid)


main()
