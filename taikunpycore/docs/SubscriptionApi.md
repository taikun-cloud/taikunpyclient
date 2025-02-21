# taikunpycore.SubscriptionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_bind**](SubscriptionApi.md#subscription_bind) | **POST** /api/v1/subscription/bind | Bind subscription
[**subscription_bound_list**](SubscriptionApi.md#subscription_bound_list) | **GET** /api/v1/subscription/boundlist | Retrieve subscription for organization bound
[**subscription_delete**](SubscriptionApi.md#subscription_delete) | **POST** /api/v1/subscription/delete | Delete subscription package
[**subscription_list**](SubscriptionApi.md#subscription_list) | **GET** /api/v1/subscription | Retrieve private subscription list for partners
[**subscription_public**](SubscriptionApi.md#subscription_public) | **GET** /api/v1/subscription/public | Retrieve subscription for organization bound
[**subscription_subscription**](SubscriptionApi.md#subscription_subscription) | **POST** /api/v1/subscription/create | Add new subscription package
[**subscription_update**](SubscriptionApi.md#subscription_update) | **POST** /api/v1/subscription/update | Update subscription


# **subscription_bind**
> BindSubscriptionResponseDto subscription_bind(bind_subscription_command)

Bind subscription

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.bind_subscription_command import BindSubscriptionCommand
from taikunpycore.models.bind_subscription_response_dto import BindSubscriptionResponseDto
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
    api_instance = taikunpycore.SubscriptionApi(api_client)
    bind_subscription_command = taikunpycore.BindSubscriptionCommand() # BindSubscriptionCommand | 

    try:
        # Bind subscription
        api_response = api_instance.subscription_bind(bind_subscription_command)
        print("The response of SubscriptionApi->subscription_bind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscription_bind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bind_subscription_command** | [**BindSubscriptionCommand**](BindSubscriptionCommand.md)|  | 

### Return type

[**BindSubscriptionResponseDto**](BindSubscriptionResponseDto.md)

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

# **subscription_bound_list**
> List[ListForOrganizationEditDto] subscription_bound_list(search=search)

Retrieve subscription for organization bound

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.list_for_organization_edit_dto import ListForOrganizationEditDto
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
    api_instance = taikunpycore.SubscriptionApi(api_client)
    search = 'search_example' # str |  (optional)

    try:
        # Retrieve subscription for organization bound
        api_response = api_instance.subscription_bound_list(search=search)
        print("The response of SubscriptionApi->subscription_bound_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscription_bound_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 

### Return type

[**List[ListForOrganizationEditDto]**](ListForOrganizationEditDto.md)

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

# **subscription_delete**
> subscription_delete(delete_subscription_command)

Delete subscription package

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_subscription_command import DeleteSubscriptionCommand
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
    api_instance = taikunpycore.SubscriptionApi(api_client)
    delete_subscription_command = taikunpycore.DeleteSubscriptionCommand() # DeleteSubscriptionCommand | 

    try:
        # Delete subscription package
        api_instance.subscription_delete(delete_subscription_command)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscription_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_subscription_command** | [**DeleteSubscriptionCommand**](DeleteSubscriptionCommand.md)|  | 

### Return type

void (empty response body)

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

# **subscription_list**
> PrivateSubscriptionList subscription_list(offset=offset, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search)

Retrieve private subscription list for partners

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.private_subscription_list import PrivateSubscriptionList
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
    api_instance = taikunpycore.SubscriptionApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Retrieve private subscription list for partners
        api_response = api_instance.subscription_list(offset=offset, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search)
        print("The response of SubscriptionApi->subscription_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscription_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**PrivateSubscriptionList**](PrivateSubscriptionList.md)

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

# **subscription_public**
> List[ListForLandingPageDto] subscription_public()

Retrieve subscription for organization bound

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.list_for_landing_page_dto import ListForLandingPageDto
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
    api_instance = taikunpycore.SubscriptionApi(api_client)

    try:
        # Retrieve subscription for organization bound
        api_response = api_instance.subscription_public()
        print("The response of SubscriptionApi->subscription_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscription_public: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ListForLandingPageDto]**](ListForLandingPageDto.md)

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

# **subscription_subscription**
> object subscription_subscription(create_subscription_command=create_subscription_command)

Add new subscription package

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.create_subscription_command import CreateSubscriptionCommand
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
    api_instance = taikunpycore.SubscriptionApi(api_client)
    create_subscription_command = taikunpycore.CreateSubscriptionCommand() # CreateSubscriptionCommand |  (optional)

    try:
        # Add new subscription package
        api_response = api_instance.subscription_subscription(create_subscription_command=create_subscription_command)
        print("The response of SubscriptionApi->subscription_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscription_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_subscription_command** | [**CreateSubscriptionCommand**](CreateSubscriptionCommand.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

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

# **subscription_update**
> object subscription_update(update_subscription_command=update_subscription_command)

Update subscription

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_subscription_command import UpdateSubscriptionCommand
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
    api_instance = taikunpycore.SubscriptionApi(api_client)
    update_subscription_command = taikunpycore.UpdateSubscriptionCommand() # UpdateSubscriptionCommand |  (optional)

    try:
        # Update subscription
        api_response = api_instance.subscription_update(update_subscription_command=update_subscription_command)
        print("The response of SubscriptionApi->subscription_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscription_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_subscription_command** | [**UpdateSubscriptionCommand**](UpdateSubscriptionCommand.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

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

