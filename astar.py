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

def reconstruct_path(came_from, current):
    """ Create the path from nodes and return it
    """
    total_path = []
    total_path.append(current)
    total_length = 0
    previous_city = current
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)

        # Length of the path
        connection = current.get_connection_to(previous_city)
        total_length += connection.distance
        previous_city = current

    return reversed(total_path), total_length

def a_star_search(city_start, city_dest, heuristic):
    """ A* algorithm to fin the best way between two cities
    
    :param city_start: city where to start
    :param city_dest: destination city
    :param heuristic: heuristic to evaluate th distance between two cities
    :returns path(list), total_cost
    """

    infinity = float("inf")
    
    # The set of nodes already evaluated
    closed_set = set()

    # The set of currently discovered nodes that are not evaluated yet.
    # Initially, only the start node is known.
    open_set = set()
    open_set.add(city_start)

    # For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, cameFrom will eventually contain the
    # most efficient previous step.
    came_from = {}

    # For each node, the cost of getting from the start node to that node.
    g_score = {}

    # The cost of going from start to start is zero.
    g_score[city_start] = 0

    # For each node, the total cost of getting from the start node to the goal
    # by passing by that node. That value is partly known, partly heuristic.
    f_score = {}

    # For the first node, that value is completely heuristic.
    f_score[city_start] = heuristic(city_start, city_dest)

    while len(open_set) > 0:
        current = min(open_set, key=lambda x:f_score.get(x,infinity))
        if current == city_dest:
            return reconstruct_path(came_from, current)

        open_set.remove(current)
        closed_set.add(current)

        for connection in current.connections:
            neighbor = connection.get_linked(current) 
            if neighbor in closed_set:
                continue		# Ignore the neighbor which is already evaluated.

            # The distance from start to a neighbor
            tentative_gscore = g_score.get(current,infinity) + connection.distance

            if neighbor not in open_set:	# Discover a new node
                open_set.add(neighbor)
            elif tentative_gscore >= g_score.get(neighbor,infinity):
                continue		# This is not a better path.
    
            # This path is the best until now. Record it!
            came_from[neighbor] = current
            g_score[neighbor] = tentative_gscore
            f_score[neighbor] = g_score.get(neighbor,infinity) + heuristic(neighbor, city_dest)
