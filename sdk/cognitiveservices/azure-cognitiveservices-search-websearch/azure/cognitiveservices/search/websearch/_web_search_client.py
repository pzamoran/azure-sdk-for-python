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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import WebSearchClientConfiguration
from .operations import WebOperations
from . import models


class WebSearchClient(SDKClient):
    """The Web Search API lets you send a search query to Bing and get back search results that include links to webpages, images, and more.

    :ivar config: Configuration for client.
    :vartype config: WebSearchClientConfiguration

    :ivar web: Web operations
    :vartype web: azure.cognitiveservices.search.websearch.operations.WebOperations

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

        self.config = WebSearchClientConfiguration(endpoint, credentials)
        super(WebSearchClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.web = WebOperations(
            self._client, self.config, self._serialize, self._deserialize)
