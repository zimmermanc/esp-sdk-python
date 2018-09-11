# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import esp_sdk
from esp_sdk.rest import ApiException
from esp_sdk.apis.external_accounts_api import ExternalAccountsApi


class TestExternalAccountsApi(unittest.TestCase):
    """ ExternalAccountsApi unit test stubs """

    def setUp(self):
        self.api = esp_sdk.apis.external_accounts_api.ExternalAccountsApi()

    def tearDown(self):
        pass

    def test_add_compliance_standard(self):
        """
        Test case for add_compliance_standard

        Add a compliance standard to an external account
        """
        pass

    def test_add_custom_compliance_standard(self):
        """
        Test case for add_custom_compliance_standard

        Add a custom compliance standard to an external account
        """
        pass

    def test_add_disabled_signature(self):
        """
        Test case for add_disabled_signature

        Disable a set of signatures for an external account or a set of external accounts for a signature
        """
        pass

    def test_delete(self):
        """
        Test case for delete

        Delete a(n) External Account
        """
        pass

    def test_list(self):
        """
        Test case for list

        Get a list of External Accounts
        """
        pass

    def test_list_compliance_standards(self):
        """
        Test case for list_compliance_standards

        Get a list of compliance standards for an external account
        """
        pass

    def test_list_custom_compliance_standards(self):
        """
        Test case for list_custom_compliance_standards

        Get a list of custom compliance standards for an external account
        """
        pass

    def test_list_disabled_signatures(self):
        """
        Test case for list_disabled_signatures

        Get a list all the disabled signatures for an external account
        """
        pass

    def test_remove_compliance_standard(self):
        """
        Test case for remove_compliance_standard

        Remove a compliance standard from an external account
        """
        pass

    def test_remove_custom_compliance_standard(self):
        """
        Test case for remove_custom_compliance_standard

        Remove a custom compliance standard from an external account
        """
        pass

    def test_remove_disabled_signature(self):
        """
        Test case for remove_disabled_signature

        Re-enable a set of signatures for an external account or a set of external accounts for a signature
        """
        pass

    def test_show(self):
        """
        Test case for show

        Show a single External Account
        """
        pass


if __name__ == '__main__':
    unittest.main()
