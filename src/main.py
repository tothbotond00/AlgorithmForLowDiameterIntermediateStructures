import matplotlib.pyplot as plt
from matplotlib.widgets import Button
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
plt.subplots_adjust(bottom=0.115, top=1, )
slower_button = Button(plt.axes([0.7, 0.05, 0.1, 0.075]), 'Slower')
quit_button = Button(plt.axes([0.81, 0.05, 0.1, 0.075]), 'Quit', color='#b38181')
faster_button = Button(plt.axes([0.59, 0.05, 0.1, 0.075]), 'Faster')
start_button = Button(plt.axes([0.48, 0.05, 0.1, 0.075]), 'Start', color='#81b38d')

# Function to start the animation
def start(event):
    plane.moveActor(ax, drawer)

def addTime(event):
    plane.addTime()

def subTime(event):
    plane.subTime()

def quit(event):
    sys.exit()

# Attach the button click event to start the animation
start_button.on_clicked(start)
slower_button.on_clicked(addTime)
faster_button.on_clicked(subTime)
quit_button.on_clicked(quit)

# Draw the initial grid
drawer.draw_hex_grid(ax, plane)
plt.show()
