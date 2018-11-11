#!/usr/bin/env python
# -*- coding: utf-8 -*-

class City:
    """
    Class city which represent a City
    """

    def __init__(self, name, x, y):
        """ Constructor

        :param name: name of the city
        :param x: x position of this city
        :param y: y position of this city
        """
        self.name = name
        self.x = x
        self.y = y
        self.connections = []

    def add_connection(self, connection):
        """ Add a connection

        :param connection: Connection to add
        """
        self.connections.append(connection)

    def remove_connection(self, connection):
        """Remove a given connection from the connections available in this city
        """
        self.connections.remove(connection)

    def get_connection_to(self, city):
        for connection in self.connections:
            if connection.get_linked(self) == city:
                return connection
        raise ValueError("No connection to this city")

    def __str__(self):
        """
        To String function for debug
        """
        return self.name
