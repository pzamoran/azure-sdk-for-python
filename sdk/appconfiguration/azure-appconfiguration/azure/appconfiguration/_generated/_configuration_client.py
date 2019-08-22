# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core import PipelineClient
from msrest import Serializer, Deserializer

from ._configuration import ConfigurationClientConfiguration
from .operations import ConfigurationClientOperationsMixin
from . import models


class ConfigurationClient(ConfigurationClientOperationsMixin):
    """Represents an Azure App Configuration Client


    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None, **kwargs):

        if not base_url:
            base_url = 'http://localhost'
        self._config = ConfigurationClientConfiguration(credentials, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '0.1'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)