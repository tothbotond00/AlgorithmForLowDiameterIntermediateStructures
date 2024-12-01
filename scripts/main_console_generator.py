import plane_console as plane
import sys

response_string = "steps,steps_tile,tiles,moved_tiles\n"

for i in range(100):
    try:
        # Parameters for the hexagon grid
        GRID_WIDTH = int(sys.argv[1])
        GRID_HEIGHT = int(sys.argv[2])
        filename = str(i) + '.txt'
        tile_counter = [0]
        plane2 = plane.Plane(GRID_HEIGHT,GRID_WIDTH,filename, tile_counter)
        
        moved_tiles_counter = [0]
        step_counter = [0, 0]
        plane2.moveActor(step_counter, moved_tiles_counter)
        steps = str(step_counter[0])
        steps_tile = str(step_counter[1])
        tiles = str(tile_counter[0])
        moved_tiles = str(moved_tiles_counter[0])
        response_string += steps + ',' + steps_tile + ',' + tiles + ',' + moved_tiles + "\n"
    except Exception as e:
        pass
        #print(i)

print(response_string)