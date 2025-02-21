# taikunpycore.ServersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servers_console**](ServersApi.md#servers_console) | **POST** /api/v1/servers/console | Console screenshot or terminal access for server
[**servers_create**](ServersApi.md#servers_create) | **POST** /api/v1/servers/create | Create a new server in the given project.
[**servers_details**](ServersApi.md#servers_details) | **GET** /api/v1/servers/{projectId} | Retrieve all servers by given project
[**servers_list**](ServersApi.md#servers_list) | **GET** /api/v1/servers | Retrieve all servers
[**servers_reboot**](ServersApi.md#servers_reboot) | **POST** /api/v1/servers/reboot | Reboot server
[**servers_reset**](ServersApi.md#servers_reset) | **POST** /api/v1/servers/reset | Update server(s) status(es)
[**servers_status**](ServersApi.md#servers_status) | **GET** /api/v1/servers/status/{serverId} | Show server status
[**servers_update_by_project_id**](ServersApi.md#servers_update_by_project_id) | **PUT** /api/v1/servers/update/{projectId} | Update server by projectId


# **servers_console**
> str servers_console(console_screenshot_command)

Console screenshot or terminal access for server

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.console_screenshot_command import ConsoleScreenshotCommand
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
    api_instance = taikunpycore.ServersApi(api_client)
    console_screenshot_command = taikunpycore.ConsoleScreenshotCommand() # ConsoleScreenshotCommand | 

    try:
        # Console screenshot or terminal access for server
        api_response = api_instance.servers_console(console_screenshot_command)
        print("The response of ServersApi->servers_console:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_console: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **console_screenshot_command** | [**ConsoleScreenshotCommand**](ConsoleScreenshotCommand.md)|  | 

### Return type

**str**

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

# **servers_create**
> ApiResponse servers_create(server_for_create_dto=server_for_create_dto)

Create a new server in the given project.

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.server_for_create_dto import ServerForCreateDto
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
    api_instance = taikunpycore.ServersApi(api_client)
    server_for_create_dto = taikunpycore.ServerForCreateDto() # ServerForCreateDto |  (optional)

    try:
        # Create a new server in the given project.
        api_response = api_instance.servers_create(server_for_create_dto=server_for_create_dto)
        print("The response of ServersApi->servers_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_for_create_dto** | [**ServerForCreateDto**](ServerForCreateDto.md)|  | [optional] 

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

# **servers_details**
> ServersListForDetails servers_details(project_id, sort_by=sort_by, sort_direction=sort_direction, with_autoscaling_group=with_autoscaling_group)

Retrieve all servers by given project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.servers_list_for_details import ServersListForDetails
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
    api_instance = taikunpycore.ServersApi(api_client)
    project_id = 56 # int | 
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    with_autoscaling_group = 'with_autoscaling_group_example' # str |  (optional)

    try:
        # Retrieve all servers by given project
        api_response = api_instance.servers_details(project_id, sort_by=sort_by, sort_direction=sort_direction, with_autoscaling_group=with_autoscaling_group)
        print("The response of ServersApi->servers_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **with_autoscaling_group** | **str**|  | [optional] 

### Return type

[**ServersListForDetails**](ServersListForDetails.md)

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

# **servers_list**
> ServersList servers_list(limit=limit, offset=offset, project_id=project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, start_ram=start_ram, end_ram=end_ram, start_disk_size=start_disk_size, end_disk_size=end_disk_size, start_cpu=start_cpu, end_cpu=end_cpu, organization_id=organization_id, id=id, filter_by=filter_by, autoscaling_group=autoscaling_group)

Retrieve all servers

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.servers_list import ServersList
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
    api_instance = taikunpycore.ServersApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    project_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_disk_size = 56 # int |  (optional)
    end_disk_size = 56 # int |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    id = 56 # int |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)
    autoscaling_group = 'autoscaling_group_example' # str |  (optional)

    try:
        # Retrieve all servers
        api_response = api_instance.servers_list(limit=limit, offset=offset, project_id=project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, start_ram=start_ram, end_ram=end_ram, start_disk_size=start_disk_size, end_disk_size=end_disk_size, start_cpu=start_cpu, end_cpu=end_cpu, organization_id=organization_id, id=id, filter_by=filter_by, autoscaling_group=autoscaling_group)
        print("The response of ServersApi->servers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **project_id** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **start_ram** | **float**|  | [optional] 
 **end_ram** | **float**|  | [optional] 
 **start_disk_size** | **int**|  | [optional] 
 **end_disk_size** | **int**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **id** | **int**|  | [optional] 
 **filter_by** | **str**|  | [optional] 
 **autoscaling_group** | **str**|  | [optional] 

### Return type

[**ServersList**](ServersList.md)

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

# **servers_reboot**
> object servers_reboot(reboot_server_command)

Reboot server

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.reboot_server_command import RebootServerCommand
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
    api_instance = taikunpycore.ServersApi(api_client)
    reboot_server_command = taikunpycore.RebootServerCommand() # RebootServerCommand | 

    try:
        # Reboot server
        api_response = api_instance.servers_reboot(reboot_server_command)
        print("The response of ServersApi->servers_reboot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_reboot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reboot_server_command** | [**RebootServerCommand**](RebootServerCommand.md)|  | 

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

# **servers_reset**
> object servers_reset(reset_server_status_command=reset_server_status_command)

Update server(s) status(es)

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.reset_server_status_command import ResetServerStatusCommand
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
    api_instance = taikunpycore.ServersApi(api_client)
    reset_server_status_command = taikunpycore.ResetServerStatusCommand() # ResetServerStatusCommand |  (optional)

    try:
        # Update server(s) status(es)
        api_response = api_instance.servers_reset(reset_server_status_command=reset_server_status_command)
        print("The response of ServersApi->servers_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_reset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_server_status_command** | [**ResetServerStatusCommand**](ResetServerStatusCommand.md)|  | [optional] 

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

# **servers_status**
> str servers_status(server_id)

Show server status

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
    api_instance = taikunpycore.ServersApi(api_client)
    server_id = 56 # int | 

    try:
        # Show server status
        api_response = api_instance.servers_status(server_id)
        print("The response of ServersApi->servers_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **servers_update_by_project_id**
> object servers_update_by_project_id(project_id, update_server_health_dto=update_server_health_dto)

Update server by projectId

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_server_health_dto import UpdateServerHealthDto
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
    api_instance = taikunpycore.ServersApi(api_client)
    project_id = 56 # int | 
    update_server_health_dto = [taikunpycore.UpdateServerHealthDto()] # List[UpdateServerHealthDto] |  (optional)

    try:
        # Update server by projectId
        api_response = api_instance.servers_update_by_project_id(project_id, update_server_health_dto=update_server_health_dto)
        print("The response of ServersApi->servers_update_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_update_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **update_server_health_dto** | [**List[UpdateServerHealthDto]**](UpdateServerHealthDto.md)|  | [optional] 

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

