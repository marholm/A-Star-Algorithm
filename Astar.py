class Node:

    def __init__(self, position, parent):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f


# Implementation of the A-star algorithm
def a_star(map, start, end):
    # Create list for open nodes (frontier) and closed nodes (not goal)
    open = []
    closed = []
    # Create a start and goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)
    # Add the start node to the frontier
    open.append(start_node)

    # Loop until the open list is empty
    while len(open) > 0:
        open.sort()
        current_node = open.pop(0)
        closed.append(current_node)  # Add current node to the closed list

        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        # Unzip the current node position
        [x, y] = current_node.position

        # Get children / neighbours
        neighbours = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]

        # Loop neighbours
        for next in neighbours:
            map_value = map.get_cell_value(next)  # Get value from map
            if map_value == -1:
                continue

            neighbour = Node(next, current_node)
            if neighbour in closed:
                continue

            # Generate heuristics
            neighbour.g = current_node.g+map.get_cell_value(neighbour.position)
            neighbour.h = abs(neighbour.position[0] - goal_node.position[0]) + abs(
                neighbour.position[1] - goal_node.position[1])
            neighbour.f = neighbour.g + neighbour.h

            # Check if neighbour is in open list and if it has a lower f value
            if add_to_open(open, neighbour) == True:
                open.append(neighbour)


def add_to_open(open, neighbour):
    for node in open:
        if neighbour == node:
            if neighbour.g >= node.g:
                return False
    return True

