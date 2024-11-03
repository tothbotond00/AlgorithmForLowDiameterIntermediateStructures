import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.widgets import Button
import matplotlib.animation as animation
import plane
import sys
import drawer

# Parameters for the hexagon grid
GRID_WIDTH = int(sys.argv[1])
GRID_HEIGHT = int(sys.argv[2])
filename = sys.argv[3]
HEX_SIZE = 1
drawer = drawer.Drawer(GRID_WIDTH, GRID_HEIGHT)
plane = plane.Plane(GRID_HEIGHT,GRID_WIDTH,filename)

# Set up the plot with a button for starting the animation
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
start_ax = plt.axes([0.7, 0.05, 0.1, 0.075])
start_button = Button(start_ax, 'Start')

# Function to start the animation
def start(event):
    plane.moveActor(ax, drawer)

# Attach the button click event to start the animation
start_button.on_clicked(start)

# Draw the initial grid
drawer.draw_hex_grid(ax, plane)
plt.show()
