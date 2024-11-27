import plane_console as plane
import sys

# Parameters for the hexagon grid
GRID_WIDTH = int(sys.argv[1])
GRID_HEIGHT = int(sys.argv[2])
filename = sys.argv[3]
tile_counter = [0]
plane = plane.Plane(GRID_HEIGHT,GRID_WIDTH,filename, tile_counter)

moved_tiles_counter = [0]
step_counter = [0, 0]
plane.moveActor(step_counter, moved_tiles_counter)
print("Steps: " + str(step_counter[0]))
print("Steps while carrying a tile: " + str(step_counter[1]))
print("Tiles: " + str(tile_counter[0]))
print("Moved Tiles: " + str(moved_tiles_counter[0]))