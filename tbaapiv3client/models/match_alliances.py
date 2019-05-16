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


class MatchAlliances(object):
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
        'red': 'MatchAlliance',
        'blue': 'MatchAlliance'
    }

    attribute_map = {
        'red': 'red',
        'blue': 'blue'
    }

    def __init__(self, red=None, blue=None):  # noqa: E501
        """MatchAlliances - a model defined in OpenAPI"""  # noqa: E501

        self._red = None
        self._blue = None
        self.discriminator = None

        if red is not None:
            self.red = red
        if blue is not None:
            self.blue = blue

    @property
    def red(self):
        """Gets the red of this MatchAlliances.  # noqa: E501


        :return: The red of this MatchAlliances.  # noqa: E501
        :rtype: MatchAlliance
        """
        return self._red

    @red.setter
    def red(self, red):
        """Sets the red of this MatchAlliances.


        :param red: The red of this MatchAlliances.  # noqa: E501
        :type: MatchAlliance
        """

        self._red = red

    @property
    def blue(self):
        """Gets the blue of this MatchAlliances.  # noqa: E501


        :return: The blue of this MatchAlliances.  # noqa: E501
        :rtype: MatchAlliance
        """
        return self._blue

    @blue.setter
    def blue(self, blue):
        """Sets the blue of this MatchAlliances.


        :param blue: The blue of this MatchAlliances.  # noqa: E501
        :type: MatchAlliance
        """

        self._blue = blue

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
        if not isinstance(other, MatchAlliances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
