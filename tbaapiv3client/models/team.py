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


class Team(object):
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
        'key': 'str',
        'team_number': 'int',
        'nickname': 'str',
        'name': 'str',
        'city': 'str',
        'state_prov': 'str',
        'country': 'str',
        'address': 'str',
        'postal_code': 'str',
        'gmaps_place_id': 'str',
        'gmaps_url': 'str',
        'lat': 'float',
        'lng': 'float',
        'location_name': 'str',
        'website': 'str',
        'rookie_year': 'int',
        'motto': 'str',
        'home_championship': 'object'
    }

    attribute_map = {
        'key': 'key',
        'team_number': 'team_number',
        'nickname': 'nickname',
        'name': 'name',
        'city': 'city',
        'state_prov': 'state_prov',
        'country': 'country',
        'address': 'address',
        'postal_code': 'postal_code',
        'gmaps_place_id': 'gmaps_place_id',
        'gmaps_url': 'gmaps_url',
        'lat': 'lat',
        'lng': 'lng',
        'location_name': 'location_name',
        'website': 'website',
        'rookie_year': 'rookie_year',
        'motto': 'motto',
        'home_championship': 'home_championship'
    }

    def __init__(self, key=None, team_number=None, nickname=None, name=None, city=None, state_prov=None, country=None, address=None, postal_code=None, gmaps_place_id=None, gmaps_url=None, lat=None, lng=None, location_name=None, website=None, rookie_year=None, motto=None, home_championship=None, local_vars_configuration=None):  # noqa: E501
        """Team - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._team_number = None
        self._nickname = None
        self._name = None
        self._city = None
        self._state_prov = None
        self._country = None
        self._address = None
        self._postal_code = None
        self._gmaps_place_id = None
        self._gmaps_url = None
        self._lat = None
        self._lng = None
        self._location_name = None
        self._website = None
        self._rookie_year = None
        self._motto = None
        self._home_championship = None
        self.discriminator = None

        self.key = key
        self.team_number = team_number
        if nickname is not None:
            self.nickname = nickname
        self.name = name
        if city is not None:
            self.city = city
        if state_prov is not None:
            self.state_prov = state_prov
        if country is not None:
            self.country = country
        if address is not None:
            self.address = address
        if postal_code is not None:
            self.postal_code = postal_code
        if gmaps_place_id is not None:
            self.gmaps_place_id = gmaps_place_id
        if gmaps_url is not None:
            self.gmaps_url = gmaps_url
        if lat is not None:
            self.lat = lat
        if lng is not None:
            self.lng = lng
        if location_name is not None:
            self.location_name = location_name
        if website is not None:
            self.website = website
        if rookie_year is not None:
            self.rookie_year = rookie_year
        if motto is not None:
            self.motto = motto
        if home_championship is not None:
            self.home_championship = home_championship

    @property
    def key(self):
        """Gets the key of this Team.  # noqa: E501

        TBA team key with the format `frcXXXX` with `XXXX` representing the team number.  # noqa: E501

        :return: The key of this Team.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Team.

        TBA team key with the format `frcXXXX` with `XXXX` representing the team number.  # noqa: E501

        :param key: The key of this Team.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def team_number(self):
        """Gets the team_number of this Team.  # noqa: E501

        Official team number issued by FIRST.  # noqa: E501

        :return: The team_number of this Team.  # noqa: E501
        :rtype: int
        """
        return self._team_number

    @team_number.setter
    def team_number(self, team_number):
        """Sets the team_number of this Team.

        Official team number issued by FIRST.  # noqa: E501

        :param team_number: The team_number of this Team.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and team_number is None:  # noqa: E501
            raise ValueError("Invalid value for `team_number`, must not be `None`")  # noqa: E501

        self._team_number = team_number

    @property
    def nickname(self):
        """Gets the nickname of this Team.  # noqa: E501

        Team nickname provided by FIRST.  # noqa: E501

        :return: The nickname of this Team.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this Team.

        Team nickname provided by FIRST.  # noqa: E501

        :param nickname: The nickname of this Team.  # noqa: E501
        :type: str
        """

        self._nickname = nickname

    @property
    def name(self):
        """Gets the name of this Team.  # noqa: E501

        Official long name registered with FIRST.  # noqa: E501

        :return: The name of this Team.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Team.

        Official long name registered with FIRST.  # noqa: E501

        :param name: The name of this Team.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def city(self):
        """Gets the city of this Team.  # noqa: E501

        City of team derived from parsing the address registered with FIRST.  # noqa: E501

        :return: The city of this Team.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Team.

        City of team derived from parsing the address registered with FIRST.  # noqa: E501

        :param city: The city of this Team.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state_prov(self):
        """Gets the state_prov of this Team.  # noqa: E501

        State of team derived from parsing the address registered with FIRST.  # noqa: E501

        :return: The state_prov of this Team.  # noqa: E501
        :rtype: str
        """
        return self._state_prov

    @state_prov.setter
    def state_prov(self, state_prov):
        """Sets the state_prov of this Team.

        State of team derived from parsing the address registered with FIRST.  # noqa: E501

        :param state_prov: The state_prov of this Team.  # noqa: E501
        :type: str
        """

        self._state_prov = state_prov

    @property
    def country(self):
        """Gets the country of this Team.  # noqa: E501

        Country of team derived from parsing the address registered with FIRST.  # noqa: E501

        :return: The country of this Team.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Team.

        Country of team derived from parsing the address registered with FIRST.  # noqa: E501

        :param country: The country of this Team.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def address(self):
        """Gets the address of this Team.  # noqa: E501

        Will be NULL, for future development.  # noqa: E501

        :return: The address of this Team.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Team.

        Will be NULL, for future development.  # noqa: E501

        :param address: The address of this Team.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def postal_code(self):
        """Gets the postal_code of this Team.  # noqa: E501

        Postal code from the team address.  # noqa: E501

        :return: The postal_code of this Team.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Team.

        Postal code from the team address.  # noqa: E501

        :param postal_code: The postal_code of this Team.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def gmaps_place_id(self):
        """Gets the gmaps_place_id of this Team.  # noqa: E501

        Will be NULL, for future development.  # noqa: E501

        :return: The gmaps_place_id of this Team.  # noqa: E501
        :rtype: str
        """
        return self._gmaps_place_id

    @gmaps_place_id.setter
    def gmaps_place_id(self, gmaps_place_id):
        """Sets the gmaps_place_id of this Team.

        Will be NULL, for future development.  # noqa: E501

        :param gmaps_place_id: The gmaps_place_id of this Team.  # noqa: E501
        :type: str
        """

        self._gmaps_place_id = gmaps_place_id

    @property
    def gmaps_url(self):
        """Gets the gmaps_url of this Team.  # noqa: E501

        Will be NULL, for future development.  # noqa: E501

        :return: The gmaps_url of this Team.  # noqa: E501
        :rtype: str
        """
        return self._gmaps_url

    @gmaps_url.setter
    def gmaps_url(self, gmaps_url):
        """Sets the gmaps_url of this Team.

        Will be NULL, for future development.  # noqa: E501

        :param gmaps_url: The gmaps_url of this Team.  # noqa: E501
        :type: str
        """

        self._gmaps_url = gmaps_url

    @property
    def lat(self):
        """Gets the lat of this Team.  # noqa: E501

        Will be NULL, for future development.  # noqa: E501

        :return: The lat of this Team.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Team.

        Will be NULL, for future development.  # noqa: E501

        :param lat: The lat of this Team.  # noqa: E501
        :type: float
        """

        self._lat = lat

    @property
    def lng(self):
        """Gets the lng of this Team.  # noqa: E501

        Will be NULL, for future development.  # noqa: E501

        :return: The lng of this Team.  # noqa: E501
        :rtype: float
        """
        return self._lng

    @lng.setter
    def lng(self, lng):
        """Sets the lng of this Team.

        Will be NULL, for future development.  # noqa: E501

        :param lng: The lng of this Team.  # noqa: E501
        :type: float
        """

        self._lng = lng

    @property
    def location_name(self):
        """Gets the location_name of this Team.  # noqa: E501

        Will be NULL, for future development.  # noqa: E501

        :return: The location_name of this Team.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this Team.

        Will be NULL, for future development.  # noqa: E501

        :param location_name: The location_name of this Team.  # noqa: E501
        :type: str
        """

        self._location_name = location_name

    @property
    def website(self):
        """Gets the website of this Team.  # noqa: E501

        Official website associated with the team.  # noqa: E501

        :return: The website of this Team.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Team.

        Official website associated with the team.  # noqa: E501

        :param website: The website of this Team.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def rookie_year(self):
        """Gets the rookie_year of this Team.  # noqa: E501

        First year the team officially competed.  # noqa: E501

        :return: The rookie_year of this Team.  # noqa: E501
        :rtype: int
        """
        return self._rookie_year

    @rookie_year.setter
    def rookie_year(self, rookie_year):
        """Sets the rookie_year of this Team.

        First year the team officially competed.  # noqa: E501

        :param rookie_year: The rookie_year of this Team.  # noqa: E501
        :type: int
        """

        self._rookie_year = rookie_year

    @property
    def motto(self):
        """Gets the motto of this Team.  # noqa: E501

        Team's motto as provided by FIRST. This field is deprecated and will return null - will be removed at end-of-season in 2019.  # noqa: E501

        :return: The motto of this Team.  # noqa: E501
        :rtype: str
        """
        return self._motto

    @motto.setter
    def motto(self, motto):
        """Sets the motto of this Team.

        Team's motto as provided by FIRST. This field is deprecated and will return null - will be removed at end-of-season in 2019.  # noqa: E501

        :param motto: The motto of this Team.  # noqa: E501
        :type: str
        """

        self._motto = motto

    @property
    def home_championship(self):
        """Gets the home_championship of this Team.  # noqa: E501

        Location of the team's home championship each year as a key-value pair. The year (as a string) is the key, and the city is the value.  # noqa: E501

        :return: The home_championship of this Team.  # noqa: E501
        :rtype: object
        """
        return self._home_championship

    @home_championship.setter
    def home_championship(self, home_championship):
        """Sets the home_championship of this Team.

        Location of the team's home championship each year as a key-value pair. The year (as a string) is the key, and the city is the value.  # noqa: E501

        :param home_championship: The home_championship of this Team.  # noqa: E501
        :type: object
        """

        self._home_championship = home_championship

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
        if not isinstance(other, Team):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Team):
            return True

        return self.to_dict() != other.to_dict()
