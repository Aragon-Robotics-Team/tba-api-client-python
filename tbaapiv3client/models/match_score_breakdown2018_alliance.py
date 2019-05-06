# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    OpenAPI spec version: 3.04.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class MatchScoreBreakdown2018Alliance(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'adjust_points': 'int',
        'auto_ownership_points': 'int',
        'auto_points': 'int',
        'auto_quest_ranking_point': 'bool',
        'auto_robot1': 'str',
        'auto_robot2': 'str',
        'auto_robot3': 'str',
        'auto_run_points': 'int',
        'auto_scale_ownership_sec': 'int',
        'auto_switch_at_zero': 'bool',
        'auto_switch_ownership_sec': 'int',
        'endgame_points': 'int',
        'endgame_robot1': 'str',
        'endgame_robot2': 'str',
        'endgame_robot3': 'str',
        'face_the_boss_ranking_point': 'bool',
        'foul_count': 'int',
        'foul_points': 'int',
        'rp': 'int',
        'tech_foul_count': 'int',
        'teleop_ownership_points': 'int',
        'teleop_points': 'int',
        'teleop_scale_boost_sec': 'int',
        'teleop_scale_force_sec': 'int',
        'teleop_scale_ownership_sec': 'int',
        'teleop_switch_boost_sec': 'int',
        'teleop_switch_force_sec': 'int',
        'teleop_switch_ownership_sec': 'int',
        'total_points': 'int',
        'vault_boost_played': 'int',
        'vault_boost_total': 'int',
        'vault_force_played': 'int',
        'vault_force_total': 'int',
        'vault_levitate_played': 'int',
        'vault_levitate_total': 'int',
        'vault_points': 'int',
        'tba_game_data': 'str'
    }

    attribute_map = {
        'adjust_points': 'adjustPoints',
        'auto_ownership_points': 'autoOwnershipPoints',
        'auto_points': 'autoPoints',
        'auto_quest_ranking_point': 'autoQuestRankingPoint',
        'auto_robot1': 'autoRobot1',
        'auto_robot2': 'autoRobot2',
        'auto_robot3': 'autoRobot3',
        'auto_run_points': 'autoRunPoints',
        'auto_scale_ownership_sec': 'autoScaleOwnershipSec',
        'auto_switch_at_zero': 'autoSwitchAtZero',
        'auto_switch_ownership_sec': 'autoSwitchOwnershipSec',
        'endgame_points': 'endgamePoints',
        'endgame_robot1': 'endgameRobot1',
        'endgame_robot2': 'endgameRobot2',
        'endgame_robot3': 'endgameRobot3',
        'face_the_boss_ranking_point': 'faceTheBossRankingPoint',
        'foul_count': 'foulCount',
        'foul_points': 'foulPoints',
        'rp': 'rp',
        'tech_foul_count': 'techFoulCount',
        'teleop_ownership_points': 'teleopOwnershipPoints',
        'teleop_points': 'teleopPoints',
        'teleop_scale_boost_sec': 'teleopScaleBoostSec',
        'teleop_scale_force_sec': 'teleopScaleForceSec',
        'teleop_scale_ownership_sec': 'teleopScaleOwnershipSec',
        'teleop_switch_boost_sec': 'teleopSwitchBoostSec',
        'teleop_switch_force_sec': 'teleopSwitchForceSec',
        'teleop_switch_ownership_sec': 'teleopSwitchOwnershipSec',
        'total_points': 'totalPoints',
        'vault_boost_played': 'vaultBoostPlayed',
        'vault_boost_total': 'vaultBoostTotal',
        'vault_force_played': 'vaultForcePlayed',
        'vault_force_total': 'vaultForceTotal',
        'vault_levitate_played': 'vaultLevitatePlayed',
        'vault_levitate_total': 'vaultLevitateTotal',
        'vault_points': 'vaultPoints',
        'tba_game_data': 'tba_gameData'
    }

    def __init__(self, adjust_points=None, auto_ownership_points=None, auto_points=None, auto_quest_ranking_point=None, auto_robot1=None, auto_robot2=None, auto_robot3=None, auto_run_points=None, auto_scale_ownership_sec=None, auto_switch_at_zero=None, auto_switch_ownership_sec=None, endgame_points=None, endgame_robot1=None, endgame_robot2=None, endgame_robot3=None, face_the_boss_ranking_point=None, foul_count=None, foul_points=None, rp=None, tech_foul_count=None, teleop_ownership_points=None, teleop_points=None, teleop_scale_boost_sec=None, teleop_scale_force_sec=None, teleop_scale_ownership_sec=None, teleop_switch_boost_sec=None, teleop_switch_force_sec=None, teleop_switch_ownership_sec=None, total_points=None, vault_boost_played=None, vault_boost_total=None, vault_force_played=None, vault_force_total=None, vault_levitate_played=None, vault_levitate_total=None, vault_points=None, tba_game_data=None):  # noqa: E501
        """MatchScoreBreakdown2018Alliance - a model defined in OpenAPI"""  # noqa: E501

        self._adjust_points = None
        self._auto_ownership_points = None
        self._auto_points = None
        self._auto_quest_ranking_point = None
        self._auto_robot1 = None
        self._auto_robot2 = None
        self._auto_robot3 = None
        self._auto_run_points = None
        self._auto_scale_ownership_sec = None
        self._auto_switch_at_zero = None
        self._auto_switch_ownership_sec = None
        self._endgame_points = None
        self._endgame_robot1 = None
        self._endgame_robot2 = None
        self._endgame_robot3 = None
        self._face_the_boss_ranking_point = None
        self._foul_count = None
        self._foul_points = None
        self._rp = None
        self._tech_foul_count = None
        self._teleop_ownership_points = None
        self._teleop_points = None
        self._teleop_scale_boost_sec = None
        self._teleop_scale_force_sec = None
        self._teleop_scale_ownership_sec = None
        self._teleop_switch_boost_sec = None
        self._teleop_switch_force_sec = None
        self._teleop_switch_ownership_sec = None
        self._total_points = None
        self._vault_boost_played = None
        self._vault_boost_total = None
        self._vault_force_played = None
        self._vault_force_total = None
        self._vault_levitate_played = None
        self._vault_levitate_total = None
        self._vault_points = None
        self._tba_game_data = None
        self.discriminator = None

        if adjust_points is not None:
            self.adjust_points = adjust_points
        if auto_ownership_points is not None:
            self.auto_ownership_points = auto_ownership_points
        if auto_points is not None:
            self.auto_points = auto_points
        if auto_quest_ranking_point is not None:
            self.auto_quest_ranking_point = auto_quest_ranking_point
        if auto_robot1 is not None:
            self.auto_robot1 = auto_robot1
        if auto_robot2 is not None:
            self.auto_robot2 = auto_robot2
        if auto_robot3 is not None:
            self.auto_robot3 = auto_robot3
        if auto_run_points is not None:
            self.auto_run_points = auto_run_points
        if auto_scale_ownership_sec is not None:
            self.auto_scale_ownership_sec = auto_scale_ownership_sec
        if auto_switch_at_zero is not None:
            self.auto_switch_at_zero = auto_switch_at_zero
        if auto_switch_ownership_sec is not None:
            self.auto_switch_ownership_sec = auto_switch_ownership_sec
        if endgame_points is not None:
            self.endgame_points = endgame_points
        if endgame_robot1 is not None:
            self.endgame_robot1 = endgame_robot1
        if endgame_robot2 is not None:
            self.endgame_robot2 = endgame_robot2
        if endgame_robot3 is not None:
            self.endgame_robot3 = endgame_robot3
        if face_the_boss_ranking_point is not None:
            self.face_the_boss_ranking_point = face_the_boss_ranking_point
        if foul_count is not None:
            self.foul_count = foul_count
        if foul_points is not None:
            self.foul_points = foul_points
        if rp is not None:
            self.rp = rp
        if tech_foul_count is not None:
            self.tech_foul_count = tech_foul_count
        if teleop_ownership_points is not None:
            self.teleop_ownership_points = teleop_ownership_points
        if teleop_points is not None:
            self.teleop_points = teleop_points
        if teleop_scale_boost_sec is not None:
            self.teleop_scale_boost_sec = teleop_scale_boost_sec
        if teleop_scale_force_sec is not None:
            self.teleop_scale_force_sec = teleop_scale_force_sec
        if teleop_scale_ownership_sec is not None:
            self.teleop_scale_ownership_sec = teleop_scale_ownership_sec
        if teleop_switch_boost_sec is not None:
            self.teleop_switch_boost_sec = teleop_switch_boost_sec
        if teleop_switch_force_sec is not None:
            self.teleop_switch_force_sec = teleop_switch_force_sec
        if teleop_switch_ownership_sec is not None:
            self.teleop_switch_ownership_sec = teleop_switch_ownership_sec
        if total_points is not None:
            self.total_points = total_points
        if vault_boost_played is not None:
            self.vault_boost_played = vault_boost_played
        if vault_boost_total is not None:
            self.vault_boost_total = vault_boost_total
        if vault_force_played is not None:
            self.vault_force_played = vault_force_played
        if vault_force_total is not None:
            self.vault_force_total = vault_force_total
        if vault_levitate_played is not None:
            self.vault_levitate_played = vault_levitate_played
        if vault_levitate_total is not None:
            self.vault_levitate_total = vault_levitate_total
        if vault_points is not None:
            self.vault_points = vault_points
        if tba_game_data is not None:
            self.tba_game_data = tba_game_data

    @property
    def adjust_points(self):
        """Gets the adjust_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The adjust_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._adjust_points

    @adjust_points.setter
    def adjust_points(self, adjust_points):
        """Sets the adjust_points of this MatchScoreBreakdown2018Alliance.


        :param adjust_points: The adjust_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._adjust_points = adjust_points

    @property
    def auto_ownership_points(self):
        """Gets the auto_ownership_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The auto_ownership_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._auto_ownership_points

    @auto_ownership_points.setter
    def auto_ownership_points(self, auto_ownership_points):
        """Sets the auto_ownership_points of this MatchScoreBreakdown2018Alliance.


        :param auto_ownership_points: The auto_ownership_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._auto_ownership_points = auto_ownership_points

    @property
    def auto_points(self):
        """Gets the auto_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The auto_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._auto_points

    @auto_points.setter
    def auto_points(self, auto_points):
        """Sets the auto_points of this MatchScoreBreakdown2018Alliance.


        :param auto_points: The auto_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._auto_points = auto_points

    @property
    def auto_quest_ranking_point(self):
        """Gets the auto_quest_ranking_point of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The auto_quest_ranking_point of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: bool
        """
        return self._auto_quest_ranking_point

    @auto_quest_ranking_point.setter
    def auto_quest_ranking_point(self, auto_quest_ranking_point):
        """Sets the auto_quest_ranking_point of this MatchScoreBreakdown2018Alliance.


        :param auto_quest_ranking_point: The auto_quest_ranking_point of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: bool
        """

        self._auto_quest_ranking_point = auto_quest_ranking_point

    @property
    def auto_robot1(self):
        """Gets the auto_robot1 of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The auto_robot1 of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: str
        """
        return self._auto_robot1

    @auto_robot1.setter
    def auto_robot1(self, auto_robot1):
        """Sets the auto_robot1 of this MatchScoreBreakdown2018Alliance.


        :param auto_robot1: The auto_robot1 of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: str
        """

        self._auto_robot1 = auto_robot1

    @property
    def auto_robot2(self):
        """Gets the auto_robot2 of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The auto_robot2 of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: str
        """
        return self._auto_robot2

    @auto_robot2.setter
    def auto_robot2(self, auto_robot2):
        """Sets the auto_robot2 of this MatchScoreBreakdown2018Alliance.


        :param auto_robot2: The auto_robot2 of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: str
        """

        self._auto_robot2 = auto_robot2

    @property
    def auto_robot3(self):
        """Gets the auto_robot3 of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The auto_robot3 of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: str
        """
        return self._auto_robot3

    @auto_robot3.setter
    def auto_robot3(self, auto_robot3):
        """Sets the auto_robot3 of this MatchScoreBreakdown2018Alliance.


        :param auto_robot3: The auto_robot3 of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: str
        """

        self._auto_robot3 = auto_robot3

    @property
    def auto_run_points(self):
        """Gets the auto_run_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The auto_run_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._auto_run_points

    @auto_run_points.setter
    def auto_run_points(self, auto_run_points):
        """Sets the auto_run_points of this MatchScoreBreakdown2018Alliance.


        :param auto_run_points: The auto_run_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._auto_run_points = auto_run_points

    @property
    def auto_scale_ownership_sec(self):
        """Gets the auto_scale_ownership_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The auto_scale_ownership_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._auto_scale_ownership_sec

    @auto_scale_ownership_sec.setter
    def auto_scale_ownership_sec(self, auto_scale_ownership_sec):
        """Sets the auto_scale_ownership_sec of this MatchScoreBreakdown2018Alliance.


        :param auto_scale_ownership_sec: The auto_scale_ownership_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._auto_scale_ownership_sec = auto_scale_ownership_sec

    @property
    def auto_switch_at_zero(self):
        """Gets the auto_switch_at_zero of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The auto_switch_at_zero of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: bool
        """
        return self._auto_switch_at_zero

    @auto_switch_at_zero.setter
    def auto_switch_at_zero(self, auto_switch_at_zero):
        """Sets the auto_switch_at_zero of this MatchScoreBreakdown2018Alliance.


        :param auto_switch_at_zero: The auto_switch_at_zero of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: bool
        """

        self._auto_switch_at_zero = auto_switch_at_zero

    @property
    def auto_switch_ownership_sec(self):
        """Gets the auto_switch_ownership_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The auto_switch_ownership_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._auto_switch_ownership_sec

    @auto_switch_ownership_sec.setter
    def auto_switch_ownership_sec(self, auto_switch_ownership_sec):
        """Sets the auto_switch_ownership_sec of this MatchScoreBreakdown2018Alliance.


        :param auto_switch_ownership_sec: The auto_switch_ownership_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._auto_switch_ownership_sec = auto_switch_ownership_sec

    @property
    def endgame_points(self):
        """Gets the endgame_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The endgame_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._endgame_points

    @endgame_points.setter
    def endgame_points(self, endgame_points):
        """Sets the endgame_points of this MatchScoreBreakdown2018Alliance.


        :param endgame_points: The endgame_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._endgame_points = endgame_points

    @property
    def endgame_robot1(self):
        """Gets the endgame_robot1 of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The endgame_robot1 of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: str
        """
        return self._endgame_robot1

    @endgame_robot1.setter
    def endgame_robot1(self, endgame_robot1):
        """Sets the endgame_robot1 of this MatchScoreBreakdown2018Alliance.


        :param endgame_robot1: The endgame_robot1 of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: str
        """

        self._endgame_robot1 = endgame_robot1

    @property
    def endgame_robot2(self):
        """Gets the endgame_robot2 of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The endgame_robot2 of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: str
        """
        return self._endgame_robot2

    @endgame_robot2.setter
    def endgame_robot2(self, endgame_robot2):
        """Sets the endgame_robot2 of this MatchScoreBreakdown2018Alliance.


        :param endgame_robot2: The endgame_robot2 of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: str
        """

        self._endgame_robot2 = endgame_robot2

    @property
    def endgame_robot3(self):
        """Gets the endgame_robot3 of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The endgame_robot3 of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: str
        """
        return self._endgame_robot3

    @endgame_robot3.setter
    def endgame_robot3(self, endgame_robot3):
        """Sets the endgame_robot3 of this MatchScoreBreakdown2018Alliance.


        :param endgame_robot3: The endgame_robot3 of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: str
        """

        self._endgame_robot3 = endgame_robot3

    @property
    def face_the_boss_ranking_point(self):
        """Gets the face_the_boss_ranking_point of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The face_the_boss_ranking_point of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: bool
        """
        return self._face_the_boss_ranking_point

    @face_the_boss_ranking_point.setter
    def face_the_boss_ranking_point(self, face_the_boss_ranking_point):
        """Sets the face_the_boss_ranking_point of this MatchScoreBreakdown2018Alliance.


        :param face_the_boss_ranking_point: The face_the_boss_ranking_point of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: bool
        """

        self._face_the_boss_ranking_point = face_the_boss_ranking_point

    @property
    def foul_count(self):
        """Gets the foul_count of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The foul_count of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._foul_count

    @foul_count.setter
    def foul_count(self, foul_count):
        """Sets the foul_count of this MatchScoreBreakdown2018Alliance.


        :param foul_count: The foul_count of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._foul_count = foul_count

    @property
    def foul_points(self):
        """Gets the foul_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The foul_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._foul_points

    @foul_points.setter
    def foul_points(self, foul_points):
        """Sets the foul_points of this MatchScoreBreakdown2018Alliance.


        :param foul_points: The foul_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._foul_points = foul_points

    @property
    def rp(self):
        """Gets the rp of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The rp of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._rp

    @rp.setter
    def rp(self, rp):
        """Sets the rp of this MatchScoreBreakdown2018Alliance.


        :param rp: The rp of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._rp = rp

    @property
    def tech_foul_count(self):
        """Gets the tech_foul_count of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The tech_foul_count of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._tech_foul_count

    @tech_foul_count.setter
    def tech_foul_count(self, tech_foul_count):
        """Sets the tech_foul_count of this MatchScoreBreakdown2018Alliance.


        :param tech_foul_count: The tech_foul_count of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._tech_foul_count = tech_foul_count

    @property
    def teleop_ownership_points(self):
        """Gets the teleop_ownership_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The teleop_ownership_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_ownership_points

    @teleop_ownership_points.setter
    def teleop_ownership_points(self, teleop_ownership_points):
        """Sets the teleop_ownership_points of this MatchScoreBreakdown2018Alliance.


        :param teleop_ownership_points: The teleop_ownership_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_ownership_points = teleop_ownership_points

    @property
    def teleop_points(self):
        """Gets the teleop_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The teleop_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_points

    @teleop_points.setter
    def teleop_points(self, teleop_points):
        """Sets the teleop_points of this MatchScoreBreakdown2018Alliance.


        :param teleop_points: The teleop_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_points = teleop_points

    @property
    def teleop_scale_boost_sec(self):
        """Gets the teleop_scale_boost_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The teleop_scale_boost_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_scale_boost_sec

    @teleop_scale_boost_sec.setter
    def teleop_scale_boost_sec(self, teleop_scale_boost_sec):
        """Sets the teleop_scale_boost_sec of this MatchScoreBreakdown2018Alliance.


        :param teleop_scale_boost_sec: The teleop_scale_boost_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_scale_boost_sec = teleop_scale_boost_sec

    @property
    def teleop_scale_force_sec(self):
        """Gets the teleop_scale_force_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The teleop_scale_force_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_scale_force_sec

    @teleop_scale_force_sec.setter
    def teleop_scale_force_sec(self, teleop_scale_force_sec):
        """Sets the teleop_scale_force_sec of this MatchScoreBreakdown2018Alliance.


        :param teleop_scale_force_sec: The teleop_scale_force_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_scale_force_sec = teleop_scale_force_sec

    @property
    def teleop_scale_ownership_sec(self):
        """Gets the teleop_scale_ownership_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The teleop_scale_ownership_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_scale_ownership_sec

    @teleop_scale_ownership_sec.setter
    def teleop_scale_ownership_sec(self, teleop_scale_ownership_sec):
        """Sets the teleop_scale_ownership_sec of this MatchScoreBreakdown2018Alliance.


        :param teleop_scale_ownership_sec: The teleop_scale_ownership_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_scale_ownership_sec = teleop_scale_ownership_sec

    @property
    def teleop_switch_boost_sec(self):
        """Gets the teleop_switch_boost_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The teleop_switch_boost_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_switch_boost_sec

    @teleop_switch_boost_sec.setter
    def teleop_switch_boost_sec(self, teleop_switch_boost_sec):
        """Sets the teleop_switch_boost_sec of this MatchScoreBreakdown2018Alliance.


        :param teleop_switch_boost_sec: The teleop_switch_boost_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_switch_boost_sec = teleop_switch_boost_sec

    @property
    def teleop_switch_force_sec(self):
        """Gets the teleop_switch_force_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The teleop_switch_force_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_switch_force_sec

    @teleop_switch_force_sec.setter
    def teleop_switch_force_sec(self, teleop_switch_force_sec):
        """Sets the teleop_switch_force_sec of this MatchScoreBreakdown2018Alliance.


        :param teleop_switch_force_sec: The teleop_switch_force_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_switch_force_sec = teleop_switch_force_sec

    @property
    def teleop_switch_ownership_sec(self):
        """Gets the teleop_switch_ownership_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The teleop_switch_ownership_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_switch_ownership_sec

    @teleop_switch_ownership_sec.setter
    def teleop_switch_ownership_sec(self, teleop_switch_ownership_sec):
        """Sets the teleop_switch_ownership_sec of this MatchScoreBreakdown2018Alliance.


        :param teleop_switch_ownership_sec: The teleop_switch_ownership_sec of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_switch_ownership_sec = teleop_switch_ownership_sec

    @property
    def total_points(self):
        """Gets the total_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The total_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._total_points

    @total_points.setter
    def total_points(self, total_points):
        """Sets the total_points of this MatchScoreBreakdown2018Alliance.


        :param total_points: The total_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._total_points = total_points

    @property
    def vault_boost_played(self):
        """Gets the vault_boost_played of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The vault_boost_played of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._vault_boost_played

    @vault_boost_played.setter
    def vault_boost_played(self, vault_boost_played):
        """Sets the vault_boost_played of this MatchScoreBreakdown2018Alliance.


        :param vault_boost_played: The vault_boost_played of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._vault_boost_played = vault_boost_played

    @property
    def vault_boost_total(self):
        """Gets the vault_boost_total of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The vault_boost_total of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._vault_boost_total

    @vault_boost_total.setter
    def vault_boost_total(self, vault_boost_total):
        """Sets the vault_boost_total of this MatchScoreBreakdown2018Alliance.


        :param vault_boost_total: The vault_boost_total of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._vault_boost_total = vault_boost_total

    @property
    def vault_force_played(self):
        """Gets the vault_force_played of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The vault_force_played of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._vault_force_played

    @vault_force_played.setter
    def vault_force_played(self, vault_force_played):
        """Sets the vault_force_played of this MatchScoreBreakdown2018Alliance.


        :param vault_force_played: The vault_force_played of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._vault_force_played = vault_force_played

    @property
    def vault_force_total(self):
        """Gets the vault_force_total of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The vault_force_total of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._vault_force_total

    @vault_force_total.setter
    def vault_force_total(self, vault_force_total):
        """Sets the vault_force_total of this MatchScoreBreakdown2018Alliance.


        :param vault_force_total: The vault_force_total of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._vault_force_total = vault_force_total

    @property
    def vault_levitate_played(self):
        """Gets the vault_levitate_played of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The vault_levitate_played of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._vault_levitate_played

    @vault_levitate_played.setter
    def vault_levitate_played(self, vault_levitate_played):
        """Sets the vault_levitate_played of this MatchScoreBreakdown2018Alliance.


        :param vault_levitate_played: The vault_levitate_played of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._vault_levitate_played = vault_levitate_played

    @property
    def vault_levitate_total(self):
        """Gets the vault_levitate_total of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The vault_levitate_total of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._vault_levitate_total

    @vault_levitate_total.setter
    def vault_levitate_total(self, vault_levitate_total):
        """Sets the vault_levitate_total of this MatchScoreBreakdown2018Alliance.


        :param vault_levitate_total: The vault_levitate_total of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._vault_levitate_total = vault_levitate_total

    @property
    def vault_points(self):
        """Gets the vault_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501


        :return: The vault_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: int
        """
        return self._vault_points

    @vault_points.setter
    def vault_points(self, vault_points):
        """Sets the vault_points of this MatchScoreBreakdown2018Alliance.


        :param vault_points: The vault_points of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: int
        """

        self._vault_points = vault_points

    @property
    def tba_game_data(self):
        """Gets the tba_game_data of this MatchScoreBreakdown2018Alliance.  # noqa: E501

        Unofficial TBA-computed value of the FMS provided GameData given to the alliance teams at the start of the match. 3 Character String containing `L` and `R` only. The first character represents the near switch, the 2nd the scale, and the 3rd the far, opposing, switch from the alliance's perspective. An `L` in a position indicates the platform on the left will be lit for the alliance while an `R` will indicate the right platform will be lit for the alliance. See also [WPI Screen Steps](https://wpilib.screenstepslive.com/s/currentCS/m/getting_started/l/826278-2018-game-data-details).  # noqa: E501

        :return: The tba_game_data of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :rtype: str
        """
        return self._tba_game_data

    @tba_game_data.setter
    def tba_game_data(self, tba_game_data):
        """Sets the tba_game_data of this MatchScoreBreakdown2018Alliance.

        Unofficial TBA-computed value of the FMS provided GameData given to the alliance teams at the start of the match. 3 Character String containing `L` and `R` only. The first character represents the near switch, the 2nd the scale, and the 3rd the far, opposing, switch from the alliance's perspective. An `L` in a position indicates the platform on the left will be lit for the alliance while an `R` will indicate the right platform will be lit for the alliance. See also [WPI Screen Steps](https://wpilib.screenstepslive.com/s/currentCS/m/getting_started/l/826278-2018-game-data-details).  # noqa: E501

        :param tba_game_data: The tba_game_data of this MatchScoreBreakdown2018Alliance.  # noqa: E501
        :type: str
        """

        self._tba_game_data = tba_game_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MatchScoreBreakdown2018Alliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
