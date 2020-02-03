# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest import Configuration

from .version import VERSION


class WebSearchClientConfiguration(Configuration):
    """Configuration for WebSearchClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Supported Cognitive Services endpoints (protocol and
     hostname, for example: "https://westus.api.cognitive.microsoft.com",
     "https://api.cognitive.microsoft.com").
    :type endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, endpoint, credentials):

        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        base_url = '{Endpoint}/bing/v7.0'

        super(WebSearchClientConfiguration, self).__init__(base_url)

        # Starting Autorest.Python 4.0.64, make connection pool activated by default
        self.keep_alive = True

        self.add_user_agent('azure-cognitiveservices-search-websearch/{}'.format(VERSION))

        self.endpoint = endpoint
        self.credentials = credentials
