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


class TeamEventStatusAllianceBackup(object):
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
        'out': 'str',
        '_in': 'str'
    }

    attribute_map = {
        'out': 'out',
        '_in': 'in'
    }

    def __init__(self, out=None, _in=None):  # noqa: E501
        """TeamEventStatusAllianceBackup - a model defined in OpenAPI"""  # noqa: E501

        self._out = None
        self.__in = None
        self.discriminator = None

        if out is not None:
            self.out = out
        if _in is not None:
            self._in = _in

    @property
    def out(self):
        """Gets the out of this TeamEventStatusAllianceBackup.  # noqa: E501

        TBA key for the team replaced by the backup.  # noqa: E501

        :return: The out of this TeamEventStatusAllianceBackup.  # noqa: E501
        :rtype: str
        """
        return self._out

    @out.setter
    def out(self, out):
        """Sets the out of this TeamEventStatusAllianceBackup.

        TBA key for the team replaced by the backup.  # noqa: E501

        :param out: The out of this TeamEventStatusAllianceBackup.  # noqa: E501
        :type: str
        """

        self._out = out

    @property
    def _in(self):
        """Gets the _in of this TeamEventStatusAllianceBackup.  # noqa: E501

        TBA key for the backup team called in.  # noqa: E501

        :return: The _in of this TeamEventStatusAllianceBackup.  # noqa: E501
        :rtype: str
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this TeamEventStatusAllianceBackup.

        TBA key for the backup team called in.  # noqa: E501

        :param _in: The _in of this TeamEventStatusAllianceBackup.  # noqa: E501
        :type: str
        """

        self.__in = _in

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
        if not isinstance(other, TeamEventStatusAllianceBackup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
