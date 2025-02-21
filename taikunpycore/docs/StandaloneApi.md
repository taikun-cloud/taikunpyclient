# taikunpycore.StandaloneApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**standalone_create**](StandaloneApi.md#standalone_create) | **POST** /api/v1/standalone/create | Create a new vm in the given project.
[**standalone_details**](StandaloneApi.md#standalone_details) | **GET** /api/v1/standalone/{projectId} | Retrieve a list of standalone vm with detailed info
[**standalone_ip_management**](StandaloneApi.md#standalone_ip_management) | **POST** /api/v1/standalone/ip/management | Enable/Disable stand alone public ip
[**standalone_list**](StandaloneApi.md#standalone_list) | **GET** /api/v1/standalone | Retrieve all vms
[**standalone_reset**](StandaloneApi.md#standalone_reset) | **POST** /api/v1/standalone/reset | Reset vm status
[**standalone_update_flavor**](StandaloneApi.md#standalone_update_flavor) | **POST** /api/v1/standalone/update/flavor | Update standalone vm flavor


# **standalone_create**
> ApiResponse standalone_create(create_stand_alone_vm_command=create_stand_alone_vm_command)

Create a new vm in the given project.

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_stand_alone_vm_command import CreateStandAloneVmCommand
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
    api_instance = taikunpycore.StandaloneApi(api_client)
    create_stand_alone_vm_command = taikunpycore.CreateStandAloneVmCommand() # CreateStandAloneVmCommand |  (optional)

    try:
        # Create a new vm in the given project.
        api_response = api_instance.standalone_create(create_stand_alone_vm_command=create_stand_alone_vm_command)
        print("The response of StandaloneApi->standalone_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneApi->standalone_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_stand_alone_vm_command** | [**CreateStandAloneVmCommand**](CreateStandAloneVmCommand.md)|  | [optional] 

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

# **standalone_details**
> StandAloneVmListForDetails standalone_details(project_id, sort_by=sort_by, sort_direction=sort_direction, id=id)

Retrieve a list of standalone vm with detailed info

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.stand_alone_vm_list_for_details import StandAloneVmListForDetails
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
    api_instance = taikunpycore.StandaloneApi(api_client)
    project_id = 56 # int | 
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve a list of standalone vm with detailed info
        api_response = api_instance.standalone_details(project_id, sort_by=sort_by, sort_direction=sort_direction, id=id)
        print("The response of StandaloneApi->standalone_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneApi->standalone_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 

### Return type

[**StandAloneVmListForDetails**](StandAloneVmListForDetails.md)

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

# **standalone_ip_management**
> object standalone_ip_management(stand_alone_vm_ip_management_command=stand_alone_vm_ip_management_command)

Enable/Disable stand alone public ip

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.stand_alone_vm_ip_management_command import StandAloneVmIpManagementCommand
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
    api_instance = taikunpycore.StandaloneApi(api_client)
    stand_alone_vm_ip_management_command = taikunpycore.StandAloneVmIpManagementCommand() # StandAloneVmIpManagementCommand |  (optional)

    try:
        # Enable/Disable stand alone public ip
        api_response = api_instance.standalone_ip_management(stand_alone_vm_ip_management_command=stand_alone_vm_ip_management_command)
        print("The response of StandaloneApi->standalone_ip_management:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneApi->standalone_ip_management: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stand_alone_vm_ip_management_command** | [**StandAloneVmIpManagementCommand**](StandAloneVmIpManagementCommand.md)|  | [optional] 

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

# **standalone_list**
> StandaloneVmsList standalone_list(limit=limit, offset=offset, project_id=project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, start_ram=start_ram, end_ram=end_ram, start_volume_size=start_volume_size, end_volume_size=end_volume_size, start_cpu=start_cpu, end_cpu=end_cpu, organization_id=organization_id, id=id, search_id=search_id, filter_by=filter_by)

Retrieve all vms

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.standalone_vms_list import StandaloneVmsList
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
    api_instance = taikunpycore.StandaloneApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    project_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_volume_size = 56 # int |  (optional)
    end_volume_size = 56 # int |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    id = 56 # int |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve all vms
        api_response = api_instance.standalone_list(limit=limit, offset=offset, project_id=project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, start_ram=start_ram, end_ram=end_ram, start_volume_size=start_volume_size, end_volume_size=end_volume_size, start_cpu=start_cpu, end_cpu=end_cpu, organization_id=organization_id, id=id, search_id=search_id, filter_by=filter_by)
        print("The response of StandaloneApi->standalone_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneApi->standalone_list: %s\n" % e)
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
 **start_volume_size** | **int**|  | [optional] 
 **end_volume_size** | **int**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **id** | **int**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**StandaloneVmsList**](StandaloneVmsList.md)

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

# **standalone_reset**
> object standalone_reset(reset_stand_alone_vm_status_command=reset_stand_alone_vm_status_command)

Reset vm status

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.reset_stand_alone_vm_status_command import ResetStandAloneVmStatusCommand
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
    api_instance = taikunpycore.StandaloneApi(api_client)
    reset_stand_alone_vm_status_command = taikunpycore.ResetStandAloneVmStatusCommand() # ResetStandAloneVmStatusCommand |  (optional)

    try:
        # Reset vm status
        api_response = api_instance.standalone_reset(reset_stand_alone_vm_status_command=reset_stand_alone_vm_status_command)
        print("The response of StandaloneApi->standalone_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneApi->standalone_reset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_stand_alone_vm_status_command** | [**ResetStandAloneVmStatusCommand**](ResetStandAloneVmStatusCommand.md)|  | [optional] 

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

# **standalone_update_flavor**
> object standalone_update_flavor(update_stand_alone_vm_flavor_command=update_stand_alone_vm_flavor_command)

Update standalone vm flavor

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_stand_alone_vm_flavor_command import UpdateStandAloneVmFlavorCommand
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
    api_instance = taikunpycore.StandaloneApi(api_client)
    update_stand_alone_vm_flavor_command = taikunpycore.UpdateStandAloneVmFlavorCommand() # UpdateStandAloneVmFlavorCommand |  (optional)

    try:
        # Update standalone vm flavor
        api_response = api_instance.standalone_update_flavor(update_stand_alone_vm_flavor_command=update_stand_alone_vm_flavor_command)
        print("The response of StandaloneApi->standalone_update_flavor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneApi->standalone_update_flavor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_stand_alone_vm_flavor_command** | [**UpdateStandAloneVmFlavorCommand**](UpdateStandAloneVmFlavorCommand.md)|  | [optional] 

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

