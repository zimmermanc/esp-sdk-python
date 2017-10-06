# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
from ..extensions.base_object import BaseObject
import re


class Tag(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, key=None, value=None, created_at=None, updated_at=None):
        """
        Tag - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'key': 'str',
            'value': 'str',
            'created_at': 'datetime',
            'updated_at': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'key': 'key',
            'value': 'value',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._id = id
        self._key = key
        self._value = value
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self):
        """
        Gets the id of this Tag.
        Unique ID

        :return: The id of this Tag.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Tag.
        Unique ID

        :param id: The id of this Tag.
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """
        Gets the key of this Tag.
        Tag key name in AWS

        :return: The key of this Tag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Tag.
        Tag key name in AWS

        :param key: The key of this Tag.
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """
        Gets the value of this Tag.
        Tag value in AWS

        :return: The value of this Tag.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Tag.
        Tag value in AWS

        :param value: The value of this Tag.
        :type: str
        """

        self._value = value

    @property
    def created_at(self):
        """
        Gets the created_at of this Tag.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this Tag.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Tag.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this Tag.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Tag.
        ISO 8601 timestamp when the resource was updated

        :return: The updated_at of this Tag.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Tag.
        ISO 8601 timestamp when the resource was updated

        :param updated_at: The updated_at of this Tag.
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
