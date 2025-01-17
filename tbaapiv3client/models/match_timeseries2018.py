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


class MatchTimeseries2018(object):
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
        'event_key': 'str',
        'match_id': 'str',
        'mode': 'str',
        'play': 'int',
        'time_remaining': 'int',
        'blue_auto_quest': 'int',
        'blue_boost_count': 'int',
        'blue_boost_played': 'int',
        'blue_current_powerup': 'str',
        'blue_face_the_boss': 'int',
        'blue_force_count': 'int',
        'blue_force_played': 'int',
        'blue_levitate_count': 'int',
        'blue_levitate_played': 'int',
        'blue_powerup_time_remaining': 'str',
        'blue_scale_owned': 'int',
        'blue_score': 'int',
        'blue_switch_owned': 'int',
        'red_auto_quest': 'int',
        'red_boost_count': 'int',
        'red_boost_played': 'int',
        'red_current_powerup': 'str',
        'red_face_the_boss': 'int',
        'red_force_count': 'int',
        'red_force_played': 'int',
        'red_levitate_count': 'int',
        'red_levitate_played': 'int',
        'red_powerup_time_remaining': 'str',
        'red_scale_owned': 'int',
        'red_score': 'int',
        'red_switch_owned': 'int'
    }

    attribute_map = {
        'event_key': 'event_key',
        'match_id': 'match_id',
        'mode': 'mode',
        'play': 'play',
        'time_remaining': 'time_remaining',
        'blue_auto_quest': 'blue_auto_quest',
        'blue_boost_count': 'blue_boost_count',
        'blue_boost_played': 'blue_boost_played',
        'blue_current_powerup': 'blue_current_powerup',
        'blue_face_the_boss': 'blue_face_the_boss',
        'blue_force_count': 'blue_force_count',
        'blue_force_played': 'blue_force_played',
        'blue_levitate_count': 'blue_levitate_count',
        'blue_levitate_played': 'blue_levitate_played',
        'blue_powerup_time_remaining': 'blue_powerup_time_remaining',
        'blue_scale_owned': 'blue_scale_owned',
        'blue_score': 'blue_score',
        'blue_switch_owned': 'blue_switch_owned',
        'red_auto_quest': 'red_auto_quest',
        'red_boost_count': 'red_boost_count',
        'red_boost_played': 'red_boost_played',
        'red_current_powerup': 'red_current_powerup',
        'red_face_the_boss': 'red_face_the_boss',
        'red_force_count': 'red_force_count',
        'red_force_played': 'red_force_played',
        'red_levitate_count': 'red_levitate_count',
        'red_levitate_played': 'red_levitate_played',
        'red_powerup_time_remaining': 'red_powerup_time_remaining',
        'red_scale_owned': 'red_scale_owned',
        'red_score': 'red_score',
        'red_switch_owned': 'red_switch_owned'
    }

    def __init__(self, event_key=None, match_id=None, mode=None, play=None, time_remaining=None, blue_auto_quest=None, blue_boost_count=None, blue_boost_played=None, blue_current_powerup=None, blue_face_the_boss=None, blue_force_count=None, blue_force_played=None, blue_levitate_count=None, blue_levitate_played=None, blue_powerup_time_remaining=None, blue_scale_owned=None, blue_score=None, blue_switch_owned=None, red_auto_quest=None, red_boost_count=None, red_boost_played=None, red_current_powerup=None, red_face_the_boss=None, red_force_count=None, red_force_played=None, red_levitate_count=None, red_levitate_played=None, red_powerup_time_remaining=None, red_scale_owned=None, red_score=None, red_switch_owned=None, local_vars_configuration=None):  # noqa: E501
        """MatchTimeseries2018 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event_key = None
        self._match_id = None
        self._mode = None
        self._play = None
        self._time_remaining = None
        self._blue_auto_quest = None
        self._blue_boost_count = None
        self._blue_boost_played = None
        self._blue_current_powerup = None
        self._blue_face_the_boss = None
        self._blue_force_count = None
        self._blue_force_played = None
        self._blue_levitate_count = None
        self._blue_levitate_played = None
        self._blue_powerup_time_remaining = None
        self._blue_scale_owned = None
        self._blue_score = None
        self._blue_switch_owned = None
        self._red_auto_quest = None
        self._red_boost_count = None
        self._red_boost_played = None
        self._red_current_powerup = None
        self._red_face_the_boss = None
        self._red_force_count = None
        self._red_force_played = None
        self._red_levitate_count = None
        self._red_levitate_played = None
        self._red_powerup_time_remaining = None
        self._red_scale_owned = None
        self._red_score = None
        self._red_switch_owned = None
        self.discriminator = None

        if event_key is not None:
            self.event_key = event_key
        if match_id is not None:
            self.match_id = match_id
        if mode is not None:
            self.mode = mode
        if play is not None:
            self.play = play
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if blue_auto_quest is not None:
            self.blue_auto_quest = blue_auto_quest
        if blue_boost_count is not None:
            self.blue_boost_count = blue_boost_count
        if blue_boost_played is not None:
            self.blue_boost_played = blue_boost_played
        if blue_current_powerup is not None:
            self.blue_current_powerup = blue_current_powerup
        if blue_face_the_boss is not None:
            self.blue_face_the_boss = blue_face_the_boss
        if blue_force_count is not None:
            self.blue_force_count = blue_force_count
        if blue_force_played is not None:
            self.blue_force_played = blue_force_played
        if blue_levitate_count is not None:
            self.blue_levitate_count = blue_levitate_count
        if blue_levitate_played is not None:
            self.blue_levitate_played = blue_levitate_played
        if blue_powerup_time_remaining is not None:
            self.blue_powerup_time_remaining = blue_powerup_time_remaining
        if blue_scale_owned is not None:
            self.blue_scale_owned = blue_scale_owned
        if blue_score is not None:
            self.blue_score = blue_score
        if blue_switch_owned is not None:
            self.blue_switch_owned = blue_switch_owned
        if red_auto_quest is not None:
            self.red_auto_quest = red_auto_quest
        if red_boost_count is not None:
            self.red_boost_count = red_boost_count
        if red_boost_played is not None:
            self.red_boost_played = red_boost_played
        if red_current_powerup is not None:
            self.red_current_powerup = red_current_powerup
        if red_face_the_boss is not None:
            self.red_face_the_boss = red_face_the_boss
        if red_force_count is not None:
            self.red_force_count = red_force_count
        if red_force_played is not None:
            self.red_force_played = red_force_played
        if red_levitate_count is not None:
            self.red_levitate_count = red_levitate_count
        if red_levitate_played is not None:
            self.red_levitate_played = red_levitate_played
        if red_powerup_time_remaining is not None:
            self.red_powerup_time_remaining = red_powerup_time_remaining
        if red_scale_owned is not None:
            self.red_scale_owned = red_scale_owned
        if red_score is not None:
            self.red_score = red_score
        if red_switch_owned is not None:
            self.red_switch_owned = red_switch_owned

    @property
    def event_key(self):
        """Gets the event_key of this MatchTimeseries2018.  # noqa: E501

        TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event.  # noqa: E501

        :return: The event_key of this MatchTimeseries2018.  # noqa: E501
        :rtype: str
        """
        return self._event_key

    @event_key.setter
    def event_key(self, event_key):
        """Sets the event_key of this MatchTimeseries2018.

        TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event.  # noqa: E501

        :param event_key: The event_key of this MatchTimeseries2018.  # noqa: E501
        :type: str
        """

        self._event_key = event_key

    @property
    def match_id(self):
        """Gets the match_id of this MatchTimeseries2018.  # noqa: E501

        Match ID consisting of the level, match number, and set number, eg `qm45` or `f1m1`.  # noqa: E501

        :return: The match_id of this MatchTimeseries2018.  # noqa: E501
        :rtype: str
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """Sets the match_id of this MatchTimeseries2018.

        Match ID consisting of the level, match number, and set number, eg `qm45` or `f1m1`.  # noqa: E501

        :param match_id: The match_id of this MatchTimeseries2018.  # noqa: E501
        :type: str
        """

        self._match_id = match_id

    @property
    def mode(self):
        """Gets the mode of this MatchTimeseries2018.  # noqa: E501

        Current mode of play, can be `pre_match`, `auto`, `telop`, or `post_match`.  # noqa: E501

        :return: The mode of this MatchTimeseries2018.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this MatchTimeseries2018.

        Current mode of play, can be `pre_match`, `auto`, `telop`, or `post_match`.  # noqa: E501

        :param mode: The mode of this MatchTimeseries2018.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def play(self):
        """Gets the play of this MatchTimeseries2018.  # noqa: E501


        :return: The play of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._play

    @play.setter
    def play(self, play):
        """Sets the play of this MatchTimeseries2018.


        :param play: The play of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._play = play

    @property
    def time_remaining(self):
        """Gets the time_remaining of this MatchTimeseries2018.  # noqa: E501

        Amount of time remaining in the match, only valid during `auto` and `teleop` modes.  # noqa: E501

        :return: The time_remaining of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, time_remaining):
        """Sets the time_remaining of this MatchTimeseries2018.

        Amount of time remaining in the match, only valid during `auto` and `teleop` modes.  # noqa: E501

        :param time_remaining: The time_remaining of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._time_remaining = time_remaining

    @property
    def blue_auto_quest(self):
        """Gets the blue_auto_quest of this MatchTimeseries2018.  # noqa: E501

        1 if the blue alliance is credited with the AUTO QUEST, 0 if not.  # noqa: E501

        :return: The blue_auto_quest of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._blue_auto_quest

    @blue_auto_quest.setter
    def blue_auto_quest(self, blue_auto_quest):
        """Sets the blue_auto_quest of this MatchTimeseries2018.

        1 if the blue alliance is credited with the AUTO QUEST, 0 if not.  # noqa: E501

        :param blue_auto_quest: The blue_auto_quest of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._blue_auto_quest = blue_auto_quest

    @property
    def blue_boost_count(self):
        """Gets the blue_boost_count of this MatchTimeseries2018.  # noqa: E501

        Number of POWER CUBES in the BOOST section of the blue alliance VAULT.  # noqa: E501

        :return: The blue_boost_count of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._blue_boost_count

    @blue_boost_count.setter
    def blue_boost_count(self, blue_boost_count):
        """Sets the blue_boost_count of this MatchTimeseries2018.

        Number of POWER CUBES in the BOOST section of the blue alliance VAULT.  # noqa: E501

        :param blue_boost_count: The blue_boost_count of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._blue_boost_count = blue_boost_count

    @property
    def blue_boost_played(self):
        """Gets the blue_boost_played of this MatchTimeseries2018.  # noqa: E501

        Returns 1 if the blue alliance BOOST was played, or 0 if not played.  # noqa: E501

        :return: The blue_boost_played of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._blue_boost_played

    @blue_boost_played.setter
    def blue_boost_played(self, blue_boost_played):
        """Sets the blue_boost_played of this MatchTimeseries2018.

        Returns 1 if the blue alliance BOOST was played, or 0 if not played.  # noqa: E501

        :param blue_boost_played: The blue_boost_played of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._blue_boost_played = blue_boost_played

    @property
    def blue_current_powerup(self):
        """Gets the blue_current_powerup of this MatchTimeseries2018.  # noqa: E501

        Name of the current blue alliance POWER UP being played, or `null`.  # noqa: E501

        :return: The blue_current_powerup of this MatchTimeseries2018.  # noqa: E501
        :rtype: str
        """
        return self._blue_current_powerup

    @blue_current_powerup.setter
    def blue_current_powerup(self, blue_current_powerup):
        """Sets the blue_current_powerup of this MatchTimeseries2018.

        Name of the current blue alliance POWER UP being played, or `null`.  # noqa: E501

        :param blue_current_powerup: The blue_current_powerup of this MatchTimeseries2018.  # noqa: E501
        :type: str
        """

        self._blue_current_powerup = blue_current_powerup

    @property
    def blue_face_the_boss(self):
        """Gets the blue_face_the_boss of this MatchTimeseries2018.  # noqa: E501

        1 if the blue alliance is credited with FACING THE BOSS, 0 if not.  # noqa: E501

        :return: The blue_face_the_boss of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._blue_face_the_boss

    @blue_face_the_boss.setter
    def blue_face_the_boss(self, blue_face_the_boss):
        """Sets the blue_face_the_boss of this MatchTimeseries2018.

        1 if the blue alliance is credited with FACING THE BOSS, 0 if not.  # noqa: E501

        :param blue_face_the_boss: The blue_face_the_boss of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._blue_face_the_boss = blue_face_the_boss

    @property
    def blue_force_count(self):
        """Gets the blue_force_count of this MatchTimeseries2018.  # noqa: E501

        Number of POWER CUBES in the FORCE section of the blue alliance VAULT.  # noqa: E501

        :return: The blue_force_count of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._blue_force_count

    @blue_force_count.setter
    def blue_force_count(self, blue_force_count):
        """Sets the blue_force_count of this MatchTimeseries2018.

        Number of POWER CUBES in the FORCE section of the blue alliance VAULT.  # noqa: E501

        :param blue_force_count: The blue_force_count of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._blue_force_count = blue_force_count

    @property
    def blue_force_played(self):
        """Gets the blue_force_played of this MatchTimeseries2018.  # noqa: E501

        Returns 1 if the blue alliance FORCE was played, or 0 if not played.  # noqa: E501

        :return: The blue_force_played of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._blue_force_played

    @blue_force_played.setter
    def blue_force_played(self, blue_force_played):
        """Sets the blue_force_played of this MatchTimeseries2018.

        Returns 1 if the blue alliance FORCE was played, or 0 if not played.  # noqa: E501

        :param blue_force_played: The blue_force_played of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._blue_force_played = blue_force_played

    @property
    def blue_levitate_count(self):
        """Gets the blue_levitate_count of this MatchTimeseries2018.  # noqa: E501

        Number of POWER CUBES in the LEVITATE section of the blue alliance VAULT.  # noqa: E501

        :return: The blue_levitate_count of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._blue_levitate_count

    @blue_levitate_count.setter
    def blue_levitate_count(self, blue_levitate_count):
        """Sets the blue_levitate_count of this MatchTimeseries2018.

        Number of POWER CUBES in the LEVITATE section of the blue alliance VAULT.  # noqa: E501

        :param blue_levitate_count: The blue_levitate_count of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._blue_levitate_count = blue_levitate_count

    @property
    def blue_levitate_played(self):
        """Gets the blue_levitate_played of this MatchTimeseries2018.  # noqa: E501

        Returns 1 if the blue alliance LEVITATE was played, or 0 if not played.  # noqa: E501

        :return: The blue_levitate_played of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._blue_levitate_played

    @blue_levitate_played.setter
    def blue_levitate_played(self, blue_levitate_played):
        """Sets the blue_levitate_played of this MatchTimeseries2018.

        Returns 1 if the blue alliance LEVITATE was played, or 0 if not played.  # noqa: E501

        :param blue_levitate_played: The blue_levitate_played of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._blue_levitate_played = blue_levitate_played

    @property
    def blue_powerup_time_remaining(self):
        """Gets the blue_powerup_time_remaining of this MatchTimeseries2018.  # noqa: E501

        Number of seconds remaining in the blue alliance POWER UP time, or 0 if none is active.  # noqa: E501

        :return: The blue_powerup_time_remaining of this MatchTimeseries2018.  # noqa: E501
        :rtype: str
        """
        return self._blue_powerup_time_remaining

    @blue_powerup_time_remaining.setter
    def blue_powerup_time_remaining(self, blue_powerup_time_remaining):
        """Sets the blue_powerup_time_remaining of this MatchTimeseries2018.

        Number of seconds remaining in the blue alliance POWER UP time, or 0 if none is active.  # noqa: E501

        :param blue_powerup_time_remaining: The blue_powerup_time_remaining of this MatchTimeseries2018.  # noqa: E501
        :type: str
        """

        self._blue_powerup_time_remaining = blue_powerup_time_remaining

    @property
    def blue_scale_owned(self):
        """Gets the blue_scale_owned of this MatchTimeseries2018.  # noqa: E501

        1 if the blue alliance owns the SCALE, 0 if not.  # noqa: E501

        :return: The blue_scale_owned of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._blue_scale_owned

    @blue_scale_owned.setter
    def blue_scale_owned(self, blue_scale_owned):
        """Sets the blue_scale_owned of this MatchTimeseries2018.

        1 if the blue alliance owns the SCALE, 0 if not.  # noqa: E501

        :param blue_scale_owned: The blue_scale_owned of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._blue_scale_owned = blue_scale_owned

    @property
    def blue_score(self):
        """Gets the blue_score of this MatchTimeseries2018.  # noqa: E501

        Current score for the blue alliance.  # noqa: E501

        :return: The blue_score of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._blue_score

    @blue_score.setter
    def blue_score(self, blue_score):
        """Sets the blue_score of this MatchTimeseries2018.

        Current score for the blue alliance.  # noqa: E501

        :param blue_score: The blue_score of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._blue_score = blue_score

    @property
    def blue_switch_owned(self):
        """Gets the blue_switch_owned of this MatchTimeseries2018.  # noqa: E501

        1 if the blue alliance owns their SWITCH, 0 if not.  # noqa: E501

        :return: The blue_switch_owned of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._blue_switch_owned

    @blue_switch_owned.setter
    def blue_switch_owned(self, blue_switch_owned):
        """Sets the blue_switch_owned of this MatchTimeseries2018.

        1 if the blue alliance owns their SWITCH, 0 if not.  # noqa: E501

        :param blue_switch_owned: The blue_switch_owned of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._blue_switch_owned = blue_switch_owned

    @property
    def red_auto_quest(self):
        """Gets the red_auto_quest of this MatchTimeseries2018.  # noqa: E501

        1 if the red alliance is credited with the AUTO QUEST, 0 if not.  # noqa: E501

        :return: The red_auto_quest of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._red_auto_quest

    @red_auto_quest.setter
    def red_auto_quest(self, red_auto_quest):
        """Sets the red_auto_quest of this MatchTimeseries2018.

        1 if the red alliance is credited with the AUTO QUEST, 0 if not.  # noqa: E501

        :param red_auto_quest: The red_auto_quest of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._red_auto_quest = red_auto_quest

    @property
    def red_boost_count(self):
        """Gets the red_boost_count of this MatchTimeseries2018.  # noqa: E501

        Number of POWER CUBES in the BOOST section of the red alliance VAULT.  # noqa: E501

        :return: The red_boost_count of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._red_boost_count

    @red_boost_count.setter
    def red_boost_count(self, red_boost_count):
        """Sets the red_boost_count of this MatchTimeseries2018.

        Number of POWER CUBES in the BOOST section of the red alliance VAULT.  # noqa: E501

        :param red_boost_count: The red_boost_count of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._red_boost_count = red_boost_count

    @property
    def red_boost_played(self):
        """Gets the red_boost_played of this MatchTimeseries2018.  # noqa: E501

        Returns 1 if the red alliance BOOST was played, or 0 if not played.  # noqa: E501

        :return: The red_boost_played of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._red_boost_played

    @red_boost_played.setter
    def red_boost_played(self, red_boost_played):
        """Sets the red_boost_played of this MatchTimeseries2018.

        Returns 1 if the red alliance BOOST was played, or 0 if not played.  # noqa: E501

        :param red_boost_played: The red_boost_played of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._red_boost_played = red_boost_played

    @property
    def red_current_powerup(self):
        """Gets the red_current_powerup of this MatchTimeseries2018.  # noqa: E501

        Name of the current red alliance POWER UP being played, or `null`.  # noqa: E501

        :return: The red_current_powerup of this MatchTimeseries2018.  # noqa: E501
        :rtype: str
        """
        return self._red_current_powerup

    @red_current_powerup.setter
    def red_current_powerup(self, red_current_powerup):
        """Sets the red_current_powerup of this MatchTimeseries2018.

        Name of the current red alliance POWER UP being played, or `null`.  # noqa: E501

        :param red_current_powerup: The red_current_powerup of this MatchTimeseries2018.  # noqa: E501
        :type: str
        """

        self._red_current_powerup = red_current_powerup

    @property
    def red_face_the_boss(self):
        """Gets the red_face_the_boss of this MatchTimeseries2018.  # noqa: E501

        1 if the red alliance is credited with FACING THE BOSS, 0 if not.  # noqa: E501

        :return: The red_face_the_boss of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._red_face_the_boss

    @red_face_the_boss.setter
    def red_face_the_boss(self, red_face_the_boss):
        """Sets the red_face_the_boss of this MatchTimeseries2018.

        1 if the red alliance is credited with FACING THE BOSS, 0 if not.  # noqa: E501

        :param red_face_the_boss: The red_face_the_boss of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._red_face_the_boss = red_face_the_boss

    @property
    def red_force_count(self):
        """Gets the red_force_count of this MatchTimeseries2018.  # noqa: E501

        Number of POWER CUBES in the FORCE section of the red alliance VAULT.  # noqa: E501

        :return: The red_force_count of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._red_force_count

    @red_force_count.setter
    def red_force_count(self, red_force_count):
        """Sets the red_force_count of this MatchTimeseries2018.

        Number of POWER CUBES in the FORCE section of the red alliance VAULT.  # noqa: E501

        :param red_force_count: The red_force_count of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._red_force_count = red_force_count

    @property
    def red_force_played(self):
        """Gets the red_force_played of this MatchTimeseries2018.  # noqa: E501

        Returns 1 if the red alliance FORCE was played, or 0 if not played.  # noqa: E501

        :return: The red_force_played of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._red_force_played

    @red_force_played.setter
    def red_force_played(self, red_force_played):
        """Sets the red_force_played of this MatchTimeseries2018.

        Returns 1 if the red alliance FORCE was played, or 0 if not played.  # noqa: E501

        :param red_force_played: The red_force_played of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._red_force_played = red_force_played

    @property
    def red_levitate_count(self):
        """Gets the red_levitate_count of this MatchTimeseries2018.  # noqa: E501

        Number of POWER CUBES in the LEVITATE section of the red alliance VAULT.  # noqa: E501

        :return: The red_levitate_count of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._red_levitate_count

    @red_levitate_count.setter
    def red_levitate_count(self, red_levitate_count):
        """Sets the red_levitate_count of this MatchTimeseries2018.

        Number of POWER CUBES in the LEVITATE section of the red alliance VAULT.  # noqa: E501

        :param red_levitate_count: The red_levitate_count of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._red_levitate_count = red_levitate_count

    @property
    def red_levitate_played(self):
        """Gets the red_levitate_played of this MatchTimeseries2018.  # noqa: E501

        Returns 1 if the red alliance LEVITATE was played, or 0 if not played.  # noqa: E501

        :return: The red_levitate_played of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._red_levitate_played

    @red_levitate_played.setter
    def red_levitate_played(self, red_levitate_played):
        """Sets the red_levitate_played of this MatchTimeseries2018.

        Returns 1 if the red alliance LEVITATE was played, or 0 if not played.  # noqa: E501

        :param red_levitate_played: The red_levitate_played of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._red_levitate_played = red_levitate_played

    @property
    def red_powerup_time_remaining(self):
        """Gets the red_powerup_time_remaining of this MatchTimeseries2018.  # noqa: E501

        Number of seconds remaining in the red alliance POWER UP time, or 0 if none is active.  # noqa: E501

        :return: The red_powerup_time_remaining of this MatchTimeseries2018.  # noqa: E501
        :rtype: str
        """
        return self._red_powerup_time_remaining

    @red_powerup_time_remaining.setter
    def red_powerup_time_remaining(self, red_powerup_time_remaining):
        """Sets the red_powerup_time_remaining of this MatchTimeseries2018.

        Number of seconds remaining in the red alliance POWER UP time, or 0 if none is active.  # noqa: E501

        :param red_powerup_time_remaining: The red_powerup_time_remaining of this MatchTimeseries2018.  # noqa: E501
        :type: str
        """

        self._red_powerup_time_remaining = red_powerup_time_remaining

    @property
    def red_scale_owned(self):
        """Gets the red_scale_owned of this MatchTimeseries2018.  # noqa: E501

        1 if the red alliance owns the SCALE, 0 if not.  # noqa: E501

        :return: The red_scale_owned of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._red_scale_owned

    @red_scale_owned.setter
    def red_scale_owned(self, red_scale_owned):
        """Sets the red_scale_owned of this MatchTimeseries2018.

        1 if the red alliance owns the SCALE, 0 if not.  # noqa: E501

        :param red_scale_owned: The red_scale_owned of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._red_scale_owned = red_scale_owned

    @property
    def red_score(self):
        """Gets the red_score of this MatchTimeseries2018.  # noqa: E501

        Current score for the red alliance.  # noqa: E501

        :return: The red_score of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._red_score

    @red_score.setter
    def red_score(self, red_score):
        """Sets the red_score of this MatchTimeseries2018.

        Current score for the red alliance.  # noqa: E501

        :param red_score: The red_score of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._red_score = red_score

    @property
    def red_switch_owned(self):
        """Gets the red_switch_owned of this MatchTimeseries2018.  # noqa: E501

        1 if the red alliance owns their SWITCH, 0 if not.  # noqa: E501

        :return: The red_switch_owned of this MatchTimeseries2018.  # noqa: E501
        :rtype: int
        """
        return self._red_switch_owned

    @red_switch_owned.setter
    def red_switch_owned(self, red_switch_owned):
        """Sets the red_switch_owned of this MatchTimeseries2018.

        1 if the red alliance owns their SWITCH, 0 if not.  # noqa: E501

        :param red_switch_owned: The red_switch_owned of this MatchTimeseries2018.  # noqa: E501
        :type: int
        """

        self._red_switch_owned = red_switch_owned

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
        if not isinstance(other, MatchTimeseries2018):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchTimeseries2018):
            return True

        return self.to_dict() != other.to_dict()
