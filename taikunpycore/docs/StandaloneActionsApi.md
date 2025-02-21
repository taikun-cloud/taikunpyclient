# taikunpycore.StandaloneActionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**standaloneactions_console**](StandaloneActionsApi.md#standaloneactions_console) | **POST** /api/v1/standaloneactions/console | Console screenshot or terminal for vm
[**standaloneactions_download_rdp**](StandaloneActionsApi.md#standaloneactions_download_rdp) | **GET** /api/v1/standaloneactions/download/rdp/{id} | Download RDP file
[**standaloneactions_reboot**](StandaloneActionsApi.md#standaloneactions_reboot) | **POST** /api/v1/standaloneactions/reboot | Reboot standalone vm
[**standaloneactions_shelve**](StandaloneActionsApi.md#standaloneactions_shelve) | **POST** /api/v1/standaloneactions/shelve | Shelve standalone vm
[**standaloneactions_start**](StandaloneActionsApi.md#standaloneactions_start) | **POST** /api/v1/standaloneactions/start | Start standalone vm
[**standaloneactions_status**](StandaloneActionsApi.md#standaloneactions_status) | **GET** /api/v1/standaloneactions/status/{id} | Show standalone vm status
[**standaloneactions_stop**](StandaloneActionsApi.md#standaloneactions_stop) | **POST** /api/v1/standaloneactions/stop | Stop standalone vm
[**standaloneactions_unshelve**](StandaloneActionsApi.md#standaloneactions_unshelve) | **POST** /api/v1/standaloneactions/unshelve | Unshelve standalone vm
[**standaloneactions_windows_instance_password**](StandaloneActionsApi.md#standaloneactions_windows_instance_password) | **POST** /api/v1/standaloneactions/password | Retrieve aws windows admin instance password


# **standaloneactions_console**
> str standaloneactions_console(vm_console_screenshot_command)

Console screenshot or terminal for vm

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.vm_console_screenshot_command import VmConsoleScreenshotCommand
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
    api_instance = taikunpycore.StandaloneActionsApi(api_client)
    vm_console_screenshot_command = taikunpycore.VmConsoleScreenshotCommand() # VmConsoleScreenshotCommand | 

    try:
        # Console screenshot or terminal for vm
        api_response = api_instance.standaloneactions_console(vm_console_screenshot_command)
        print("The response of StandaloneActionsApi->standaloneactions_console:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneActionsApi->standaloneactions_console: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_console_screenshot_command** | [**VmConsoleScreenshotCommand**](VmConsoleScreenshotCommand.md)|  | 

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

# **standaloneactions_download_rdp**
> CsvExporter standaloneactions_download_rdp(id)

Download RDP file

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.csv_exporter import CsvExporter
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
    api_instance = taikunpycore.StandaloneActionsApi(api_client)
    id = 56 # int | 

    try:
        # Download RDP file
        api_response = api_instance.standaloneactions_download_rdp(id)
        print("The response of StandaloneActionsApi->standaloneactions_download_rdp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneActionsApi->standaloneactions_download_rdp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CsvExporter**](CsvExporter.md)

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

# **standaloneactions_reboot**
> object standaloneactions_reboot(reboot_stand_alone_vm_command)

Reboot standalone vm

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.reboot_stand_alone_vm_command import RebootStandAloneVmCommand
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
    api_instance = taikunpycore.StandaloneActionsApi(api_client)
    reboot_stand_alone_vm_command = taikunpycore.RebootStandAloneVmCommand() # RebootStandAloneVmCommand | 

    try:
        # Reboot standalone vm
        api_response = api_instance.standaloneactions_reboot(reboot_stand_alone_vm_command)
        print("The response of StandaloneActionsApi->standaloneactions_reboot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneActionsApi->standaloneactions_reboot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reboot_stand_alone_vm_command** | [**RebootStandAloneVmCommand**](RebootStandAloneVmCommand.md)|  | 

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

# **standaloneactions_shelve**
> object standaloneactions_shelve(shelve_stand_alone_vm_command)

Shelve standalone vm

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.shelve_stand_alone_vm_command import ShelveStandAloneVmCommand
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
    api_instance = taikunpycore.StandaloneActionsApi(api_client)
    shelve_stand_alone_vm_command = taikunpycore.ShelveStandAloneVmCommand() # ShelveStandAloneVmCommand | 

    try:
        # Shelve standalone vm
        api_response = api_instance.standaloneactions_shelve(shelve_stand_alone_vm_command)
        print("The response of StandaloneActionsApi->standaloneactions_shelve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneActionsApi->standaloneactions_shelve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shelve_stand_alone_vm_command** | [**ShelveStandAloneVmCommand**](ShelveStandAloneVmCommand.md)|  | 

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

# **standaloneactions_start**
> object standaloneactions_start(start_standalone_vm_command)

Start standalone vm

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.start_standalone_vm_command import StartStandaloneVmCommand
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
    api_instance = taikunpycore.StandaloneActionsApi(api_client)
    start_standalone_vm_command = taikunpycore.StartStandaloneVmCommand() # StartStandaloneVmCommand | 

    try:
        # Start standalone vm
        api_response = api_instance.standaloneactions_start(start_standalone_vm_command)
        print("The response of StandaloneActionsApi->standaloneactions_start:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneActionsApi->standaloneactions_start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_standalone_vm_command** | [**StartStandaloneVmCommand**](StartStandaloneVmCommand.md)|  | 

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

# **standaloneactions_status**
> str standaloneactions_status(id)

Show standalone vm status

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
    api_instance = taikunpycore.StandaloneActionsApi(api_client)
    id = 56 # int | 

    try:
        # Show standalone vm status
        api_response = api_instance.standaloneactions_status(id)
        print("The response of StandaloneActionsApi->standaloneactions_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneActionsApi->standaloneactions_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

# **standaloneactions_stop**
> object standaloneactions_stop(stop_standalone_vm_command)

Stop standalone vm

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.stop_standalone_vm_command import StopStandaloneVmCommand
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
    api_instance = taikunpycore.StandaloneActionsApi(api_client)
    stop_standalone_vm_command = taikunpycore.StopStandaloneVmCommand() # StopStandaloneVmCommand | 

    try:
        # Stop standalone vm
        api_response = api_instance.standaloneactions_stop(stop_standalone_vm_command)
        print("The response of StandaloneActionsApi->standaloneactions_stop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneActionsApi->standaloneactions_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop_standalone_vm_command** | [**StopStandaloneVmCommand**](StopStandaloneVmCommand.md)|  | 

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

# **standaloneactions_unshelve**
> object standaloneactions_unshelve(unshelve_standalone_vm_command)

Unshelve standalone vm

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.unshelve_standalone_vm_command import UnshelveStandaloneVmCommand
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
    api_instance = taikunpycore.StandaloneActionsApi(api_client)
    unshelve_standalone_vm_command = taikunpycore.UnshelveStandaloneVmCommand() # UnshelveStandaloneVmCommand | 

    try:
        # Unshelve standalone vm
        api_response = api_instance.standaloneactions_unshelve(unshelve_standalone_vm_command)
        print("The response of StandaloneActionsApi->standaloneactions_unshelve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneActionsApi->standaloneactions_unshelve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unshelve_standalone_vm_command** | [**UnshelveStandaloneVmCommand**](UnshelveStandaloneVmCommand.md)|  | 

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

# **standaloneactions_windows_instance_password**
> str standaloneactions_windows_instance_password(id=id, key=key, config=config)

Retrieve aws windows admin instance password

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
    api_instance = taikunpycore.StandaloneActionsApi(api_client)
    id = 56 # int |  (optional)
    key = 'key_example' # str |  (optional)
    config = None # bytearray |  (optional)

    try:
        # Retrieve aws windows admin instance password
        api_response = api_instance.standaloneactions_windows_instance_password(id=id, key=key, config=config)
        print("The response of StandaloneActionsApi->standaloneactions_windows_instance_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneActionsApi->standaloneactions_windows_instance_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 
 **key** | **str**|  | [optional] 
 **config** | **bytearray**|  | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

