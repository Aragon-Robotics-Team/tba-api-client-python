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


class TeamEventStatusPlayoff(object):
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
        'level': 'str',
        'current_level_record': 'WLTRecord',
        'record': 'WLTRecord',
        'status': 'str',
        'playoff_average': 'int'
    }

    attribute_map = {
        'level': 'level',
        'current_level_record': 'current_level_record',
        'record': 'record',
        'status': 'status',
        'playoff_average': 'playoff_average'
    }

    def __init__(self, level=None, current_level_record=None, record=None, status=None, playoff_average=None):  # noqa: E501
        """TeamEventStatusPlayoff - a model defined in OpenAPI"""  # noqa: E501

        self._level = None
        self._current_level_record = None
        self._record = None
        self._status = None
        self._playoff_average = None
        self.discriminator = None

        if level is not None:
            self.level = level
        if current_level_record is not None:
            self.current_level_record = current_level_record
        if record is not None:
            self.record = record
        if status is not None:
            self.status = status
        if playoff_average is not None:
            self.playoff_average = playoff_average

    @property
    def level(self):
        """Gets the level of this TeamEventStatusPlayoff.  # noqa: E501

        The highest playoff level the team reached.  # noqa: E501

        :return: The level of this TeamEventStatusPlayoff.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this TeamEventStatusPlayoff.

        The highest playoff level the team reached.  # noqa: E501

        :param level: The level of this TeamEventStatusPlayoff.  # noqa: E501
        :type: str
        """
        allowed_values = ["qm", "ef", "qf", "sf", "f"]  # noqa: E501
        if level not in allowed_values:
            raise ValueError(
                "Invalid value for `level` ({0}), must be one of {1}"  # noqa: E501
                .format(level, allowed_values)
            )

        self._level = level

    @property
    def current_level_record(self):
        """Gets the current_level_record of this TeamEventStatusPlayoff.  # noqa: E501


        :return: The current_level_record of this TeamEventStatusPlayoff.  # noqa: E501
        :rtype: WLTRecord
        """
        return self._current_level_record

    @current_level_record.setter
    def current_level_record(self, current_level_record):
        """Sets the current_level_record of this TeamEventStatusPlayoff.


        :param current_level_record: The current_level_record of this TeamEventStatusPlayoff.  # noqa: E501
        :type: WLTRecord
        """

        self._current_level_record = current_level_record

    @property
    def record(self):
        """Gets the record of this TeamEventStatusPlayoff.  # noqa: E501


        :return: The record of this TeamEventStatusPlayoff.  # noqa: E501
        :rtype: WLTRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this TeamEventStatusPlayoff.


        :param record: The record of this TeamEventStatusPlayoff.  # noqa: E501
        :type: WLTRecord
        """

        self._record = record

    @property
    def status(self):
        """Gets the status of this TeamEventStatusPlayoff.  # noqa: E501

        Current competition status for the playoffs.  # noqa: E501

        :return: The status of this TeamEventStatusPlayoff.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TeamEventStatusPlayoff.

        Current competition status for the playoffs.  # noqa: E501

        :param status: The status of this TeamEventStatusPlayoff.  # noqa: E501
        :type: str
        """
        allowed_values = ["won", "eliminated", "playing"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def playoff_average(self):
        """Gets the playoff_average of this TeamEventStatusPlayoff.  # noqa: E501

        The average match score during playoffs. Year specific. May be null if not relevant for a given year.  # noqa: E501

        :return: The playoff_average of this TeamEventStatusPlayoff.  # noqa: E501
        :rtype: int
        """
        return self._playoff_average

    @playoff_average.setter
    def playoff_average(self, playoff_average):
        """Sets the playoff_average of this TeamEventStatusPlayoff.

        The average match score during playoffs. Year specific. May be null if not relevant for a given year.  # noqa: E501

        :param playoff_average: The playoff_average of this TeamEventStatusPlayoff.  # noqa: E501
        :type: int
        """

        self._playoff_average = playoff_average

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
        if not isinstance(other, TeamEventStatusPlayoff):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
