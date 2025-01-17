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
from tbaapiv3client.api.tba_api import TBAApi  # noqa: E501
from tbaapiv3client.rest import ApiException


class TestTBAApi(unittest.TestCase):
    """TBAApi unit test stubs"""

    def setUp(self):
        self.api = tbaapiv3client.api.tba_api.TBAApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_status(self):
        """Test case for get_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
