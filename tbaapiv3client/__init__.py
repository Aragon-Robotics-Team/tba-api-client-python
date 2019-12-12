# coding: utf-8

# flake8: noqa

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    The version of the OpenAPI document: 3.5.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "3.5.1"

# import apis into sdk package
from tbaapiv3client.api.tba_api import TBAApi
from tbaapiv3client.api.district_api import DistrictApi
from tbaapiv3client.api.event_api import EventApi
from tbaapiv3client.api.list_api import ListApi
from tbaapiv3client.api.match_api import MatchApi
from tbaapiv3client.api.team_api import TeamApi

# import ApiClient
from tbaapiv3client.api_client import ApiClient
from tbaapiv3client.configuration import Configuration
from tbaapiv3client.exceptions import OpenApiException
from tbaapiv3client.exceptions import ApiTypeError
from tbaapiv3client.exceptions import ApiValueError
from tbaapiv3client.exceptions import ApiKeyError
from tbaapiv3client.exceptions import ApiException
# import models into sdk package
from tbaapiv3client.models.api_status import APIStatus
from tbaapiv3client.models.api_status_app_version import APIStatusAppVersion
from tbaapiv3client.models.award import Award
from tbaapiv3client.models.award_recipient import AwardRecipient
from tbaapiv3client.models.district_list import DistrictList
from tbaapiv3client.models.district_ranking import DistrictRanking
from tbaapiv3client.models.district_ranking_event_points import DistrictRankingEventPoints
from tbaapiv3client.models.elimination_alliance import EliminationAlliance
from tbaapiv3client.models.elimination_alliance_backup import EliminationAllianceBackup
from tbaapiv3client.models.elimination_alliance_status import EliminationAllianceStatus
from tbaapiv3client.models.event import Event
from tbaapiv3client.models.event_district_points import EventDistrictPoints
from tbaapiv3client.models.event_district_points_points import EventDistrictPointsPoints
from tbaapiv3client.models.event_district_points_tiebreakers import EventDistrictPointsTiebreakers
from tbaapiv3client.models.event_insights import EventInsights
from tbaapiv3client.models.event_insights2016 import EventInsights2016
from tbaapiv3client.models.event_insights2017 import EventInsights2017
from tbaapiv3client.models.event_insights2018 import EventInsights2018
from tbaapiv3client.models.event_op_rs import EventOPRs
from tbaapiv3client.models.event_ranking import EventRanking
from tbaapiv3client.models.event_ranking_extra_stats_info import EventRankingExtraStatsInfo
from tbaapiv3client.models.event_ranking_rankings import EventRankingRankings
from tbaapiv3client.models.event_ranking_sort_order_info import EventRankingSortOrderInfo
from tbaapiv3client.models.event_simple import EventSimple
from tbaapiv3client.models.match import Match
from tbaapiv3client.models.match_alliance import MatchAlliance
from tbaapiv3client.models.match_score_breakdown2015 import MatchScoreBreakdown2015
from tbaapiv3client.models.match_score_breakdown2015_alliance import MatchScoreBreakdown2015Alliance
from tbaapiv3client.models.match_score_breakdown2016 import MatchScoreBreakdown2016
from tbaapiv3client.models.match_score_breakdown2016_alliance import MatchScoreBreakdown2016Alliance
from tbaapiv3client.models.match_score_breakdown2017 import MatchScoreBreakdown2017
from tbaapiv3client.models.match_score_breakdown2017_alliance import MatchScoreBreakdown2017Alliance
from tbaapiv3client.models.match_score_breakdown2018 import MatchScoreBreakdown2018
from tbaapiv3client.models.match_score_breakdown2018_alliance import MatchScoreBreakdown2018Alliance
from tbaapiv3client.models.match_score_breakdown2019 import MatchScoreBreakdown2019
from tbaapiv3client.models.match_score_breakdown2019_alliance import MatchScoreBreakdown2019Alliance
from tbaapiv3client.models.match_simple import MatchSimple
from tbaapiv3client.models.match_simple_alliances import MatchSimpleAlliances
from tbaapiv3client.models.match_timeseries2018 import MatchTimeseries2018
from tbaapiv3client.models.match_videos import MatchVideos
from tbaapiv3client.models.media import Media
from tbaapiv3client.models.team import Team
from tbaapiv3client.models.team_event_status import TeamEventStatus
from tbaapiv3client.models.team_event_status_alliance import TeamEventStatusAlliance
from tbaapiv3client.models.team_event_status_alliance_backup import TeamEventStatusAllianceBackup
from tbaapiv3client.models.team_event_status_playoff import TeamEventStatusPlayoff
from tbaapiv3client.models.team_event_status_rank import TeamEventStatusRank
from tbaapiv3client.models.team_event_status_rank_ranking import TeamEventStatusRankRanking
from tbaapiv3client.models.team_event_status_rank_sort_order_info import TeamEventStatusRankSortOrderInfo
from tbaapiv3client.models.team_robot import TeamRobot
from tbaapiv3client.models.team_simple import TeamSimple
from tbaapiv3client.models.wlt_record import WLTRecord
from tbaapiv3client.models.webcast import Webcast

