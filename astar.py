#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class MapHeuristic:
    """Class to represent heuristic methods
    """

    @staticmethod
    def h0(city1,city2):
        """ Heuristique 0 to evaluate the cost between to cities
        h(c1,c2)=0

        :param city1: first city
        :param city2: second city
        """
        return 0
    
    @staticmethod
    def h1(city1,city2):
        """ Heuristique 1 to evaluate the cost between to cities
        h(c1,c2)=abs(city1.x-city2.x)

        :param city1: first city
        :param city2: second city
        """
        return abs(city1.x-city2.x)

    @staticmethod
    def h2(city1,city2):
        """ Heuristique 2 to evaluate the cost between to cities
        h(c1,c2)=abs(city1.y-city2.y)

        :param city1: first city
        :param city2: second city
        """
        return abs(city1.y-city2.y)

    @staticmethod 
    def h3(city1,city2):
        """ Heuristique 3 to evaluate the cost between to cities
        h(c1,c2)=math.sqrt((c1.x-c2.x)**2+(c1.y-c2.y)**2)

        :param city1: first city
        :param city2: second city
        """
        return math.sqrt((city1.x-city2.x)**2+(city1.y-city2.y)**2)
    
    @staticmethod
    def h4(city1,city2):
        """ Heuristique 4 to evaluate the cost between to cities
        h(c1,c2)=h1(c1,c2)+h2(c1,c2)

        :param city1: first city
        :param city2: second city
        """
        return MapHeuristic.h1(city1,city2)+MapHeuristic.h2(city1,city2)

def build_path(came_from, current):
    """ Create the path from nodes and return it
    """
    total_path = []
    total_path.append(current)
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)

    return reversed(total_path)

def a_star_search(city_start, city_dest, heuristic):
    """ A* algorithm to find the best way between two cities
    
    :param city_start: city where to start
    :param city_dest: destination city
    :param heuristic: heuristic to evaluate th distance between two cities
    :returns path(list), total_cost
    """

    infinity = float("inf")

    # For statistics purpose
    nb_iteration = 0
    
    # Node evaluated
    closed_set = set()

    # Node known but not evaluated yet, initialized with startNode
    open_set = set()
    open_set.add(city_start)

    # Dictionnary of node with the best to come from
    came_from = {}

    # Cost of the node to go from start
    g_score = {}

    # The cost of going from start to start is zero
    g_score[city_start] = 0

    # Total cost of getting from the start to the destination by passing by that node. That value is partly known, partly heuristic
    f_score = {}

    # The f_score of the first node is completely heuristic
    f_score[city_start] = heuristic(city_start, city_dest)

    # Evaluate node till we have one
    while len(open_set) > 0:
        # Statistics count number of cycles
        nb_iteration += 1

        # Find best node
        current = min(open_set, key=lambda x:f_score.get(x,infinity))

        # Final city reached
        if current == city_dest:
            return (build_path(came_from, current), g_score[current], nb_iteration)

        # Renove evaluated node from the set of node to explore and add it to the explored node
        open_set.remove(current)
        closed_set.add(current)

        # Explore all neighbor city and add them, in open_set
        for connection in current.connections:
            # get the connected city
            neighbor = connection.get_linked(current)

            # Check if the city is already known and evaluated
            if neighbor in closed_set:
                continue # if so ignore it

            # Calculate g_score for this path
            tentative_gscore = g_score.get(current,infinity) + connection.distance

            # Check if this node is known
            if neighbor not in open_set:
                open_set.add(neighbor) # new node reached
            elif tentative_gscore >= g_score.get(neighbor,infinity):
                continue # Already known but not a better path
    
            # New best path to go to this city, update came_from, g_score and f_score
            came_from[neighbor] = current
            g_score[neighbor] = tentative_gscore
            f_score[neighbor] = g_score.get(neighbor,infinity) + heuristic(neighbor, city_dest)
