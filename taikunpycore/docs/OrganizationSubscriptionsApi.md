# taikunpycore.OrganizationSubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizationsubcriptions_list**](OrganizationSubscriptionsApi.md#organizationsubcriptions_list) | **GET** /api/v1/organizationsubcriptions | Retrieve all organization subscriptions
[**organizationsubcriptions_update**](OrganizationSubscriptionsApi.md#organizationsubcriptions_update) | **POST** /api/v1/organizationsubcriptions/update | Update subscription


# **organizationsubcriptions_list**
> List[OrganizationSubscriptionDto] organizationsubcriptions_list()

Retrieve all organization subscriptions

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.organization_subscription_dto import OrganizationSubscriptionDto
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.OrganizationSubscriptionsApi(api_client)

    try:
        # Retrieve all organization subscriptions
        api_response = api_instance.organizationsubcriptions_list()
        print("The response of OrganizationSubscriptionsApi->organizationsubcriptions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationSubscriptionsApi->organizationsubcriptions_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OrganizationSubscriptionDto]**](OrganizationSubscriptionDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizationsubcriptions_update**
> LeaveTaikunDto organizationsubcriptions_update(update_organization_subscription_command)

Update subscription

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.leave_taikun_dto import LeaveTaikunDto
from taikunpycore.models.update_organization_subscription_command import UpdateOrganizationSubscriptionCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.OrganizationSubscriptionsApi(api_client)
    update_organization_subscription_command = taikunpycore.UpdateOrganizationSubscriptionCommand() # UpdateOrganizationSubscriptionCommand | 

    try:
        # Update subscription
        api_response = api_instance.organizationsubcriptions_update(update_organization_subscription_command)
        print("The response of OrganizationSubscriptionsApi->organizationsubcriptions_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationSubscriptionsApi->organizationsubcriptions_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_organization_subscription_command** | [**UpdateOrganizationSubscriptionCommand**](UpdateOrganizationSubscriptionCommand.md)|  | 

### Return type

[**LeaveTaikunDto**](LeaveTaikunDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

