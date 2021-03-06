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


class Attribution(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, event_id=None, event_name=None, event_time=None, raw_event=None, user=None, ip_address=None, scope_name=None, alert=None, alert_id=None):
        """
        Attribution - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'event_id': 'int',
            'event_name': 'str',
            'event_time': 'datetime',
            'raw_event': 'object',
            'user': 'str',
            'ip_address': 'str',
            'scope_name': 'str',
            'alert': 'Alert',
            'alert_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'event_id': 'event_id',
            'event_name': 'event_name',
            'event_time': 'event_time',
            'raw_event': 'raw_event',
            'user': 'user',
            'ip_address': 'ip_address',
            'scope_name': 'scope_name',
            'alert': 'alert',
            'alert_id': 'alert_id'
        }

        self._id = id
        self._event_id = event_id
        self._event_name = event_name
        self._event_time = event_time
        self._raw_event = raw_event
        self._user = user
        self._ip_address = ip_address
        self._scope_name = scope_name
        self._alert = alert
        self._alert_id = alert_id

    @property
    def id(self):
        """
        Gets the id of this Attribution.
        Unique ID

        :return: The id of this Attribution.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Attribution.
        Unique ID

        :param id: The id of this Attribution.
        :type: int
        """

        self._id = id

    @property
    def event_id(self):
        """
        Gets the event_id of this Attribution.
        GUID to uniquely identify each event

        :return: The event_id of this Attribution.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this Attribution.
        GUID to uniquely identify each event

        :param event_id: The event_id of this Attribution.
        :type: int
        """

        self._event_id = event_id

    @property
    def event_name(self):
        """
        Gets the event_name of this Attribution.
        The requested action, which is one of the actions listed in the API Reference for the service

        :return: The event_name of this Attribution.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this Attribution.
        The requested action, which is one of the actions listed in the API Reference for the service

        :param event_name: The event_name of this Attribution.
        :type: str
        """

        self._event_name = event_name

    @property
    def event_time(self):
        """
        Gets the event_time of this Attribution.
        ISO 8601 timestamp when the event occurred

        :return: The event_time of this Attribution.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """
        Sets the event_time of this Attribution.
        ISO 8601 timestamp when the event occurred

        :param event_time: The event_time of this Attribution.
        :type: datetime
        """

        self._event_time = event_time

    @property
    def raw_event(self):
        """
        Gets the raw_event of this Attribution.
        The event as it is sent in

        :return: The raw_event of this Attribution.
        :rtype: object
        """
        return self._raw_event

    @raw_event.setter
    def raw_event(self, raw_event):
        """
        Sets the raw_event of this Attribution.
        The event as it is sent in

        :param raw_event: The raw_event of this Attribution.
        :type: object
        """

        self._raw_event = raw_event

    @property
    def user(self):
        """
        Gets the user of this Attribution.
        The user associated with the event

        :return: The user of this Attribution.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Attribution.
        The user associated with the event

        :param user: The user of this Attribution.
        :type: str
        """

        self._user = user

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Attribution.
        The apparent IP address that the request was made from for the given event

        :return: The ip_address of this Attribution.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Attribution.
        The apparent IP address that the request was made from for the given event

        :param ip_address: The ip_address of this Attribution.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def scope_name(self):
        """
        Gets the scope_name of this Attribution.
        The agent through which the request was made, such as the AWS Management Console or an AWS SDK

        :return: The scope_name of this Attribution.
        :rtype: str
        """
        return self._scope_name

    @scope_name.setter
    def scope_name(self, scope_name):
        """
        Sets the scope_name of this Attribution.
        The agent through which the request was made, such as the AWS Management Console or an AWS SDK

        :param scope_name: The scope_name of this Attribution.
        :type: str
        """

        self._scope_name = scope_name

    @property
    def alert(self):
        """
        Gets the alert of this Attribution.
        Associated Alert

        :return: The alert of this Attribution.
        :rtype: Alert
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        """
        Sets the alert of this Attribution.
        Associated Alert

        :param alert: The alert of this Attribution.
        :type: Alert
        """

        self._alert = alert

    @property
    def alert_id(self):
        """
        Gets the alert_id of this Attribution.
        Associated Alert ID

        :return: The alert_id of this Attribution.
        :rtype: int
        """
        return self._alert_id

    @alert_id.setter
    def alert_id(self, alert_id):
        """
        Sets the alert_id of this Attribution.
        Associated Alert ID

        :param alert_id: The alert_id of this Attribution.
        :type: int
        """

        self._alert_id = alert_id

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
        if not isinstance(other, Attribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
