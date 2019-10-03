# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConfigurationSetting(Model):
    """A configuration value.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar etag: Entity tag (etag) of the object
    :vartype etag: str
    :param key:
    :type key: str
    :param label:
    :type label: str
    :param content_type:
    :type content_type: str
    :param value:
    :type value: str
    :ivar last_modified:
    :vartype last_modified: datetime
    :ivar locked:
    :vartype locked: bool
    :param tags:
    :type tags: dict[str, str]
    """

    _validation = {
        'etag': {'readonly': True},
        'last_modified': {'readonly': True},
        'locked': {'readonly': True},
    }

    _attribute_map = {
        'etag': {'key': 'etag', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'content_type': {'key': 'content_type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'last_modified': {'key': 'last_modified', 'type': 'iso-8601'},
        'locked': {'key': 'locked', 'type': 'bool'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, key: str=None, label: str=None, content_type: str=None, value: str=None, tags=None, **kwargs) -> None:
        super(ConfigurationSetting, self).__init__(**kwargs)
        self.etag = None
        self.key = key
        self.label = label
        self.content_type = content_type
        self.value = value
        self.last_modified = None
        self.locked = None
        self.tags = tags


class ConfigurationSettingList(Model):
    """ConfigurationSettingList.

    :param items:
    :type items: list[~appconfiguration.models.ConfigurationSetting]
    """

    _attribute_map = {
        'items': {'key': 'items', 'type': '[ConfigurationSetting]'},
    }

    def __init__(self, *, items=None, **kwargs) -> None:
        super(ConfigurationSettingList, self).__init__(**kwargs)
        self.items = items


class Key(Model):
    """Key.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, name: str, **kwargs) -> None:
        super(Key, self).__init__(**kwargs)
        self.name = name


class KeyList(Model):
    """KeyList.

    :param items:
    :type items: list[~appconfiguration.models.Key]
    """

    _attribute_map = {
        'items': {'key': 'items', 'type': '[Key]'},
    }

    def __init__(self, *, items=None, **kwargs) -> None:
        super(KeyList, self).__init__(**kwargs)
        self.items = items


class Label(Model):
    """Label.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, name: str, **kwargs) -> None:
        super(Label, self).__init__(**kwargs)
        self.name = name


class LabelList(Model):
    """LabelList.

    :param items:
    :type items: list[~appconfiguration.models.Label]
    """

    _attribute_map = {
        'items': {'key': 'items', 'type': '[Label]'},
    }

    def __init__(self, *, items=None, **kwargs) -> None:
        super(LabelList, self).__init__(**kwargs)
        self.items = items