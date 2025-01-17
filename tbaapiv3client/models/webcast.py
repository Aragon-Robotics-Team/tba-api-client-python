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


class Webcast(object):
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
        'type': 'str',
        'channel': 'str',
        'file': 'str'
    }

    attribute_map = {
        'type': 'type',
        'channel': 'channel',
        'file': 'file'
    }

    def __init__(self, type=None, channel=None, file=None, local_vars_configuration=None):  # noqa: E501
        """Webcast - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._channel = None
        self._file = None
        self.discriminator = None

        self.type = type
        self.channel = channel
        if file is not None:
            self.file = file

    @property
    def type(self):
        """Gets the type of this Webcast.  # noqa: E501

        Type of webcast, typically descriptive of the streaming provider.  # noqa: E501

        :return: The type of this Webcast.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Webcast.

        Type of webcast, typically descriptive of the streaming provider.  # noqa: E501

        :param type: The type of this Webcast.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["youtube", "twitch", "ustream", "iframe", "html5", "rtmp", "livestream", "direct_link", "mms", "justin", "stemtv", "dacast"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def channel(self):
        """Gets the channel of this Webcast.  # noqa: E501

        Type specific channel information. May be the YouTube stream, or Twitch channel name. In the case of iframe types, contains HTML to embed the stream in an HTML iframe.  # noqa: E501

        :return: The channel of this Webcast.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this Webcast.

        Type specific channel information. May be the YouTube stream, or Twitch channel name. In the case of iframe types, contains HTML to embed the stream in an HTML iframe.  # noqa: E501

        :param channel: The channel of this Webcast.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and channel is None:  # noqa: E501
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def file(self):
        """Gets the file of this Webcast.  # noqa: E501

        File identification as may be required for some types. May be null.  # noqa: E501

        :return: The file of this Webcast.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Webcast.

        File identification as may be required for some types. May be null.  # noqa: E501

        :param file: The file of this Webcast.  # noqa: E501
        :type: str
        """

        self._file = file

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
        if not isinstance(other, Webcast):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Webcast):
            return True

        return self.to_dict() != other.to_dict()
