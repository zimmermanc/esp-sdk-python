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


class Service(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, code=None, default_interval=None, minimum_interval=None, created_at=None, name=None, policy_name=None, updated_at=None, provider=None):
        """
        Service - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'code': 'str',
            'default_interval': 'int',
            'minimum_interval': 'int',
            'created_at': 'datetime',
            'name': 'str',
            'policy_name': 'str',
            'updated_at': 'datetime',
            'provider': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'code': 'code',
            'default_interval': 'default_interval',
            'minimum_interval': 'minimum_interval',
            'created_at': 'created_at',
            'name': 'name',
            'policy_name': 'policy_name',
            'updated_at': 'updated_at',
            'provider': 'provider'
        }

        self._id = id
        self._code = code
        self._default_interval = default_interval
        self._minimum_interval = minimum_interval
        self._created_at = created_at
        self._name = name
        self._policy_name = policy_name
        self._updated_at = updated_at
        self._provider = provider

    @property
    def id(self):
        """
        Gets the id of this Service.
        Unique ID

        :return: The id of this Service.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Service.
        Unique ID

        :param id: The id of this Service.
        :type: int
        """

        self._id = id

    @property
    def code(self):
        """
        Gets the code of this Service.
        The code associated with this service

        :return: The code of this Service.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Service.
        The code associated with this service

        :param code: The code of this Service.
        :type: str
        """

        self._code = code

    @property
    def default_interval(self):
        """
        Gets the default_interval of this Service.
        Default interval used for scans if a scan interval was not created

        :return: The default_interval of this Service.
        :rtype: int
        """
        return self._default_interval

    @default_interval.setter
    def default_interval(self, default_interval):
        """
        Sets the default_interval of this Service.
        Default interval used for scans if a scan interval was not created

        :param default_interval: The default_interval of this Service.
        :type: int
        """

        self._default_interval = default_interval

    @property
    def minimum_interval(self):
        """
        Gets the minimum_interval of this Service.
        Minimum interval allowed for scans on this service

        :return: The minimum_interval of this Service.
        :rtype: int
        """
        return self._minimum_interval

    @minimum_interval.setter
    def minimum_interval(self, minimum_interval):
        """
        Sets the minimum_interval of this Service.
        Minimum interval allowed for scans on this service

        :param minimum_interval: The minimum_interval of this Service.
        :type: int
        """

        self._minimum_interval = minimum_interval

    @property
    def created_at(self):
        """
        Gets the created_at of this Service.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this Service.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Service.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this Service.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def name(self):
        """
        Gets the name of this Service.
        The name of the service

        :return: The name of this Service.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Service.
        The name of the service

        :param name: The name of this Service.
        :type: str
        """

        self._name = name

    @property
    def policy_name(self):
        """
        Gets the policy_name of this Service.
        The policy name of the service. This matches the namespace set by Amazon

        :return: The policy_name of this Service.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """
        Sets the policy_name of this Service.
        The policy name of the service. This matches the namespace set by Amazon

        :param policy_name: The policy_name of this Service.
        :type: str
        """

        self._policy_name = policy_name

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Service.
        ISO 8601 timestamp when the resource was updated

        :return: The updated_at of this Service.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Service.
        ISO 8601 timestamp when the resource was updated

        :param updated_at: The updated_at of this Service.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def provider(self):
        """
        Gets the provider of this Service.
        The cloud provider this account is for

        :return: The provider of this Service.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this Service.
        The cloud provider this account is for

        :param provider: The provider of this Service.
        :type: str
        """

        self._provider = provider

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
        if not isinstance(other, Service):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
