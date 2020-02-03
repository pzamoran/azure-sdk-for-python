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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class AdPrincipal(Model):
    """Active Directory Principal who’ll get owner access on the new subscription.

    All required parameters must be populated in order to send to Azure.

    :param object_id: Required. Object id of the Principal
    :type object_id: str
    """

    _validation = {
        'object_id': {'required': True},
    }

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdPrincipal, self).__init__(**kwargs)
        self.object_id = kwargs.get('object_id', None)


class CanceledSubscriptionId(Model):
    """The ID of the canceled subscription.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The ID of the canceled subscription
    :vartype value: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CanceledSubscriptionId, self).__init__(**kwargs)
        self.value = None


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class EnabledSubscriptionId(Model):
    """The ID of the subscriptions that is being enabled.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The ID of the subscriptions that is being enabled
    :vartype value: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EnabledSubscriptionId, self).__init__(**kwargs)
        self.value = None


class ErrorResponse(Model):
    """Describes the format of Error response.

    :param code: Error code
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class Location(Model):
    """Location information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified ID of the location. For example,
     /subscriptions/00000000-0000-0000-0000-000000000000/locations/westus.
    :vartype id: str
    :ivar subscription_id: The subscription ID.
    :vartype subscription_id: str
    :ivar name: The location name.
    :vartype name: str
    :ivar display_name: The display name of the location.
    :vartype display_name: str
    :ivar latitude: The latitude of the location.
    :vartype latitude: str
    :ivar longitude: The longitude of the location.
    :vartype longitude: str
    """

    _validation = {
        'id': {'readonly': True},
        'subscription_id': {'readonly': True},
        'name': {'readonly': True},
        'display_name': {'readonly': True},
        'latitude': {'readonly': True},
        'longitude': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'latitude': {'key': 'latitude', 'type': 'str'},
        'longitude': {'key': 'longitude', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Location, self).__init__(**kwargs)
        self.id = None
        self.subscription_id = None
        self.name = None
        self.display_name = None
        self.latitude = None
        self.longitude = None


class ModernCspSubscriptionCreationParameters(Model):
    """The parameters required to create a new CSP subscription.

    All required parameters must be populated in order to send to Azure.

    :param display_name: Required. The friendly name of the subscription.
    :type display_name: str
    :param sku_id: Required. The SKU ID of the Azure plan. Azure plan
     determines the pricing and service-level agreement of the subscription.
     Use 001 for Microsoft Azure Plan and 002 for Microsoft Azure Plan for
     DevTest.
    :type sku_id: str
    :param reseller_id: Reseller ID, basically MPN Id.
    :type reseller_id: str
    :param service_provider_id: Service provider ID, basically MPN Id.
    :type service_provider_id: str
    """

    _validation = {
        'display_name': {'required': True},
        'sku_id': {'required': True},
    }

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'sku_id': {'key': 'skuId', 'type': 'str'},
        'reseller_id': {'key': 'resellerId', 'type': 'str'},
        'service_provider_id': {'key': 'serviceProviderId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ModernCspSubscriptionCreationParameters, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.sku_id = kwargs.get('sku_id', None)
        self.reseller_id = kwargs.get('reseller_id', None)
        self.service_provider_id = kwargs.get('service_provider_id', None)


class ModernSubscriptionCreationParameters(Model):
    """The parameters required to create a new subscription.

    All required parameters must be populated in order to send to Azure.

    :param display_name: Required. The friendly name of the subscription.
    :type display_name: str
    :param billing_profile_id: Required. The ARM ID of the billing profile for
     which you want to create the subscription.
    :type billing_profile_id: str
    :param sku_id: Required. The SKU ID of the Azure plan. Azure plan
     determines the pricing and service-level agreement of the subscription.
     Use 001 for Microsoft Azure Plan and 002 for Microsoft Azure Plan for
     DevTest.
    :type sku_id: str
    :param cost_center: If set, the cost center will show up on the Azure
     usage and charges file.
    :type cost_center: str
    :param owner: If specified, the AD principal will get owner access to the
     subscription, along with the user who is performing the create
     subscription operation
    :type owner: ~azure.mgmt.subscription.models.AdPrincipal
    :param management_group_id: The identifier of the management group to
     which this subscription will be associated.
    :type management_group_id: str
    :param additional_parameters: Additional, untyped parameters to support
     custom subscription creation scenarios.
    :type additional_parameters: dict[str, object]
    """

    _validation = {
        'display_name': {'required': True},
        'billing_profile_id': {'required': True},
        'sku_id': {'required': True},
    }

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'billing_profile_id': {'key': 'billingProfileId', 'type': 'str'},
        'sku_id': {'key': 'skuId', 'type': 'str'},
        'cost_center': {'key': 'costCenter', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'AdPrincipal'},
        'management_group_id': {'key': 'managementGroupId', 'type': 'str'},
        'additional_parameters': {'key': 'additionalParameters', 'type': '{object}'},
    }

    def __init__(self, **kwargs):
        super(ModernSubscriptionCreationParameters, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.billing_profile_id = kwargs.get('billing_profile_id', None)
        self.sku_id = kwargs.get('sku_id', None)
        self.cost_center = kwargs.get('cost_center', None)
        self.owner = kwargs.get('owner', None)
        self.management_group_id = kwargs.get('management_group_id', None)
        self.additional_parameters = kwargs.get('additional_parameters', None)


class Operation(Model):
    """REST API operation.

    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.subscription.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)


