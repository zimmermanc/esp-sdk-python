# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UserAttributionsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add_channel(self, external_account_id, **kwargs):
        """
        Create a User Attribution Channel for an external account
        URL will only be returned in this response and will not be accessible again.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_channel(external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int external_account_id: The ID of the external account to create a User Attribution Channel for (required)
        :return: ExternalAccountUserAttributionChannel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_channel_with_http_info(external_account_id, **kwargs)
        else:
            (data) = self.add_channel_with_http_info(external_account_id, **kwargs)
            return data

    def add_channel_with_http_info(self, external_account_id, **kwargs):
        """
        Create a User Attribution Channel for an external account
        URL will only be returned in this response and will not be accessible again.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_channel_with_http_info(external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int external_account_id: The ID of the external account to create a User Attribution Channel for (required)
        :return: ExternalAccountUserAttributionChannel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['external_account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_channel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'external_account_id' is set
        if ('external_account_id' not in params) or (params['external_account_id'] is None):
            raise ValueError("Missing the required parameter `external_account_id` when calling `add_channel`")


        collection_formats = {}

        resource_path = '/api/v2/external_accounts/{external_account_id}/user_attribution/channel.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'external_account_id' in params:
            path_params['external_account_id'] = params['external_account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ExternalAccountUserAttributionChannel',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def remove_channel(self, external_account_id, **kwargs):
        """
        Remove the User Attribution Channel for an external account
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_channel(external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int external_account_id: The ID of the external account to remove the User Attribution Channel from (required)
        :return: Meta
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.remove_channel_with_http_info(external_account_id, **kwargs)
        else:
            (data) = self.remove_channel_with_http_info(external_account_id, **kwargs)
            return data

    def remove_channel_with_http_info(self, external_account_id, **kwargs):
        """
        Remove the User Attribution Channel for an external account
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_channel_with_http_info(external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int external_account_id: The ID of the external account to remove the User Attribution Channel from (required)
        :return: Meta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['external_account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_channel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'external_account_id' is set
        if ('external_account_id' not in params) or (params['external_account_id'] is None):
            raise ValueError("Missing the required parameter `external_account_id` when calling `remove_channel`")


        collection_formats = {}

        resource_path = '/api/v2/external_accounts/{external_account_id}/user_attribution/channel.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'external_account_id' in params:
            path_params['external_account_id'] = params['external_account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Meta',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def show_channel(self, external_account_id, **kwargs):
        """
        Show the User Attribution Channel of an external account
        The channel url will not be returned.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show_channel(external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int external_account_id: The ID of the external account to show the user attribution channel for (required)
        :return: ExternalAccountUserAttributionChannel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.show_channel_with_http_info(external_account_id, **kwargs)
        else:
            (data) = self.show_channel_with_http_info(external_account_id, **kwargs)
            return data

    def show_channel_with_http_info(self, external_account_id, **kwargs):
        """
        Show the User Attribution Channel of an external account
        The channel url will not be returned.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show_channel_with_http_info(external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int external_account_id: The ID of the external account to show the user attribution channel for (required)
        :return: ExternalAccountUserAttributionChannel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['external_account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show_channel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'external_account_id' is set
        if ('external_account_id' not in params) or (params['external_account_id'] is None):
            raise ValueError("Missing the required parameter `external_account_id` when calling `show_channel`")


        collection_formats = {}

        resource_path = '/api/v2/external_accounts/{external_account_id}/user_attribution/channel.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'external_account_id' in params:
            path_params['external_account_id'] = params['external_account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ExternalAccountUserAttributionChannel',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update(self, external_account_id, **kwargs):
        """
        Update the user attributions on an external account
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update(external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int external_account_id: The ID of the external account to update the user attributions of (required)
        :param str include: Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, suppressions, azure_group See Including Objects for more information.
        :param str cloudtrail_name: The name of the cloudetrail associated with the user attribution.
        :return: ExternalAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(external_account_id, **kwargs)
        else:
            (data) = self.update_with_http_info(external_account_id, **kwargs)
            return data

    def update_with_http_info(self, external_account_id, **kwargs):
        """
        Update the user attributions on an external account
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_with_http_info(external_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int external_account_id: The ID of the external account to update the user attributions of (required)
        :param str include: Related objects that can be included in the response:  organization, sub_organization, team, scan_intervals, disabled_signatures, suppressions, azure_group See Including Objects for more information.
        :param str cloudtrail_name: The name of the cloudetrail associated with the user attribution.
        :return: ExternalAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['external_account_id', 'include', 'cloudtrail_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'external_account_id' is set
        if ('external_account_id' not in params) or (params['external_account_id'] is None):
            raise ValueError("Missing the required parameter `external_account_id` when calling `update`")


        collection_formats = {}

        resource_path = '/api/v2/external_accounts/{external_account_id}/user_attribution.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'external_account_id' in params:
            path_params['external_account_id'] = params['external_account_id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'cloudtrail_name' in params:
            form_params.append(('cloudtrail_name', params['cloudtrail_name']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ExternalAccount',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
