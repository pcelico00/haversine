"""
Created on May 18, 2016

@author: Paul Celicourt
@email: pc@sofiot.com
"""

import math


class Haversine(object):
    def __init__(self):
        self.earth_radius = 6373  # km

    @staticmethod
    def convert_degree_to_radian(value_in_degree):
        value_in_radian = math.radians(value_in_degree)
        return value_in_radian

    def compute_distance_between_lat_lon_pairs(self, origin_lat_lon_pair, destination_lat_lon_pair):
        origin_latitude, origin_longitude = origin_lat_lon_pair
        destination_latitude, destination_longitude = destination_lat_lon_pair

        assert (-180 <= origin_longitude <= 180)
        assert (-180 <= destination_longitude <= 180)
        assert (-90 <= origin_latitude <= 90)
        assert (-90 <= destination_latitude <= 90)

        origin_latitude_in_radian = math.radians(origin_latitude)
        origin_longitude_in_radian = math.radians(origin_longitude)
        destination_latitude_in_radian = math.radians(destination_latitude)
        destination_longitude_in_radian = math.radians(destination_longitude)

        latitude_difference_in_radian = destination_latitude_in_radian - origin_latitude_in_radian
        longitude_difference_in_radian = destination_longitude_in_radian - origin_longitude_in_radian

        haversine_of_central_angle = (math.sin(latitude_difference_in_radian / 2)) ** 2 + \
                                     math.cos(destination_latitude_in_radian) * math.cos(origin_latitude_in_radian) * \
                                     (math.sin(longitude_difference_in_radian / 2)) ** 2

        central_angle = 2 * math.atan2(math.sqrt(haversine_of_central_angle), math.sqrt(1 - haversine_of_central_angle))
        distance_between_lat_lon_pairs = self.earth_radius * central_angle

        return distance_between_lat_lon_pairs
