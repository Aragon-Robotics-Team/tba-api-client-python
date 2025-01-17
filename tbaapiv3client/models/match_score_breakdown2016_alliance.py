# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    The version of the OpenAPI document: 3.5.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tbaapiv3client.configuration import Configuration


class MatchScoreBreakdown2016Alliance(object):
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
        'auto_points': 'int',
        'teleop_points': 'int',
        'breach_points': 'int',
        'foul_points': 'int',
        'capture_points': 'int',
        'adjust_points': 'int',
        'total_points': 'int',
        'robot1_auto': 'str',
        'robot2_auto': 'str',
        'robot3_auto': 'str',
        'auto_reach_points': 'int',
        'auto_crossing_points': 'int',
        'auto_boulders_low': 'int',
        'auto_boulders_high': 'int',
        'auto_boulder_points': 'int',
        'teleop_crossing_points': 'int',
        'teleop_boulders_low': 'int',
        'teleop_boulders_high': 'int',
        'teleop_boulder_points': 'int',
        'teleop_defenses_breached': 'bool',
        'teleop_challenge_points': 'int',
        'teleop_scale_points': 'int',
        'teleop_tower_captured': 'int',
        'tower_face_a': 'str',
        'tower_face_b': 'str',
        'tower_face_c': 'str',
        'tower_end_strength': 'int',
        'tech_foul_count': 'int',
        'foul_count': 'int',
        'position2': 'str',
        'position3': 'str',
        'position4': 'str',
        'position5': 'str',
        'position1crossings': 'int',
        'position2crossings': 'int',
        'position3crossings': 'int',
        'position4crossings': 'int',
        'position5crossings': 'int'
    }

    attribute_map = {
        'auto_points': 'autoPoints',
        'teleop_points': 'teleopPoints',
        'breach_points': 'breachPoints',
        'foul_points': 'foulPoints',
        'capture_points': 'capturePoints',
        'adjust_points': 'adjustPoints',
        'total_points': 'totalPoints',
        'robot1_auto': 'robot1Auto',
        'robot2_auto': 'robot2Auto',
        'robot3_auto': 'robot3Auto',
        'auto_reach_points': 'autoReachPoints',
        'auto_crossing_points': 'autoCrossingPoints',
        'auto_boulders_low': 'autoBouldersLow',
        'auto_boulders_high': 'autoBouldersHigh',
        'auto_boulder_points': 'autoBoulderPoints',
        'teleop_crossing_points': 'teleopCrossingPoints',
        'teleop_boulders_low': 'teleopBouldersLow',
        'teleop_boulders_high': 'teleopBouldersHigh',
        'teleop_boulder_points': 'teleopBoulderPoints',
        'teleop_defenses_breached': 'teleopDefensesBreached',
        'teleop_challenge_points': 'teleopChallengePoints',
        'teleop_scale_points': 'teleopScalePoints',
        'teleop_tower_captured': 'teleopTowerCaptured',
        'tower_face_a': 'towerFaceA',
        'tower_face_b': 'towerFaceB',
        'tower_face_c': 'towerFaceC',
        'tower_end_strength': 'towerEndStrength',
        'tech_foul_count': 'techFoulCount',
        'foul_count': 'foulCount',
        'position2': 'position2',
        'position3': 'position3',
        'position4': 'position4',
        'position5': 'position5',
        'position1crossings': 'position1crossings',
        'position2crossings': 'position2crossings',
        'position3crossings': 'position3crossings',
        'position4crossings': 'position4crossings',
        'position5crossings': 'position5crossings'
    }

    def __init__(self, auto_points=None, teleop_points=None, breach_points=None, foul_points=None, capture_points=None, adjust_points=None, total_points=None, robot1_auto=None, robot2_auto=None, robot3_auto=None, auto_reach_points=None, auto_crossing_points=None, auto_boulders_low=None, auto_boulders_high=None, auto_boulder_points=None, teleop_crossing_points=None, teleop_boulders_low=None, teleop_boulders_high=None, teleop_boulder_points=None, teleop_defenses_breached=None, teleop_challenge_points=None, teleop_scale_points=None, teleop_tower_captured=None, tower_face_a=None, tower_face_b=None, tower_face_c=None, tower_end_strength=None, tech_foul_count=None, foul_count=None, position2=None, position3=None, position4=None, position5=None, position1crossings=None, position2crossings=None, position3crossings=None, position4crossings=None, position5crossings=None, local_vars_configuration=None):  # noqa: E501
        """MatchScoreBreakdown2016Alliance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auto_points = None
        self._teleop_points = None
        self._breach_points = None
        self._foul_points = None
        self._capture_points = None
        self._adjust_points = None
        self._total_points = None
        self._robot1_auto = None
        self._robot2_auto = None
        self._robot3_auto = None
        self._auto_reach_points = None
        self._auto_crossing_points = None
        self._auto_boulders_low = None
        self._auto_boulders_high = None
        self._auto_boulder_points = None
        self._teleop_crossing_points = None
        self._teleop_boulders_low = None
        self._teleop_boulders_high = None
        self._teleop_boulder_points = None
        self._teleop_defenses_breached = None
        self._teleop_challenge_points = None
        self._teleop_scale_points = None
        self._teleop_tower_captured = None
        self._tower_face_a = None
        self._tower_face_b = None
        self._tower_face_c = None
        self._tower_end_strength = None
        self._tech_foul_count = None
        self._foul_count = None
        self._position2 = None
        self._position3 = None
        self._position4 = None
        self._position5 = None
        self._position1crossings = None
        self._position2crossings = None
        self._position3crossings = None
        self._position4crossings = None
        self._position5crossings = None
        self.discriminator = None

        if auto_points is not None:
            self.auto_points = auto_points
        if teleop_points is not None:
            self.teleop_points = teleop_points
        if breach_points is not None:
            self.breach_points = breach_points
        if foul_points is not None:
            self.foul_points = foul_points
        if capture_points is not None:
            self.capture_points = capture_points
        if adjust_points is not None:
            self.adjust_points = adjust_points
        if total_points is not None:
            self.total_points = total_points
        if robot1_auto is not None:
            self.robot1_auto = robot1_auto
        if robot2_auto is not None:
            self.robot2_auto = robot2_auto
        if robot3_auto is not None:
            self.robot3_auto = robot3_auto
        if auto_reach_points is not None:
            self.auto_reach_points = auto_reach_points
        if auto_crossing_points is not None:
            self.auto_crossing_points = auto_crossing_points
        if auto_boulders_low is not None:
            self.auto_boulders_low = auto_boulders_low
        if auto_boulders_high is not None:
            self.auto_boulders_high = auto_boulders_high
        if auto_boulder_points is not None:
            self.auto_boulder_points = auto_boulder_points
        if teleop_crossing_points is not None:
            self.teleop_crossing_points = teleop_crossing_points
        if teleop_boulders_low is not None:
            self.teleop_boulders_low = teleop_boulders_low
        if teleop_boulders_high is not None:
            self.teleop_boulders_high = teleop_boulders_high
        if teleop_boulder_points is not None:
            self.teleop_boulder_points = teleop_boulder_points
        if teleop_defenses_breached is not None:
            self.teleop_defenses_breached = teleop_defenses_breached
        if teleop_challenge_points is not None:
            self.teleop_challenge_points = teleop_challenge_points
        if teleop_scale_points is not None:
            self.teleop_scale_points = teleop_scale_points
        if teleop_tower_captured is not None:
            self.teleop_tower_captured = teleop_tower_captured
        if tower_face_a is not None:
            self.tower_face_a = tower_face_a
        if tower_face_b is not None:
            self.tower_face_b = tower_face_b
        if tower_face_c is not None:
            self.tower_face_c = tower_face_c
        if tower_end_strength is not None:
            self.tower_end_strength = tower_end_strength
        if tech_foul_count is not None:
            self.tech_foul_count = tech_foul_count
        if foul_count is not None:
            self.foul_count = foul_count
        if position2 is not None:
            self.position2 = position2
        if position3 is not None:
            self.position3 = position3
        if position4 is not None:
            self.position4 = position4
        if position5 is not None:
            self.position5 = position5
        if position1crossings is not None:
            self.position1crossings = position1crossings
        if position2crossings is not None:
            self.position2crossings = position2crossings
        if position3crossings is not None:
            self.position3crossings = position3crossings
        if position4crossings is not None:
            self.position4crossings = position4crossings
        if position5crossings is not None:
            self.position5crossings = position5crossings

    @property
    def auto_points(self):
        """Gets the auto_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The auto_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._auto_points

    @auto_points.setter
    def auto_points(self, auto_points):
        """Sets the auto_points of this MatchScoreBreakdown2016Alliance.


        :param auto_points: The auto_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._auto_points = auto_points

    @property
    def teleop_points(self):
        """Gets the teleop_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The teleop_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_points

    @teleop_points.setter
    def teleop_points(self, teleop_points):
        """Sets the teleop_points of this MatchScoreBreakdown2016Alliance.


        :param teleop_points: The teleop_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_points = teleop_points

    @property
    def breach_points(self):
        """Gets the breach_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The breach_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._breach_points

    @breach_points.setter
    def breach_points(self, breach_points):
        """Sets the breach_points of this MatchScoreBreakdown2016Alliance.


        :param breach_points: The breach_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._breach_points = breach_points

    @property
    def foul_points(self):
        """Gets the foul_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The foul_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._foul_points

    @foul_points.setter
    def foul_points(self, foul_points):
        """Sets the foul_points of this MatchScoreBreakdown2016Alliance.


        :param foul_points: The foul_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._foul_points = foul_points

    @property
    def capture_points(self):
        """Gets the capture_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The capture_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._capture_points

    @capture_points.setter
    def capture_points(self, capture_points):
        """Sets the capture_points of this MatchScoreBreakdown2016Alliance.


        :param capture_points: The capture_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._capture_points = capture_points

    @property
    def adjust_points(self):
        """Gets the adjust_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The adjust_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._adjust_points

    @adjust_points.setter
    def adjust_points(self, adjust_points):
        """Sets the adjust_points of this MatchScoreBreakdown2016Alliance.


        :param adjust_points: The adjust_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._adjust_points = adjust_points

    @property
    def total_points(self):
        """Gets the total_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The total_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._total_points

    @total_points.setter
    def total_points(self, total_points):
        """Sets the total_points of this MatchScoreBreakdown2016Alliance.


        :param total_points: The total_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._total_points = total_points

    @property
    def robot1_auto(self):
        """Gets the robot1_auto of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The robot1_auto of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: str
        """
        return self._robot1_auto

    @robot1_auto.setter
    def robot1_auto(self, robot1_auto):
        """Sets the robot1_auto of this MatchScoreBreakdown2016Alliance.


        :param robot1_auto: The robot1_auto of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: str
        """
        allowed_values = ["Crossed", "Reached", "None"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and robot1_auto not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `robot1_auto` ({0}), must be one of {1}"  # noqa: E501
                .format(robot1_auto, allowed_values)
            )

        self._robot1_auto = robot1_auto

    @property
    def robot2_auto(self):
        """Gets the robot2_auto of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The robot2_auto of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: str
        """
        return self._robot2_auto

    @robot2_auto.setter
    def robot2_auto(self, robot2_auto):
        """Sets the robot2_auto of this MatchScoreBreakdown2016Alliance.


        :param robot2_auto: The robot2_auto of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: str
        """
        allowed_values = ["Crossed", "Reached", "None"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and robot2_auto not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `robot2_auto` ({0}), must be one of {1}"  # noqa: E501
                .format(robot2_auto, allowed_values)
            )

        self._robot2_auto = robot2_auto

    @property
    def robot3_auto(self):
        """Gets the robot3_auto of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The robot3_auto of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: str
        """
        return self._robot3_auto

    @robot3_auto.setter
    def robot3_auto(self, robot3_auto):
        """Sets the robot3_auto of this MatchScoreBreakdown2016Alliance.


        :param robot3_auto: The robot3_auto of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: str
        """
        allowed_values = ["Crossed", "Reached", "None"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and robot3_auto not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `robot3_auto` ({0}), must be one of {1}"  # noqa: E501
                .format(robot3_auto, allowed_values)
            )

        self._robot3_auto = robot3_auto

    @property
    def auto_reach_points(self):
        """Gets the auto_reach_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The auto_reach_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._auto_reach_points

    @auto_reach_points.setter
    def auto_reach_points(self, auto_reach_points):
        """Sets the auto_reach_points of this MatchScoreBreakdown2016Alliance.


        :param auto_reach_points: The auto_reach_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._auto_reach_points = auto_reach_points

    @property
    def auto_crossing_points(self):
        """Gets the auto_crossing_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The auto_crossing_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._auto_crossing_points

    @auto_crossing_points.setter
    def auto_crossing_points(self, auto_crossing_points):
        """Sets the auto_crossing_points of this MatchScoreBreakdown2016Alliance.


        :param auto_crossing_points: The auto_crossing_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._auto_crossing_points = auto_crossing_points

    @property
    def auto_boulders_low(self):
        """Gets the auto_boulders_low of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The auto_boulders_low of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._auto_boulders_low

    @auto_boulders_low.setter
    def auto_boulders_low(self, auto_boulders_low):
        """Sets the auto_boulders_low of this MatchScoreBreakdown2016Alliance.


        :param auto_boulders_low: The auto_boulders_low of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._auto_boulders_low = auto_boulders_low

    @property
    def auto_boulders_high(self):
        """Gets the auto_boulders_high of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The auto_boulders_high of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._auto_boulders_high

    @auto_boulders_high.setter
    def auto_boulders_high(self, auto_boulders_high):
        """Sets the auto_boulders_high of this MatchScoreBreakdown2016Alliance.


        :param auto_boulders_high: The auto_boulders_high of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._auto_boulders_high = auto_boulders_high

    @property
    def auto_boulder_points(self):
        """Gets the auto_boulder_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The auto_boulder_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._auto_boulder_points

    @auto_boulder_points.setter
    def auto_boulder_points(self, auto_boulder_points):
        """Sets the auto_boulder_points of this MatchScoreBreakdown2016Alliance.


        :param auto_boulder_points: The auto_boulder_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._auto_boulder_points = auto_boulder_points

    @property
    def teleop_crossing_points(self):
        """Gets the teleop_crossing_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The teleop_crossing_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_crossing_points

    @teleop_crossing_points.setter
    def teleop_crossing_points(self, teleop_crossing_points):
        """Sets the teleop_crossing_points of this MatchScoreBreakdown2016Alliance.


        :param teleop_crossing_points: The teleop_crossing_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_crossing_points = teleop_crossing_points

    @property
    def teleop_boulders_low(self):
        """Gets the teleop_boulders_low of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The teleop_boulders_low of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_boulders_low

    @teleop_boulders_low.setter
    def teleop_boulders_low(self, teleop_boulders_low):
        """Sets the teleop_boulders_low of this MatchScoreBreakdown2016Alliance.


        :param teleop_boulders_low: The teleop_boulders_low of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_boulders_low = teleop_boulders_low

    @property
    def teleop_boulders_high(self):
        """Gets the teleop_boulders_high of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The teleop_boulders_high of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_boulders_high

    @teleop_boulders_high.setter
    def teleop_boulders_high(self, teleop_boulders_high):
        """Sets the teleop_boulders_high of this MatchScoreBreakdown2016Alliance.


        :param teleop_boulders_high: The teleop_boulders_high of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_boulders_high = teleop_boulders_high

    @property
    def teleop_boulder_points(self):
        """Gets the teleop_boulder_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The teleop_boulder_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_boulder_points

    @teleop_boulder_points.setter
    def teleop_boulder_points(self, teleop_boulder_points):
        """Sets the teleop_boulder_points of this MatchScoreBreakdown2016Alliance.


        :param teleop_boulder_points: The teleop_boulder_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_boulder_points = teleop_boulder_points

    @property
    def teleop_defenses_breached(self):
        """Gets the teleop_defenses_breached of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The teleop_defenses_breached of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: bool
        """
        return self._teleop_defenses_breached

    @teleop_defenses_breached.setter
    def teleop_defenses_breached(self, teleop_defenses_breached):
        """Sets the teleop_defenses_breached of this MatchScoreBreakdown2016Alliance.


        :param teleop_defenses_breached: The teleop_defenses_breached of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: bool
        """

        self._teleop_defenses_breached = teleop_defenses_breached

    @property
    def teleop_challenge_points(self):
        """Gets the teleop_challenge_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The teleop_challenge_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_challenge_points

    @teleop_challenge_points.setter
    def teleop_challenge_points(self, teleop_challenge_points):
        """Sets the teleop_challenge_points of this MatchScoreBreakdown2016Alliance.


        :param teleop_challenge_points: The teleop_challenge_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_challenge_points = teleop_challenge_points

    @property
    def teleop_scale_points(self):
        """Gets the teleop_scale_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The teleop_scale_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_scale_points

    @teleop_scale_points.setter
    def teleop_scale_points(self, teleop_scale_points):
        """Sets the teleop_scale_points of this MatchScoreBreakdown2016Alliance.


        :param teleop_scale_points: The teleop_scale_points of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_scale_points = teleop_scale_points

    @property
    def teleop_tower_captured(self):
        """Gets the teleop_tower_captured of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The teleop_tower_captured of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._teleop_tower_captured

    @teleop_tower_captured.setter
    def teleop_tower_captured(self, teleop_tower_captured):
        """Sets the teleop_tower_captured of this MatchScoreBreakdown2016Alliance.


        :param teleop_tower_captured: The teleop_tower_captured of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._teleop_tower_captured = teleop_tower_captured

    @property
    def tower_face_a(self):
        """Gets the tower_face_a of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The tower_face_a of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: str
        """
        return self._tower_face_a

    @tower_face_a.setter
    def tower_face_a(self, tower_face_a):
        """Sets the tower_face_a of this MatchScoreBreakdown2016Alliance.


        :param tower_face_a: The tower_face_a of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: str
        """

        self._tower_face_a = tower_face_a

    @property
    def tower_face_b(self):
        """Gets the tower_face_b of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The tower_face_b of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: str
        """
        return self._tower_face_b

    @tower_face_b.setter
    def tower_face_b(self, tower_face_b):
        """Sets the tower_face_b of this MatchScoreBreakdown2016Alliance.


        :param tower_face_b: The tower_face_b of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: str
        """

        self._tower_face_b = tower_face_b

    @property
    def tower_face_c(self):
        """Gets the tower_face_c of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The tower_face_c of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: str
        """
        return self._tower_face_c

    @tower_face_c.setter
    def tower_face_c(self, tower_face_c):
        """Sets the tower_face_c of this MatchScoreBreakdown2016Alliance.


        :param tower_face_c: The tower_face_c of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: str
        """

        self._tower_face_c = tower_face_c

    @property
    def tower_end_strength(self):
        """Gets the tower_end_strength of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The tower_end_strength of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._tower_end_strength

    @tower_end_strength.setter
    def tower_end_strength(self, tower_end_strength):
        """Sets the tower_end_strength of this MatchScoreBreakdown2016Alliance.


        :param tower_end_strength: The tower_end_strength of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._tower_end_strength = tower_end_strength

    @property
    def tech_foul_count(self):
        """Gets the tech_foul_count of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The tech_foul_count of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._tech_foul_count

    @tech_foul_count.setter
    def tech_foul_count(self, tech_foul_count):
        """Sets the tech_foul_count of this MatchScoreBreakdown2016Alliance.


        :param tech_foul_count: The tech_foul_count of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._tech_foul_count = tech_foul_count

    @property
    def foul_count(self):
        """Gets the foul_count of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The foul_count of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._foul_count

    @foul_count.setter
    def foul_count(self, foul_count):
        """Sets the foul_count of this MatchScoreBreakdown2016Alliance.


        :param foul_count: The foul_count of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._foul_count = foul_count

    @property
    def position2(self):
        """Gets the position2 of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The position2 of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: str
        """
        return self._position2

    @position2.setter
    def position2(self, position2):
        """Sets the position2 of this MatchScoreBreakdown2016Alliance.


        :param position2: The position2 of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: str
        """

        self._position2 = position2

    @property
    def position3(self):
        """Gets the position3 of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The position3 of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: str
        """
        return self._position3

    @position3.setter
    def position3(self, position3):
        """Sets the position3 of this MatchScoreBreakdown2016Alliance.


        :param position3: The position3 of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: str
        """

        self._position3 = position3

    @property
    def position4(self):
        """Gets the position4 of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The position4 of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: str
        """
        return self._position4

    @position4.setter
    def position4(self, position4):
        """Sets the position4 of this MatchScoreBreakdown2016Alliance.


        :param position4: The position4 of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: str
        """

        self._position4 = position4

    @property
    def position5(self):
        """Gets the position5 of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The position5 of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: str
        """
        return self._position5

    @position5.setter
    def position5(self, position5):
        """Sets the position5 of this MatchScoreBreakdown2016Alliance.


        :param position5: The position5 of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: str
        """

        self._position5 = position5

    @property
    def position1crossings(self):
        """Gets the position1crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The position1crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._position1crossings

    @position1crossings.setter
    def position1crossings(self, position1crossings):
        """Sets the position1crossings of this MatchScoreBreakdown2016Alliance.


        :param position1crossings: The position1crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._position1crossings = position1crossings

    @property
    def position2crossings(self):
        """Gets the position2crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The position2crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._position2crossings

    @position2crossings.setter
    def position2crossings(self, position2crossings):
        """Sets the position2crossings of this MatchScoreBreakdown2016Alliance.


        :param position2crossings: The position2crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._position2crossings = position2crossings

    @property
    def position3crossings(self):
        """Gets the position3crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The position3crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._position3crossings

    @position3crossings.setter
    def position3crossings(self, position3crossings):
        """Sets the position3crossings of this MatchScoreBreakdown2016Alliance.


        :param position3crossings: The position3crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._position3crossings = position3crossings

    @property
    def position4crossings(self):
        """Gets the position4crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The position4crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._position4crossings

    @position4crossings.setter
    def position4crossings(self, position4crossings):
        """Sets the position4crossings of this MatchScoreBreakdown2016Alliance.


        :param position4crossings: The position4crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._position4crossings = position4crossings

    @property
    def position5crossings(self):
        """Gets the position5crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501


        :return: The position5crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :rtype: int
        """
        return self._position5crossings

    @position5crossings.setter
    def position5crossings(self, position5crossings):
        """Sets the position5crossings of this MatchScoreBreakdown2016Alliance.


        :param position5crossings: The position5crossings of this MatchScoreBreakdown2016Alliance.  # noqa: E501
        :type: int
        """

        self._position5crossings = position5crossings

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
        if not isinstance(other, MatchScoreBreakdown2016Alliance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchScoreBreakdown2016Alliance):
            return True

        return self.to_dict() != other.to_dict()
