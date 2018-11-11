#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Programe which allow a user to find the shortest way between two cities

:param argv[1]: Start city
:param argv[2]: Dest city
:param argv[3]: Heuristique
:returns: List of the cities to go through

Correct syntax:
python app.py start_city dest_city heuristique

Concrete example :
python app.py Copenhagen Lisbon h0

List of available heuristiques:
    h0 -> 0
    h1 -> abs(city1.x-city2.x)
    h2 -> abs(city1.y-city2.y)
    h3 -> math.sqrt((c1.x-c2.x)**2+(c1.y-c2.y)**2)
    h4 -> h1(c1,c2)+h2(c1,c2)

Notes: Cities' names are case insensitive

Dependencies:
    positions.txt - Contains a list of all cities
    connections.txt - Contains a list of all connections between cities
"""

from city import City
from connection import Connection
from astar import a_star_search, MapHeuristic

def load_config():
    """Load config files

    :returns: map<city_name string, city City> of the cities
    """
    cities = {}
    with open("positions.txt") as file:
        for line in file:
            name, x, y = line.split(" ")
            cities[name.lower()] = City(name,int(x), int(y))
    
    with open("connections.txt") as file:
        for line in file:
            city_name1, city_name2, distance = line.split(" ")
            city1 = cities[city_name1.lower()]
            city2 = cities[city_name2.lower()]
            connection = Connection(city1,city2,int(distance))
            city1.add_connection(connection)
            city2.add_connection(connection)
    
    return cities

def check_city(cities, city_name):
    """Check the validity of a city's name

    :param cities: map of the cities
    :param city_name: name of the city
    :returns: City object associted with this name
    """
    if city_name.lower() not in cities:
        print("Error, invalid input:")
        print(f"'{city_name}' is not a valid city")
        exit(-2)
    
    return cities[city_name.lower()]

def check_heuristique(heuristiques, heuristique_name):
    method_to_call = getattr(heuristiques, heuristique_name)
    return method_to_call

    
def main():
    """main program

    :param argv[1]: Start city
    :param argv[2]: Dest city
    :param argv[3]: Heuristique
    :returns: List of the cities to go through

    Correct syntax:
    python app.py start_city dest_city heuristique

    Concrete example :
    python app.py Copenhagen Lisbon h0

    List of available heuristiques:
        h0 -> 0
        h1 -> abs(city1.x-city2.x)
        h2 -> abs(city1.y-city2.y)
        h3 -> math.sqrt((c1.x-c2.x)**2+(c1.y-c2.y)**2)
        h4 -> h1(c1,c2)+h2(c1,c2)

    Notes: Cities' names are case insensitive
    Dependencies:
        positions.txt - Contains a list of all cities
        connections.txt - Contains a list of all connections between cities
    """
    import sys
    if len(sys.argv) != 4:
        print("Invalid use!")
        print(main.__doc__)
        exit(-1)

    cities = load_config()

    start_city = check_city(cities, sys.argv[1])
    dest_city = check_city(cities, sys.argv[2])
    heuristique = check_heuristique(MapHeuristic, sys.argv[3])

    cities, total_length = a_star_search(start_city, dest_city ,heuristique)
    for city in cities:
        print(str(city))
    print(f"Total Length : {total_length}")

if __name__ == '__main__':
    main()