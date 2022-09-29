from code_handout import Astar, Map

def main():
    #In the line below, change task number to see the different paths
    map = Map.Map_Obj(task=4)

    #Gets start and goal positions
    start = map.get_start_pos()
    goal = map.get_goal_pos()

    #Gets the generated path from the a* algorithm
    path = Astar.a_star(map, start, goal)

    #Loops thorugh the path and creates visualization
    for item in path:
        map.str_map[item[0], item [1]] = ' '
    map.show_map()

main()
