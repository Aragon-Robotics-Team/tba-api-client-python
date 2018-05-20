# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    OpenAPI spec version: 3.03.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import net.thefletcher.tbaapi.v3client
from net.thefletcher.tbaapi.v3client.models.elimination_alliance_status import EliminationAllianceStatus  # noqa: E501
from net.thefletcher.tbaapi.v3client.rest import ApiException


class TestEliminationAllianceStatus(unittest.TestCase):
    """EliminationAllianceStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEliminationAllianceStatus(self):
        """Test EliminationAllianceStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = net.thefletcher.tbaapi.v3client.models.elimination_alliance_status.EliminationAllianceStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
