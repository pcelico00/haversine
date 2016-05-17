"""
Created on May 18, 2016

@author: Paul Celicourt
@email: pc@sofiot.com
"""

import unittest

from haversine import Haversine


class HaversineSuperTest(unittest.TestCase):
    def setUp(self):
        self.harversine_object = Haversine()


class HaversineTest(HaversineSuperTest):
    def test_compute_distance_between_lat_lon_pairs(self):
        distance = self.harversine_object.compute_distance_between_lat_lon_pairs((52.2296756, 21.0122287),
                                                                                 (52.406374, 16.9251681))
        self.assertAlmostEqual(distance, 278.545589351, 3)
