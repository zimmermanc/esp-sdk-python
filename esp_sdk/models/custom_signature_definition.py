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


class CustomSignatureDefinition(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, code=None, updated_at=None, created_at=None, version_number=None, language=None, status=None, custom_signature=None, custom_signature_id=None, results=None, result_ids=None):
        """
        CustomSignatureDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'code': 'str',
            'updated_at': 'datetime',
            'created_at': 'datetime',
            'version_number': 'int',
            'language': 'str',
            'status': 'str',
            'custom_signature': 'CustomSignature',
            'custom_signature_id': 'int',
            'results': 'list[CustomSignatureResult]',
            'result_ids': 'list[int]'
        }

        self.attribute_map = {
            'id': 'id',
            'code': 'code',
            'updated_at': 'updated_at',
            'created_at': 'created_at',
            'version_number': 'version_number',
            'language': 'language',
            'status': 'status',
            'custom_signature': 'custom_signature',
            'custom_signature_id': 'custom_signature_id',
            'results': 'results',
            'result_ids': 'result_ids'
        }

        self._id = id
        self._code = code
        self._updated_at = updated_at
        self._created_at = created_at
        self._version_number = version_number
        self._language = language
        self._status = status
        self._custom_signature = custom_signature
        self._custom_signature_id = custom_signature_id
        self._results = results
        self._result_ids = result_ids

    @property
    def id(self):
        """
        Gets the id of this CustomSignatureDefinition.
        Unique ID

        :return: The id of this CustomSignatureDefinition.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CustomSignatureDefinition.
        Unique ID

        :param id: The id of this CustomSignatureDefinition.
        :type: int
        """

        self._id = id

    @property
    def code(self):
        """
        Gets the code of this CustomSignatureDefinition.
        The code for this definition

        :return: The code of this CustomSignatureDefinition.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this CustomSignatureDefinition.
        The code for this definition

        :param code: The code of this CustomSignatureDefinition.
        :type: str
        """

        self._code = code

    @property
    def updated_at(self):
        """
        Gets the updated_at of this CustomSignatureDefinition.
        ISO 8601 timestamp when the resource was updated

        :return: The updated_at of this CustomSignatureDefinition.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this CustomSignatureDefinition.
        ISO 8601 timestamp when the resource was updated

        :param updated_at: The updated_at of this CustomSignatureDefinition.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def created_at(self):
        """
        Gets the created_at of this CustomSignatureDefinition.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this CustomSignatureDefinition.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CustomSignatureDefinition.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this CustomSignatureDefinition.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def version_number(self):
        """
        Gets the version_number of this CustomSignatureDefinition.
        Version of definition

        :return: The version_number of this CustomSignatureDefinition.
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """
        Sets the version_number of this CustomSignatureDefinition.
        Version of definition

        :param version_number: The version_number of this CustomSignatureDefinition.
        :type: int
        """

        self._version_number = version_number

    @property
    def language(self):
        """
        Gets the language of this CustomSignatureDefinition.
        The language of the definition. Valid values are ruby, javascript

        :return: The language of this CustomSignatureDefinition.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this CustomSignatureDefinition.
        The language of the definition. Valid values are ruby, javascript

        :param language: The language of this CustomSignatureDefinition.
        :type: str
        """

        self._language = language

    @property
    def status(self):
        """
        Gets the status of this CustomSignatureDefinition.
        Status of the definition. Valid values are editable, validating, active, archived, disabled

        :return: The status of this CustomSignatureDefinition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CustomSignatureDefinition.
        Status of the definition. Valid values are editable, validating, active, archived, disabled

        :param status: The status of this CustomSignatureDefinition.
        :type: str
        """

        self._status = status

    @property
    def custom_signature(self):
        """
        Gets the custom_signature of this CustomSignatureDefinition.
        Associated Custom Signature

        :return: The custom_signature of this CustomSignatureDefinition.
        :rtype: CustomSignature
        """
        return self._custom_signature

    @custom_signature.setter
    def custom_signature(self, custom_signature):
        """
        Sets the custom_signature of this CustomSignatureDefinition.
        Associated Custom Signature

        :param custom_signature: The custom_signature of this CustomSignatureDefinition.
        :type: CustomSignature
        """

        self._custom_signature = custom_signature

    @property
    def custom_signature_id(self):
        """
        Gets the custom_signature_id of this CustomSignatureDefinition.
        Associated Custom Signature ID

        :return: The custom_signature_id of this CustomSignatureDefinition.
        :rtype: int
        """
        return self._custom_signature_id

    @custom_signature_id.setter
    def custom_signature_id(self, custom_signature_id):
        """
        Sets the custom_signature_id of this CustomSignatureDefinition.
        Associated Custom Signature ID

        :param custom_signature_id: The custom_signature_id of this CustomSignatureDefinition.
        :type: int
        """

        self._custom_signature_id = custom_signature_id

    @property
    def results(self):
        """
        Gets the results of this CustomSignatureDefinition.
        Associated Results

        :return: The results of this CustomSignatureDefinition.
        :rtype: list[CustomSignatureResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this CustomSignatureDefinition.
        Associated Results

        :param results: The results of this CustomSignatureDefinition.
        :type: list[CustomSignatureResult]
        """

        self._results = results

    @property
    def result_ids(self):
        """
        Gets the result_ids of this CustomSignatureDefinition.
        Associated Results IDs

        :return: The result_ids of this CustomSignatureDefinition.
        :rtype: list[int]
        """
        return self._result_ids

    @result_ids.setter
    def result_ids(self, result_ids):
        """
        Sets the result_ids of this CustomSignatureDefinition.
        Associated Results IDs

        :param result_ids: The result_ids of this CustomSignatureDefinition.
        :type: list[int]
        """

        self._result_ids = result_ids

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
        if not isinstance(other, CustomSignatureDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
