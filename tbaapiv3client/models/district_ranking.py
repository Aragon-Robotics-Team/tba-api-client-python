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


class DistrictRanking(object):
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
        'team_key': 'str',
        'rank': 'int',
        'rookie_bonus': 'int',
        'point_total': 'int',
        'event_points': 'list[DistrictRankingEventPoints]'
    }

    attribute_map = {
        'team_key': 'team_key',
        'rank': 'rank',
        'rookie_bonus': 'rookie_bonus',
        'point_total': 'point_total',
        'event_points': 'event_points'
    }

    def __init__(self, team_key=None, rank=None, rookie_bonus=None, point_total=None, event_points=None):  # noqa: E501
        """DistrictRanking - a model defined in OpenAPI"""  # noqa: E501

        self._team_key = None
        self._rank = None
        self._rookie_bonus = None
        self._point_total = None
        self._event_points = None
        self.discriminator = None

        self.team_key = team_key
        self.rank = rank
        if rookie_bonus is not None:
            self.rookie_bonus = rookie_bonus
        self.point_total = point_total
        if event_points is not None:
            self.event_points = event_points

    @property
    def team_key(self):
        """Gets the team_key of this DistrictRanking.  # noqa: E501

        TBA team key for the team.  # noqa: E501

        :return: The team_key of this DistrictRanking.  # noqa: E501
        :rtype: str
        """
        return self._team_key

    @team_key.setter
    def team_key(self, team_key):
        """Sets the team_key of this DistrictRanking.

        TBA team key for the team.  # noqa: E501

        :param team_key: The team_key of this DistrictRanking.  # noqa: E501
        :type: str
        """
        if team_key is None:
            raise ValueError("Invalid value for `team_key`, must not be `None`")  # noqa: E501

        self._team_key = team_key

    @property
    def rank(self):
        """Gets the rank of this DistrictRanking.  # noqa: E501

        Numerical rank of the team, 1 being top rank.  # noqa: E501

        :return: The rank of this DistrictRanking.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this DistrictRanking.

        Numerical rank of the team, 1 being top rank.  # noqa: E501

        :param rank: The rank of this DistrictRanking.  # noqa: E501
        :type: int
        """
        if rank is None:
            raise ValueError("Invalid value for `rank`, must not be `None`")  # noqa: E501

        self._rank = rank

    @property
    def rookie_bonus(self):
        """Gets the rookie_bonus of this DistrictRanking.  # noqa: E501

        Any points added to a team as a result of the rookie bonus.  # noqa: E501

        :return: The rookie_bonus of this DistrictRanking.  # noqa: E501
        :rtype: int
        """
        return self._rookie_bonus

    @rookie_bonus.setter
    def rookie_bonus(self, rookie_bonus):
        """Sets the rookie_bonus of this DistrictRanking.

        Any points added to a team as a result of the rookie bonus.  # noqa: E501

        :param rookie_bonus: The rookie_bonus of this DistrictRanking.  # noqa: E501
        :type: int
        """

        self._rookie_bonus = rookie_bonus

    @property
    def point_total(self):
        """Gets the point_total of this DistrictRanking.  # noqa: E501

        Total district points for the team.  # noqa: E501

        :return: The point_total of this DistrictRanking.  # noqa: E501
        :rtype: int
        """
        return self._point_total

    @point_total.setter
    def point_total(self, point_total):
        """Sets the point_total of this DistrictRanking.

        Total district points for the team.  # noqa: E501

        :param point_total: The point_total of this DistrictRanking.  # noqa: E501
        :type: int
        """
        if point_total is None:
            raise ValueError("Invalid value for `point_total`, must not be `None`")  # noqa: E501

        self._point_total = point_total

    @property
    def event_points(self):
        """Gets the event_points of this DistrictRanking.  # noqa: E501

        List of events that contributed to the point total for the team.  # noqa: E501

        :return: The event_points of this DistrictRanking.  # noqa: E501
        :rtype: list[DistrictRankingEventPoints]
        """
        return self._event_points

    @event_points.setter
    def event_points(self, event_points):
        """Sets the event_points of this DistrictRanking.

        List of events that contributed to the point total for the team.  # noqa: E501

        :param event_points: The event_points of this DistrictRanking.  # noqa: E501
        :type: list[DistrictRankingEventPoints]
        """

        self._event_points = event_points

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
        if not isinstance(other, DistrictRanking):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
