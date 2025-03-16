from utils import *
from grid import *

def in_polygon(point, polygon):
    x, y = point.x, point.y
    inside = False
    n = len(polygon)
    for i in range(n):
        j = (i + 1) % n
        xi, yi = polygon[i].x, polygon[i].y
        xj, yj = polygon[j].x, polygon[j].y
        if (yi > y) != (yj > y):
            x_intersect = (xj - xi) * (y - yi) / (yj - yi) + xi
            if x < x_intersect:
                inside = not inside
    return inside

def on_edge(point, polygon):
    x, y = point.x, point.y
    n = len(polygon)
    for i in range(n):
        j = (i + 1) % n
        xi, yi = polygon[i].x, polygon[i].y
        xj, yj = polygon[j].x, polygon[j].y
        if (x == xi and y == yi) or (x == xj and y == yj):
            return True
        dx, dy = xj - xi, yj - yi
        if abs(dy * (x - xi) - dx * (y - yi)) < 1e-9:
            if min(xi, xj) <= x <= max(xi, xj) and min(yi, yj) <= y <= max(yi, yj):
                return True
    return False


def enclosure(point, epolygons):
    for poly in epolygons:
        if in_polygon(point, poly) or on_edge(point, poly):
            return True
    return False

def turf(point, tpolygons):
    for poly in tpolygons:
        if in_polygon(point, poly) or on_edge(point, poly):
            return True
    return False


def get_neighbors(point, epolygons, tpolygons):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        neighbor = Point(point.x + dx, point.y + dy)
        if not (0 <= neighbor.x < MAX and 0 <= neighbor.y < MAX):
            continue
        if enclosure(neighbor, epolygons):
            continue
        cost = 1.5 if turf(neighbor, tpolygons) else 1.0
        neighbors.append((neighbor, cost))
    return neighbors





def heuristic(point, dest):
    return ((point.x - dest.x) ** 2 + (point.y - dest.y) ** 2) ** 0.5



def astar(source, dest, epolygons, tpolygons):
    queue = PriorityQueue()
    queue.push((source, [source], 0), heuristic(source, dest))
    visited = {}
    count = 0

    while not queue.isEmpty():
        current, path, cost = queue.pop()
        count += 1

        if current == dest:
            print("A* found a path of length", len(path), "with", count, "nodes expanded")
            return path

        if (current.x, current.y) in visited and visited[(current.x, current.y)] <= cost:
            continue
        visited[(current.x, current.y)] = cost

        for nbr, step in get_neighbors(current, epolygons, tpolygons):
            new_cost = cost + step
            if (nbr.x, nbr.y) in visited and visited[(nbr.x, nbr.y)] <= new_cost:
                continue
            total = new_cost + heuristic(nbr, dest)
            queue.push((nbr, path + [nbr], new_cost), total)

    print("A* did not find a path")
    return None
