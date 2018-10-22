from city import City
from connection import Connection

def load_config():
    towns = {}
    connections = []
    with open("positions.txt") as file:
        for line in file:
            name, x, y = line.split(" ")
            towns[name] = City(name,x, y)
    
    with open("connections.txt") as file:
        for line in file:
            city_name1, city_name2, distance = line.split(" ")
            city1 = towns[city_name1]
            city2 = towns[city_name2]
            connection = Connection(city1,city2,distance)
            city1.add_connection(connection)
            city1.add_connectiond(connection)
    
    return towns, connections

class Node:
    def __init(self, city, g, h):
        self.city = city
        self._g = g
        self._h = h
    
    def g(self):
        return self._g

    def h(self):
        return self._h

def a_star_search(town1, town2, heuristique):
    explored_node = []
    to_explore = []

    node = Node(town1,0,heuristique(town1))


if __name__ == '__main__':
    towns, connections = load_config()

    h4 = lambda city:city.h4()

    a_star_search(towns['Copenhagen'], towns['Lisbon'],h4)
