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


class EventInsights(object):
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
        'qual': 'object',
        'playoff': 'object'
    }

    attribute_map = {
        'qual': 'qual',
        'playoff': 'playoff'
    }

    def __init__(self, qual=None, playoff=None):  # noqa: E501
        """EventInsights - a model defined in OpenAPI"""  # noqa: E501

        self._qual = None
        self._playoff = None
        self.discriminator = None

        if qual is not None:
            self.qual = qual
        if playoff is not None:
            self.playoff = playoff

    @property
    def qual(self):
        """Gets the qual of this EventInsights.  # noqa: E501

        Inights for the qualification round of an event  # noqa: E501

        :return: The qual of this EventInsights.  # noqa: E501
        :rtype: object
        """
        return self._qual

    @qual.setter
    def qual(self, qual):
        """Sets the qual of this EventInsights.

        Inights for the qualification round of an event  # noqa: E501

        :param qual: The qual of this EventInsights.  # noqa: E501
        :type: object
        """

        self._qual = qual

    @property
    def playoff(self):
        """Gets the playoff of this EventInsights.  # noqa: E501

        Insights for the playoff round of an event  # noqa: E501

        :return: The playoff of this EventInsights.  # noqa: E501
        :rtype: object
        """
        return self._playoff

    @playoff.setter
    def playoff(self, playoff):
        """Sets the playoff of this EventInsights.

        Insights for the playoff round of an event  # noqa: E501

        :param playoff: The playoff of this EventInsights.  # noqa: E501
        :type: object
        """

        self._playoff = playoff

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
        if not isinstance(other, EventInsights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
