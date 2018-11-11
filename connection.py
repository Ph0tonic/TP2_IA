#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Connection:
    """
    Class connection which allow to link two cities, contains the length of this connection
    """

    def __init__(self, city1, city2, distance):
        """ Constructor

        :param city1: City n°1
        :param city2: City n°2
        :param distance: distance between the 2 cities
        """
        self.city1 = city1
        self.city2 = city2
        self.distance = distance

    def get_linked(self, city):
        """ get the other city connected via this connection

        :param city: city from where the connection is coming from
        :return: city where the connection is going
        """
        return self.city1 if city != self.city1 else self.city2
    
    def __str__(self):
        """
        To String function for debug
        """
        return str(self.city1)+" - "+str(self.city2)