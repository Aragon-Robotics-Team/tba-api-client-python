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
from tbaapiv3client.models.match_score_breakdown2018 import MatchScoreBreakdown2018  # noqa: E501
from tbaapiv3client.rest import ApiException


class TestMatchScoreBreakdown2018(unittest.TestCase):
    """MatchScoreBreakdown2018 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMatchScoreBreakdown2018(self):
        """Test MatchScoreBreakdown2018"""
        # FIXME: construct object with mandatory attributes with example values
        # model = tbaapiv3client.models.match_score_breakdown2018.MatchScoreBreakdown2018()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
