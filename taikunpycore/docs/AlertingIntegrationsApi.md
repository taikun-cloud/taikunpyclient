# taikunpycore.AlertingIntegrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertingintegrations_create**](AlertingIntegrationsApi.md#alertingintegrations_create) | **POST** /api/v1/alertingintegrations/create | Create alerting profile alerting integration
[**alertingintegrations_delete**](AlertingIntegrationsApi.md#alertingintegrations_delete) | **DELETE** /api/v1/alertingintegrations/{id} | Delete alerting profile alerting integration
[**alertingintegrations_edit**](AlertingIntegrationsApi.md#alertingintegrations_edit) | **PUT** /api/v1/alertingintegrations/edit | Edit alerting profile alerting integration
[**alertingintegrations_list**](AlertingIntegrationsApi.md#alertingintegrations_list) | **GET** /api/v1/alertingintegrations/{alertingProfileId} | List alerting integrations by profile id
[**documentation_list**](AlertingIntegrationsApi.md#documentation_list) | **GET** /api/v1/documentation | Retrieve all documentation links


# **alertingintegrations_create**
> ApiResponse alertingintegrations_create(create_alerting_integration_command=create_alerting_integration_command)

Create alerting profile alerting integration

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_alerting_integration_command import CreateAlertingIntegrationCommand
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
    api_instance = taikunpycore.AlertingIntegrationsApi(api_client)
    create_alerting_integration_command = {"url":"https://www.google.com","token":"Only if no microsoft teams type","alertingIntegrationType":"Opsgenie","alertingProfileId":1} # CreateAlertingIntegrationCommand |  (optional)

    try:
        # Create alerting profile alerting integration
        api_response = api_instance.alertingintegrations_create(create_alerting_integration_command=create_alerting_integration_command)
        print("The response of AlertingIntegrationsApi->alertingintegrations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingIntegrationsApi->alertingintegrations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_alerting_integration_command** | [**CreateAlertingIntegrationCommand**](CreateAlertingIntegrationCommand.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **alertingintegrations_delete**
> alertingintegrations_delete(id)

Delete alerting profile alerting integration

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
    api_instance = taikunpycore.AlertingIntegrationsApi(api_client)
    id = 56 # int | 

    try:
        # Delete alerting profile alerting integration
        api_instance.alertingintegrations_delete(id)
    except Exception as e:
        print("Exception when calling AlertingIntegrationsApi->alertingintegrations_delete: %s\n" % e)
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

# **alertingintegrations_edit**
> object alertingintegrations_edit(edit_alerting_integration_command=edit_alerting_integration_command)

Edit alerting profile alerting integration

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.edit_alerting_integration_command import EditAlertingIntegrationCommand
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
    api_instance = taikunpycore.AlertingIntegrationsApi(api_client)
    edit_alerting_integration_command = {"id":1,"url":"https://www.google.com","token":"Only if no microsoft teams type","alertingIntegrationType":"Opsgenie","alertingProfileId":1} # EditAlertingIntegrationCommand |  (optional)

    try:
        # Edit alerting profile alerting integration
        api_response = api_instance.alertingintegrations_edit(edit_alerting_integration_command=edit_alerting_integration_command)
        print("The response of AlertingIntegrationsApi->alertingintegrations_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingIntegrationsApi->alertingintegrations_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_alerting_integration_command** | [**EditAlertingIntegrationCommand**](EditAlertingIntegrationCommand.md)|  | [optional] 

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

# **alertingintegrations_list**
> List[AlertingIntegrationsListDto] alertingintegrations_list(alerting_profile_id, search=search)

List alerting integrations by profile id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.alerting_integrations_list_dto import AlertingIntegrationsListDto
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
    api_instance = taikunpycore.AlertingIntegrationsApi(api_client)
    alerting_profile_id = 56 # int | 
    search = 'search_example' # str |  (optional)

    try:
        # List alerting integrations by profile id
        api_response = api_instance.alertingintegrations_list(alerting_profile_id, search=search)
        print("The response of AlertingIntegrationsApi->alertingintegrations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingIntegrationsApi->alertingintegrations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alerting_profile_id** | **int**|  | 
 **search** | **str**|  | [optional] 

### Return type

[**List[AlertingIntegrationsListDto]**](AlertingIntegrationsListDto.md)

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

# **documentation_list**
> DocumentationsList documentation_list(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, key=key)

Retrieve all documentation links

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.documentations_list import DocumentationsList
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
    api_instance = taikunpycore.AlertingIntegrationsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    key = 'key_example' # str |  (optional)

    try:
        # Retrieve all documentation links
        api_response = api_instance.documentation_list(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, key=key)
        print("The response of AlertingIntegrationsApi->documentation_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingIntegrationsApi->documentation_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **key** | **str**|  | [optional] 

### Return type

[**DocumentationsList**](DocumentationsList.md)

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

