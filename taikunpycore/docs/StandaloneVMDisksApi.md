# taikunpycore.StandaloneVMDisksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**standalonevmdisks_create**](StandaloneVMDisksApi.md#standalonevmdisks_create) | **POST** /api/v1/standalonevmdisks/create | Add disk for standalone vm
[**standalonevmdisks_update_size**](StandaloneVMDisksApi.md#standalonevmdisks_update_size) | **POST** /api/v1/standalonevmdisks/update-size | Update disk size


# **standalonevmdisks_create**
> ApiResponse standalonevmdisks_create(create_stand_alone_disk_command=create_stand_alone_disk_command)

Add disk for standalone vm

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_stand_alone_disk_command import CreateStandAloneDiskCommand
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
    api_instance = taikunpycore.StandaloneVMDisksApi(api_client)
    create_stand_alone_disk_command = taikunpycore.CreateStandAloneDiskCommand() # CreateStandAloneDiskCommand |  (optional)

    try:
        # Add disk for standalone vm
        api_response = api_instance.standalonevmdisks_create(create_stand_alone_disk_command=create_stand_alone_disk_command)
        print("The response of StandaloneVMDisksApi->standalonevmdisks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneVMDisksApi->standalonevmdisks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_stand_alone_disk_command** | [**CreateStandAloneDiskCommand**](CreateStandAloneDiskCommand.md)|  | [optional] 

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

# **standalonevmdisks_update_size**
> object standalonevmdisks_update_size(update_standalone_vm_disk_size_command=update_standalone_vm_disk_size_command)

Update disk size

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_standalone_vm_disk_size_command import UpdateStandaloneVmDiskSizeCommand
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
    api_instance = taikunpycore.StandaloneVMDisksApi(api_client)
    update_standalone_vm_disk_size_command = taikunpycore.UpdateStandaloneVmDiskSizeCommand() # UpdateStandaloneVmDiskSizeCommand |  (optional)

    try:
        # Update disk size
        api_response = api_instance.standalonevmdisks_update_size(update_standalone_vm_disk_size_command=update_standalone_vm_disk_size_command)
        print("The response of StandaloneVMDisksApi->standalonevmdisks_update_size:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneVMDisksApi->standalonevmdisks_update_size: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_standalone_vm_disk_size_command** | [**UpdateStandaloneVmDiskSizeCommand**](UpdateStandaloneVmDiskSizeCommand.md)|  | [optional] 

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

