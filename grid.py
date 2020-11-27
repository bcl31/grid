

def create_grid(filename):
    grid = []
    grid_info = open(filename, "r")
    row_number = int(grid_info.readline())
    row_width = int(grid_info.readline())
    for row_location in range(row_number):
        row = []
        for item_pos in range(row_width):
            row.append(int(grid_info.readline()))
        grid.append(row)
    return grid


print(create_grid("data_1.txt"))
