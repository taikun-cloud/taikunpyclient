# taikunpycore.SlackApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slack_create**](SlackApi.md#slack_create) | **POST** /api/v1/slack/create | Create slack configuration
[**slack_delete_multiple**](SlackApi.md#slack_delete_multiple) | **POST** /api/v1/slack/delete-multiple | Delete slack configuration(s)
[**slack_dropdown**](SlackApi.md#slack_dropdown) | **GET** /api/v1/slack/list | Retrieve all slack configs for organization
[**slack_list**](SlackApi.md#slack_list) | **GET** /api/v1/slack | Retrieve all slack configs
[**slack_update**](SlackApi.md#slack_update) | **PUT** /api/v1/slack/update/{id} | Update slack configuration
[**slack_verify**](SlackApi.md#slack_verify) | **POST** /api/v1/slack/verify | Verify slack configuration


# **slack_create**
> ApiResponse slack_create(create_slack_configuration_command)

Create slack configuration

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_slack_configuration_command import CreateSlackConfigurationCommand
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
    api_instance = taikunpycore.SlackApi(api_client)
    create_slack_configuration_command = taikunpycore.CreateSlackConfigurationCommand() # CreateSlackConfigurationCommand | 

    try:
        # Create slack configuration
        api_response = api_instance.slack_create(create_slack_configuration_command)
        print("The response of SlackApi->slack_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlackApi->slack_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_slack_configuration_command** | [**CreateSlackConfigurationCommand**](CreateSlackConfigurationCommand.md)|  | 

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

# **slack_delete_multiple**
> object slack_delete_multiple(delete_slack_config_command)

Delete slack configuration(s)

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_slack_config_command import DeleteSlackConfigCommand
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
    api_instance = taikunpycore.SlackApi(api_client)
    delete_slack_config_command = taikunpycore.DeleteSlackConfigCommand() # DeleteSlackConfigCommand | 

    try:
        # Delete slack configuration(s)
        api_response = api_instance.slack_delete_multiple(delete_slack_config_command)
        print("The response of SlackApi->slack_delete_multiple:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlackApi->slack_delete_multiple: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_slack_config_command** | [**DeleteSlackConfigCommand**](DeleteSlackConfigCommand.md)|  | 

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

# **slack_dropdown**
> List[CommonDropdownDto] slack_dropdown(organization_id=organization_id, search=search)

Retrieve all slack configs for organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_dropdown_dto import CommonDropdownDto
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
    api_instance = taikunpycore.SlackApi(api_client)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Retrieve all slack configs for organization
        api_response = api_instance.slack_dropdown(organization_id=organization_id, search=search)
        print("The response of SlackApi->slack_dropdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlackApi->slack_dropdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**List[CommonDropdownDto]**](CommonDropdownDto.md)

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

# **slack_list**
> SlackConfigurationList slack_list(organization_id=organization_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id)

Retrieve all slack configs

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.slack_configuration_list import SlackConfigurationList
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
    api_instance = taikunpycore.SlackApi(api_client)
    organization_id = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve all slack configs
        api_response = api_instance.slack_list(organization_id=organization_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id)
        print("The response of SlackApi->slack_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlackApi->slack_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 

### Return type

[**SlackConfigurationList**](SlackConfigurationList.md)

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

# **slack_update**
> object slack_update(id, update_slack_configuration_dto=update_slack_configuration_dto)

Update slack configuration

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_slack_configuration_dto import UpdateSlackConfigurationDto
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
    api_instance = taikunpycore.SlackApi(api_client)
    id = 56 # int | 
    update_slack_configuration_dto = taikunpycore.UpdateSlackConfigurationDto() # UpdateSlackConfigurationDto |  (optional)

    try:
        # Update slack configuration
        api_response = api_instance.slack_update(id, update_slack_configuration_dto=update_slack_configuration_dto)
        print("The response of SlackApi->slack_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlackApi->slack_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_slack_configuration_dto** | [**UpdateSlackConfigurationDto**](UpdateSlackConfigurationDto.md)|  | [optional] 

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

# **slack_verify**
> object slack_verify(verify_slack_credentials_command)

Verify slack configuration

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.verify_slack_credentials_command import VerifySlackCredentialsCommand
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
    api_instance = taikunpycore.SlackApi(api_client)
    verify_slack_credentials_command = taikunpycore.VerifySlackCredentialsCommand() # VerifySlackCredentialsCommand | 

    try:
        # Verify slack configuration
        api_response = api_instance.slack_verify(verify_slack_credentials_command)
        print("The response of SlackApi->slack_verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlackApi->slack_verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_slack_credentials_command** | [**VerifySlackCredentialsCommand**](VerifySlackCredentialsCommand.md)|  | 

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

