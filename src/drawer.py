import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

HEX_SIZE = 1

class Drawer:
    def __init__(self,GRID_WIDTH,GRID_HEIGHT):
        self.GRID_WIDTH = GRID_WIDTH
        self.GRID_HEIGHT = GRID_HEIGHT
    
    # Function to create a hexagon at a given position
    def create_hexagon(self, x, y, color, ax):
        # Creates a hexagon at position (x, y) with a given color.
        hexagon = patches.RegularPolygon(
            (x, y), numVertices=6, radius=HEX_SIZE * 0.5,
            orientation=np.radians(30), facecolor=color, edgecolor='black'
        )
        ax.add_patch(hexagon)

    # Function to draw the hexagon grid
    def draw_hex_grid(self, ax, plane):
        ax.clear()
        max_y = self.GRID_HEIGHT * HEX_SIZE * 0.9
        for row in range(self.GRID_WIDTH):
            for col in range(self.GRID_HEIGHT):
                # If the Tile is empty and the actor is not carrying a Tile
                if plane.getTile(col,row) == False and (col != plane.getActor().getPosition().getX() or row != plane.getActor().getPosition().getY()):
                    continue
                # Calculate the position for each hexagon
                x = col * HEX_SIZE * 0.8  # Adjusted horizontal distance between hexagons
                y = max_y - (row * HEX_SIZE * 0.9 + (col % 2) * (HEX_SIZE * 0.5))
                # Adjusted vertical distance to make hexagons slightly further apart

                # Determine the color based on the grid state
                if col == plane.getActor().getPosition().getX() and row == plane.getActor().getPosition().getY():
                    color = 'black'  # Actor's position
                else:
                    color = 'lightgrey'  # Normal Tile

                self.create_hexagon(x, y, color, ax)

        ax.set_xlim(-1, self.GRID_WIDTH * HEX_SIZE * 0.8 + 1)
        ax.set_ylim(-1, self.GRID_HEIGHT * HEX_SIZE * 0.9 + 1)
        ax.set_aspect('equal')
        ax.axis('off')