import numpy as np
import random
import os

def generate_more_random_hexagons(size=30, ones_count=25):
    """
    Generate a matrix with a random connected shape, ensuring exactly `ones_count` connected 1's and one 2.
    """
    # Create an empty matrix
    matrix = np.zeros((size, size), dtype=int)

    # Randomly choose the starting position for the '2'
    center_x, center_y = random.randint(5, size - 5), random.randint(5, size - 5)
    matrix[center_x, center_y] = 2

    # Helper to get neighbors in a hexagonal grid
    def get_neighbors(x, y):
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # up, down, left, right
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # diagonals
        ]
        return [(x + dx, y + dy) for dx, dy in directions if 0 <= x + dx < size and 0 <= y + dy < size]

    # Generate exactly `ones_count` connected ones with a random path shape
    to_visit = [(center_x, center_y)]
    visited = set()

    while len(visited) < ones_count:
        if not to_visit:
            break  # Avoid infinite loop if disconnected areas arise
        x, y = to_visit.pop(random.randint(0, len(to_visit) - 1))
        if (x, y) in visited:
            continue
        visited.add((x, y))
        matrix[x, y] = 1

        # Add neighbors to the queue with some randomness
        if len(visited) < ones_count:
            neighbors = get_neighbors(x, y)
            random.shuffle(neighbors)
            to_visit.extend(neighbors[:random.randint(1, len(neighbors))])

    # Set visited cells to 1, leaving the starting cell as 2
    for x, y in visited:
        matrix[x, y] = 1
    matrix[center_x, center_y] = 2

    return matrix

def write_matrix_to_file(matrix, directory="tests", filename="1.txt"):
    """
    Write the generated matrix as a string to a file in the specified directory.
    If the directory doesn't exist, it will be created.

    Args:
        matrix: The matrix to write, as a list of strings (each representing a row).
        directory: The directory to create the file in (default is 'tests').
        filename: The name of the file to write (default is 'matrix_output.txt').
    """
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    # Full file path
    file_path = os.path.join(directory, filename)

    # Write the matrix to the file
    with open(file_path, "w") as file:
        file.write("\n".join("".join(map(str, row)) for row in matrix))

    return file_path

# Generate a random shape matrix and write it to a file
for i in range(100):
    random_shape_matrix = generate_more_random_hexagons()
    file_path = write_matrix_to_file(random_shape_matrix, directory="tests", filename=str(i)+".txt")