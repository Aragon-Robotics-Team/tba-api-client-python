# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    The version of the OpenAPI document: 3.5.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import tbaapiv3client
from tbaapiv3client.models.event_district_points_points import EventDistrictPointsPoints  # noqa: E501
from tbaapiv3client.rest import ApiException


class TestEventDistrictPointsPoints(unittest.TestCase):
    """EventDistrictPointsPoints unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEventDistrictPointsPoints(self):
        """Test EventDistrictPointsPoints"""
        # FIXME: construct object with mandatory attributes with example values
        # model = tbaapiv3client.models.event_district_points_points.EventDistrictPointsPoints()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
