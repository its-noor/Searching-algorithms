import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.animation as animation
from bfs import bfs
from dfs import dfs
from gbfs import gbfs
from astar import astar

from utils import *
from grid import *

def gen_polygons(worldfilepath):
    polygons = []
    with open(worldfilepath, "r") as f:
        lines = f.readlines()
        lines = [line[:-1] for line in lines]
        for line in lines:
            polygon = []
            pts = line.split(';')
            for pt in pts:
                xy = pt.split(',')
                polygon.append(Point(int(xy[0]), int(xy[1])))
            polygons.append(polygon)
    return polygons

if __name__ == "__main__":
    epolygons = gen_polygons('TestingGrid/world1_enclosures.txt')
    tpolygons = gen_polygons('TestingGrid/world1_turfs.txt')

    source = Point(8,10)
    dest = Point(43,45)


    fig, ax = draw_board()
    draw_grids(ax)
    draw_source(ax, source.x, source.y)  # source point
    draw_dest(ax, dest.x, dest.y)  # destination point
    
    # Draw enclosure polygons
    for polygon in epolygons:
        for p in polygon:
            draw_point(ax, p.x, p.y)
    for polygon in epolygons:
        for i in range(0, len(polygon)):
            draw_line(ax, [polygon[i].x, polygon[(i+1)%len(polygon)].x], [polygon[i].y, polygon[(i+1)%len(polygon)].y])
    
    # Draw turf polygons
    for polygon in tpolygons:
        for p in polygon:
            draw_green_point(ax, p.x, p.y)
    for polygon in tpolygons:
        for i in range(0, len(polygon)):
            draw_green_line(ax, [polygon[i].x, polygon[(i+1)%len(polygon)].x], [polygon[i].y, polygon[(i+1)%len(polygon)].y])

    #### Here call your search to compute and collect res_path
   
    print("Select search algorithm:")
    print("1. BFS")
    print("2. DFS")
    print("3. GBFS")
    print("4. ASTAR")
    choice = input("Enter choice: ").strip()

    if choice == '1':
        path = bfs(source, dest, epolygons, tpolygons)
    elif choice == '2':
        path = dfs(source, dest, epolygons, tpolygons)
    elif choice == '3':
        path = gbfs(source, dest, epolygons, tpolygons)
    elif choice == '4':
        path = astar(source, dest, epolygons, tpolygons)    
    else:
        print("Invalid choice. Exiting.")
        exit(0)

    if path is None:
        print("No path found!")
    else:
        for i in range(len(path) - 1):
            draw_result_line(ax, [path[i].x, path[i+1].x], [path[i].y, path[i+1].y])
            plt.pause(0.1)


    # res_path = [Point(24,17), Point(25,17), Point(26,17), Point(27,17),  
    #             Point(28,17), Point(28,18), Point(28,19), Point(28,20)]
    
    
    plt.show()
