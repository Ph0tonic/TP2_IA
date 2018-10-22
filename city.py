import math

class City:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.connections = []
    
    def h0(self, city):
        return 0
    
    def h1(self, city):
        return abs(self.x-city.x)

    def h2(self, city):
        return abs(self.y-city.y)
        
    def h3(self, city):
        return math.sqrt((self.x-city.x)^2+(self.y-city.y)^2)
        
    def h4(self, city):
        return self.h1(city)+self.h2(city)

    def add_connection(self, connection):
        self.connections.append(connection)

    def remove_connection(self, connection):
        self.connections.remove(connection)

    def get_connections(self):
        return self.connections