class OperationDisplay(Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.Subscription
    :type provider: str
    :param resource: Resource on which the operation is performed: Profile,
     endpoint, etc.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)


class OperationListResult(Model):
    """Result of the request to list operations. It contains a list of operations
    and a URL link to get the next set of results.

    :param value: List of operations.
    :type value: list[~azure.mgmt.subscription.models.Operation]
    :param next_link: URL to get the next set of operation list results if
     there are any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class RenamedSubscriptionId(Model):
    """The ID of the subscriptions that is being renamed.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The ID of the subscriptions that is being renamed
    :vartype value: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RenamedSubscriptionId, self).__init__(**kwargs)
        self.value = None


class Subscription(Model):
    """Subscription information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified ID for the subscription. For example,
     /subscriptions/00000000-0000-0000-0000-000000000000.
    :vartype id: str
    :ivar subscription_id: The subscription ID.
    :vartype subscription_id: str
    :ivar display_name: The subscription display name.
    :vartype display_name: str
    :ivar state: The subscription state. Possible values are Enabled, Warned,
     PastDue, Disabled, and Deleted. Possible values include: 'Enabled',
     'Warned', 'PastDue', 'Disabled', 'Deleted'
    :vartype state: str or ~azure.mgmt.subscription.models.SubscriptionState
    :param subscription_policies: The subscription policies.
    :type subscription_policies:
     ~azure.mgmt.subscription.models.SubscriptionPolicies
    :param authorization_source: The authorization source of the request.
     Valid values are one or more combinations of Legacy, RoleBased, Bypassed,
     Direct and Management. For example, 'Legacy, RoleBased'.
    :type authorization_source: str
    """

    _validation = {
        'id': {'readonly': True},
        'subscription_id': {'readonly': True},
        'display_name': {'readonly': True},
        'state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'state': {'key': 'state', 'type': 'SubscriptionState'},
        'subscription_policies': {'key': 'subscriptionPolicies', 'type': 'SubscriptionPolicies'},
        'authorization_source': {'key': 'authorizationSource', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Subscription, self).__init__(**kwargs)
        self.id = None
        self.subscription_id = None
        self.display_name = None
        self.state = None
        self.subscription_policies = kwargs.get('subscription_policies', None)
        self.authorization_source = kwargs.get('authorization_source', None)


class SubscriptionCreationParameters(Model):
    """Subscription Creation Parameters required to create a new Azure
    subscription.

    :param display_name: The display name of the subscription.
    :type display_name: str
    :param owners: The list of principals that should be granted Owner access
     on the subscription. Principals should be of type User, Service Principal
     or Security Group.
    :type owners: list[~azure.mgmt.subscription.models.AdPrincipal]
    :param offer_type: The offer type of the subscription. For example,
     MS-AZR-0017P (EnterpriseAgreement) and MS-AZR-0148P (EnterpriseAgreement
     devTest) are available. Only valid when creating a subscription in a
     enrollment account scope. Possible values include: 'MS-AZR-0017P',
     'MS-AZR-0148P'
    :type offer_type: str or ~azure.mgmt.subscription.models.OfferType
    :param additional_parameters: Additional, untyped parameters to support
     custom subscription creation scenarios.
    :type additional_parameters: dict[str, object]
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'owners': {'key': 'owners', 'type': '[AdPrincipal]'},
        'offer_type': {'key': 'offerType', 'type': 'str'},
        'additional_parameters': {'key': 'additionalParameters', 'type': '{object}'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionCreationParameters, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.owners = kwargs.get('owners', None)
        self.offer_type = kwargs.get('offer_type', None)
        self.additional_parameters = kwargs.get('additional_parameters', None)


class SubscriptionCreationResult(Model):
    """The created subscription object.

    :param subscription_link: The link to the new subscription. Use this link
     to check the status of subscription creation operation.
    :type subscription_link: str
    """

    _attribute_map = {
        'subscription_link': {'key': 'subscriptionLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionCreationResult, self).__init__(**kwargs)
        self.subscription_link = kwargs.get('subscription_link', None)


class SubscriptionName(Model):
    """The new name of the subscription.

    :param subscription_name: New subscription name
    :type subscription_name: str
    """

    _attribute_map = {
        'subscription_name': {'key': 'subscriptionName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionName, self).__init__(**kwargs)
        self.subscription_name = kwargs.get('subscription_name', None)


class SubscriptionOperation(Model):
    """status of the subscription POST operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The operation Id.
    :vartype id: str
    :param status: Status of the pending subscription
    :type status: str
    :param status_detail: Status Detail of the pending subscription
    :type status_detail: str
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'status_detail': {'key': 'statusDetail', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionOperation, self).__init__(**kwargs)
        self.id = None
        self.status = kwargs.get('status', None)
        self.status_detail = kwargs.get('status_detail', None)


class SubscriptionOperationListResult(Model):
    """A list of pending subscription operations.

    :param value: A list of pending SubscriptionOperations
    :type value: list[~azure.mgmt.subscription.models.SubscriptionOperation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[SubscriptionOperation]'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionOperationListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class SubscriptionPolicies(Model):
    """Subscription policies.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar location_placement_id: The subscription location placement ID. The
     ID indicates which regions are visible for a subscription. For example, a
     subscription with a location placement Id of Public_2014-09-01 has access
     to Azure public regions.
    :vartype location_placement_id: str
    :ivar quota_id: The subscription quota ID.
    :vartype quota_id: str
    :ivar spending_limit: The subscription spending limit. Possible values
     include: 'On', 'Off', 'CurrentPeriodOff'
    :vartype spending_limit: str or
     ~azure.mgmt.subscription.models.SpendingLimit
    """

    _validation = {
        'location_placement_id': {'readonly': True},
        'quota_id': {'readonly': True},
        'spending_limit': {'readonly': True},
    }

    _attribute_map = {
        'location_placement_id': {'key': 'locationPlacementId', 'type': 'str'},
        'quota_id': {'key': 'quotaId', 'type': 'str'},
        'spending_limit': {'key': 'spendingLimit', 'type': 'SpendingLimit'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionPolicies, self).__init__(**kwargs)
        self.location_placement_id = None
        self.quota_id = None
        self.spending_limit = None


class TenantIdDescription(Model):
    """Tenant Id information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified ID of the tenant. For example,
     /tenants/00000000-0000-0000-0000-000000000000.
    :vartype id: str
    :ivar tenant_id: The tenant ID. For example,
     00000000-0000-0000-0000-000000000000.
    :vartype tenant_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TenantIdDescription, self).__init__(**kwargs)
        self.id = None
        self.tenant_id = None
