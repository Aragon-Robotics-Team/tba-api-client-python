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


class MatchAlliance(object):
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
        'score': 'int',
        'team_keys': 'list[str]',
        'surrogate_team_keys': 'list[str]',
        'dq_team_keys': 'list[str]'
    }

    attribute_map = {
        'score': 'score',
        'team_keys': 'team_keys',
        'surrogate_team_keys': 'surrogate_team_keys',
        'dq_team_keys': 'dq_team_keys'
    }

    def __init__(self, score=None, team_keys=None, surrogate_team_keys=None, dq_team_keys=None, local_vars_configuration=None):  # noqa: E501
        """MatchAlliance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._score = None
        self._team_keys = None
        self._surrogate_team_keys = None
        self._dq_team_keys = None
        self.discriminator = None

        self.score = score
        self.team_keys = team_keys
        if surrogate_team_keys is not None:
            self.surrogate_team_keys = surrogate_team_keys
        if dq_team_keys is not None:
            self.dq_team_keys = dq_team_keys

    @property
    def score(self):
        """Gets the score of this MatchAlliance.  # noqa: E501

        Score for this alliance. Will be null or -1 for an unplayed match.  # noqa: E501

        :return: The score of this MatchAlliance.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this MatchAlliance.

        Score for this alliance. Will be null or -1 for an unplayed match.  # noqa: E501

        :param score: The score of this MatchAlliance.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and score is None:  # noqa: E501
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

    @property
    def team_keys(self):
        """Gets the team_keys of this MatchAlliance.  # noqa: E501


        :return: The team_keys of this MatchAlliance.  # noqa: E501
        :rtype: list[str]
        """
        return self._team_keys

    @team_keys.setter
    def team_keys(self, team_keys):
        """Sets the team_keys of this MatchAlliance.


        :param team_keys: The team_keys of this MatchAlliance.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and team_keys is None:  # noqa: E501
            raise ValueError("Invalid value for `team_keys`, must not be `None`")  # noqa: E501

        self._team_keys = team_keys

    @property
    def surrogate_team_keys(self):
        """Gets the surrogate_team_keys of this MatchAlliance.  # noqa: E501

        TBA team keys (eg `frc254`) of any teams playing as a surrogate.  # noqa: E501

        :return: The surrogate_team_keys of this MatchAlliance.  # noqa: E501
        :rtype: list[str]
        """
        return self._surrogate_team_keys

    @surrogate_team_keys.setter
    def surrogate_team_keys(self, surrogate_team_keys):
        """Sets the surrogate_team_keys of this MatchAlliance.

        TBA team keys (eg `frc254`) of any teams playing as a surrogate.  # noqa: E501

        :param surrogate_team_keys: The surrogate_team_keys of this MatchAlliance.  # noqa: E501
        :type: list[str]
        """

        self._surrogate_team_keys = surrogate_team_keys

    @property
    def dq_team_keys(self):
        """Gets the dq_team_keys of this MatchAlliance.  # noqa: E501

        TBA team keys (eg `frc254`) of any disqualified teams.  # noqa: E501

        :return: The dq_team_keys of this MatchAlliance.  # noqa: E501
        :rtype: list[str]
        """
        return self._dq_team_keys

    @dq_team_keys.setter
    def dq_team_keys(self, dq_team_keys):
        """Sets the dq_team_keys of this MatchAlliance.

        TBA team keys (eg `frc254`) of any disqualified teams.  # noqa: E501

        :param dq_team_keys: The dq_team_keys of this MatchAlliance.  # noqa: E501
        :type: list[str]
        """

        self._dq_team_keys = dq_team_keys

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
        if not isinstance(other, MatchAlliance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchAlliance):
            return True

        return self.to_dict() != other.to_dict()
