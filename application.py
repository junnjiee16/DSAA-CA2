# from classes.utils import Utils
# from classes.map import Map
# from classes.pathfinder import Pathfinder
# from classes.drone import Drone
# from archived_classes.screen import Screen

import turtle

# program logic imports
from classes.utils import Utils
from classes.map import Map
from classes.drone import Drone
from classes.mapgraph import MapGraph

# pathfinder imports
from classes.lefthandpathfinder import LeftHandPathfinder
from classes.shortestpathfinder import ShortestPathfinder

# media imports
from classes.renderer import Renderer
from classes.dronesprite import DroneSprite
from classes.blocksprite import BlockSprite


# class to control the logic of the program
class Application:
    # metadata for the program
    def __init__(self, program_name, authors, class_name):
        self.program_name = program_name
        self.authors = authors
        self.class_name = class_name
        self.title = f"{self.program_name}: Done by {self.authors}, {self.class_name}"

    def startProgram(self, file_name):

        ### -------------------------------------------------------
        ### READ AND SCAN MAP FILE
        ### -------------------------------------------------------
        print("Reading and scanning map file")
        map_text, start_pos, end_pos = Utils.readMapFile(file_name)
        if map_text == None:
            return



        ### -------------------------------------------------------
        ### RUN ALL PROGRAM LOGIC FIRST BEFORE RENDERING ANYTHING
        ### -------------------------------------------------------
        # instantiate map and drone objects
        map = Map(map_text, start_pos, end_pos)
        drone = Drone(current_pos=map.start_pos)

        # get graph from map
        map_graph = Utils.map_to_graph(map.layout, map.start_pos, map.end_pos)

        # instantiate pathfinder object and solve the graph, default is left hand algorithm
        lefthand_pathfinder = LeftHandPathfinder()
        lefthand_pathfinder.solve(map_graph)
        solution = lefthand_pathfinder.solution



        ### -------------------------------------------------------
        ### RENDERING GRAPHICS
        ### -------------------------------------------------------
        # create turtle screen
        window = turtle.Screen()

        # use Renderer to render map and spawn the drone
        Renderer.render_map(map.layout)
        drone_sprite = Renderer.spawn_drone(drone.current_pos, drone.orientation)



        ### -------------------------------------------------------
        ### CATCH KEY PRESS EVENTS
        ### -------------------------------------------------------
        


        # this must be the last line in the turtle program
        window.mainloop()

        # # create the turtle screen
        # window = Screen(self.title)

        # # instantiate map
        # map = Map(map_text, start_coords, end_coords)

        # # create graph from map layout
        # print("Generating graph from map")
        # graph = Utils.map_to_graph(map.layout)

        # # instantiate pathfinder object
        # print("Instantiating pathfinder object")
        # pathfinder = Pathfinder(graph, map.start_position, map.end_position)

        # # draw map on screen
        # print("Drawing map")
        # map.draw() # this uses turtle's Turtle object to place down tiles on the map

        # # solve maze
        # solution = pathfinder.maze_solution() # 0 = Left Hand Algorithm, 1 = Shortest Path Algorithm

        # # show the solution
        # # instantiate Drone object
        # drone = Drone(solution, map.start_position)

        # # update title bar after everything is initialized
        # window.update_title(f"{self.title}, {pathfinder.algo_name()} - Steps: {drone.steps_taken}")

        # # set key event handlers
        # # command drone to execute next step in solution and update title bar
        # window.set_key(
        #     lambda: 
        #         drone.move() or 
        #         window.update_title(f"{self.title}, {pathfinder.algo_name()} - Steps: {drone.steps_taken}"), 
        #     "m"
        # )

        # # TAB key: reset drone, change algorithm, update solution, update title bar
        # window.set_key(
        #     lambda: 
        #         drone.reset() or 
        #         pathfinder.change_algo() or 
        #         drone.set_instructions(pathfinder.maze_solution()) or
        #         window.update_title(f"{self.title}, {pathfinder.algo_name()} - Steps: {drone.steps_taken}"), 
        #     "Tab"
        # )

        # # this must be the last line in the turtle program
        # window.mainloop()