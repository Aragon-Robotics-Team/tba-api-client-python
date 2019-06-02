# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    The version of the OpenAPI document: 3.04.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class MatchScoreBreakdown2015(object):
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
        'blue': 'MatchScoreBreakdown2015Alliance',
        'red': 'MatchScoreBreakdown2015Alliance',
        'coopertition': 'str',
        'coopertition_points': 'int'
    }

    attribute_map = {
        'blue': 'blue',
        'red': 'red',
        'coopertition': 'coopertition',
        'coopertition_points': 'coopertition_points'
    }

    def __init__(self, blue=None, red=None, coopertition=None, coopertition_points=None):  # noqa: E501
        """MatchScoreBreakdown2015 - a model defined in OpenAPI"""  # noqa: E501

        self._blue = None
        self._red = None
        self._coopertition = None
        self._coopertition_points = None
        self.discriminator = None

        if blue is not None:
            self.blue = blue
        if red is not None:
            self.red = red
        if coopertition is not None:
            self.coopertition = coopertition
        if coopertition_points is not None:
            self.coopertition_points = coopertition_points

    @property
    def blue(self):
        """Gets the blue of this MatchScoreBreakdown2015.  # noqa: E501


        :return: The blue of this MatchScoreBreakdown2015.  # noqa: E501
        :rtype: MatchScoreBreakdown2015Alliance
        """
        return self._blue

    @blue.setter
    def blue(self, blue):
        """Sets the blue of this MatchScoreBreakdown2015.


        :param blue: The blue of this MatchScoreBreakdown2015.  # noqa: E501
        :type: MatchScoreBreakdown2015Alliance
        """

        self._blue = blue

    @property
    def red(self):
        """Gets the red of this MatchScoreBreakdown2015.  # noqa: E501


        :return: The red of this MatchScoreBreakdown2015.  # noqa: E501
        :rtype: MatchScoreBreakdown2015Alliance
        """
        return self._red

    @red.setter
    def red(self, red):
        """Sets the red of this MatchScoreBreakdown2015.


        :param red: The red of this MatchScoreBreakdown2015.  # noqa: E501
        :type: MatchScoreBreakdown2015Alliance
        """

        self._red = red

    @property
    def coopertition(self):
        """Gets the coopertition of this MatchScoreBreakdown2015.  # noqa: E501


        :return: The coopertition of this MatchScoreBreakdown2015.  # noqa: E501
        :rtype: str
        """
        return self._coopertition

    @coopertition.setter
    def coopertition(self, coopertition):
        """Sets the coopertition of this MatchScoreBreakdown2015.


        :param coopertition: The coopertition of this MatchScoreBreakdown2015.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Unknown", "Stack"]  # noqa: E501
        if coopertition not in allowed_values:
            raise ValueError(
                "Invalid value for `coopertition` ({0}), must be one of {1}"  # noqa: E501
                .format(coopertition, allowed_values)
            )

        self._coopertition = coopertition

    @property
    def coopertition_points(self):
        """Gets the coopertition_points of this MatchScoreBreakdown2015.  # noqa: E501


        :return: The coopertition_points of this MatchScoreBreakdown2015.  # noqa: E501
        :rtype: int
        """
        return self._coopertition_points

    @coopertition_points.setter
    def coopertition_points(self, coopertition_points):
        """Sets the coopertition_points of this MatchScoreBreakdown2015.


        :param coopertition_points: The coopertition_points of this MatchScoreBreakdown2015.  # noqa: E501
        :type: int
        """

        self._coopertition_points = coopertition_points

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
        if not isinstance(other, MatchScoreBreakdown2015):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
