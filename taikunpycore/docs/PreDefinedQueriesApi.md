# taikunpycore.PreDefinedQueriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**predefinedqueries_create**](PreDefinedQueriesApi.md#predefinedqueries_create) | **POST** /api/v1/predefinedqueries/prometheus/dashboard/create | Create prometheus dashboard pre defined query
[**predefinedqueries_delete**](PreDefinedQueriesApi.md#predefinedqueries_delete) | **DELETE** /api/v1/predefinedqueries/prometheus/dashboard/delete/{id} | Delete prometheus dashboard pre defined query
[**predefinedqueries_list**](PreDefinedQueriesApi.md#predefinedqueries_list) | **GET** /api/v1/predefinedqueries/prometheus/dashboard/list/{projectId} | Get list of pre defined organization prometheus dashboard elements
[**predefinedqueries_prometheus_dashboard_common**](PreDefinedQueriesApi.md#predefinedqueries_prometheus_dashboard_common) | **GET** /api/v1/predefinedqueries/prometheus/dashboard/common/{projectId} | et list of pre defined common prometheus dashboard elements
[**predefinedqueries_update**](PreDefinedQueriesApi.md#predefinedqueries_update) | **POST** /api/v1/predefinedqueries/prometheus/dashboard/update | Update prometheus dashboard pre defined query


# **predefinedqueries_create**
> object predefinedqueries_create(prometheus_dashboard_create_command)

Create prometheus dashboard pre defined query

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.prometheus_dashboard_create_command import PrometheusDashboardCreateCommand
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
    api_instance = taikunpycore.PreDefinedQueriesApi(api_client)
    prometheus_dashboard_create_command = taikunpycore.PrometheusDashboardCreateCommand() # PrometheusDashboardCreateCommand | 

    try:
        # Create prometheus dashboard pre defined query
        api_response = api_instance.predefinedqueries_create(prometheus_dashboard_create_command)
        print("The response of PreDefinedQueriesApi->predefinedqueries_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreDefinedQueriesApi->predefinedqueries_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prometheus_dashboard_create_command** | [**PrometheusDashboardCreateCommand**](PrometheusDashboardCreateCommand.md)|  | 

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

# **predefinedqueries_delete**
> predefinedqueries_delete(id)

Delete prometheus dashboard pre defined query

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
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
    api_instance = taikunpycore.PreDefinedQueriesApi(api_client)
    id = 56 # int | 

    try:
        # Delete prometheus dashboard pre defined query
        api_instance.predefinedqueries_delete(id)
    except Exception as e:
        print("Exception when calling PreDefinedQueriesApi->predefinedqueries_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

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

# **predefinedqueries_list**
> List[PrometheusDashboardListDto] predefinedqueries_list(project_id)

Get list of pre defined organization prometheus dashboard elements

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.prometheus_dashboard_list_dto import PrometheusDashboardListDto
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
    api_instance = taikunpycore.PreDefinedQueriesApi(api_client)
    project_id = 56 # int | 

    try:
        # Get list of pre defined organization prometheus dashboard elements
        api_response = api_instance.predefinedqueries_list(project_id)
        print("The response of PreDefinedQueriesApi->predefinedqueries_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreDefinedQueriesApi->predefinedqueries_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**List[PrometheusDashboardListDto]**](PrometheusDashboardListDto.md)

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

# **predefinedqueries_prometheus_dashboard_common**
> List[PrometheusDashboardListDto] predefinedqueries_prometheus_dashboard_common(project_id)

et list of pre defined common prometheus dashboard elements

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.prometheus_dashboard_list_dto import PrometheusDashboardListDto
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
    api_instance = taikunpycore.PreDefinedQueriesApi(api_client)
    project_id = 56 # int | 

    try:
        # et list of pre defined common prometheus dashboard elements
        api_response = api_instance.predefinedqueries_prometheus_dashboard_common(project_id)
        print("The response of PreDefinedQueriesApi->predefinedqueries_prometheus_dashboard_common:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreDefinedQueriesApi->predefinedqueries_prometheus_dashboard_common: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**List[PrometheusDashboardListDto]**](PrometheusDashboardListDto.md)

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

# **predefinedqueries_update**
> object predefinedqueries_update(prometheus_dashboard_update_command)

Update prometheus dashboard pre defined query

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.prometheus_dashboard_update_command import PrometheusDashboardUpdateCommand
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
    api_instance = taikunpycore.PreDefinedQueriesApi(api_client)
    prometheus_dashboard_update_command = taikunpycore.PrometheusDashboardUpdateCommand() # PrometheusDashboardUpdateCommand | 

    try:
        # Update prometheus dashboard pre defined query
        api_response = api_instance.predefinedqueries_update(prometheus_dashboard_update_command)
        print("The response of PreDefinedQueriesApi->predefinedqueries_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreDefinedQueriesApi->predefinedqueries_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prometheus_dashboard_update_command** | [**PrometheusDashboardUpdateCommand**](PrometheusDashboardUpdateCommand.md)|  | 

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

