# taikunpycore.AutoscalingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autoscaling_disable**](AutoscalingApi.md#autoscaling_disable) | **POST** /api/v1/autoscaling/disable | Disable autoscaling
[**autoscaling_edit**](AutoscalingApi.md#autoscaling_edit) | **POST** /api/v1/autoscaling/edit | Edit autoscaling
[**autoscaling_enable**](AutoscalingApi.md#autoscaling_enable) | **POST** /api/v1/autoscaling/enable | Enable autoscaling
[**autoscaling_sync**](AutoscalingApi.md#autoscaling_sync) | **POST** /api/v1/autoscaling/sync | Sync autoscaling


# **autoscaling_disable**
> object autoscaling_disable(disable_autoscaling_command=disable_autoscaling_command)

Disable autoscaling

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.disable_autoscaling_command import DisableAutoscalingCommand
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
    api_instance = taikunpycore.AutoscalingApi(api_client)
    disable_autoscaling_command = {"projectId":1} # DisableAutoscalingCommand |  (optional)

    try:
        # Disable autoscaling
        api_response = api_instance.autoscaling_disable(disable_autoscaling_command=disable_autoscaling_command)
        print("The response of AutoscalingApi->autoscaling_disable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoscalingApi->autoscaling_disable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_autoscaling_command** | [**DisableAutoscalingCommand**](DisableAutoscalingCommand.md)|  | [optional] 

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

# **autoscaling_edit**
> object autoscaling_edit(edit_autoscaling_command=edit_autoscaling_command)

Edit autoscaling

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.edit_autoscaling_command import EditAutoscalingCommand
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
    api_instance = taikunpycore.AutoscalingApi(api_client)
    edit_autoscaling_command = {"projectId":1,"minSize":1,"maxSize":1} # EditAutoscalingCommand |  (optional)

    try:
        # Edit autoscaling
        api_response = api_instance.autoscaling_edit(edit_autoscaling_command=edit_autoscaling_command)
        print("The response of AutoscalingApi->autoscaling_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoscalingApi->autoscaling_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_autoscaling_command** | [**EditAutoscalingCommand**](EditAutoscalingCommand.md)|  | [optional] 

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

# **autoscaling_enable**
> object autoscaling_enable(enable_autoscaling_command=enable_autoscaling_command)

Enable autoscaling

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.enable_autoscaling_command import EnableAutoscalingCommand
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
    api_instance = taikunpycore.AutoscalingApi(api_client)
    enable_autoscaling_command = {"id":1,"autoscalingGroupName":"taikun","minSize":1,"maxSize":1,"diskSize":32212254720,"flavor":"m1.medium","spotEnabled":false} # EnableAutoscalingCommand |  (optional)

    try:
        # Enable autoscaling
        api_response = api_instance.autoscaling_enable(enable_autoscaling_command=enable_autoscaling_command)
        print("The response of AutoscalingApi->autoscaling_enable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoscalingApi->autoscaling_enable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_autoscaling_command** | [**EnableAutoscalingCommand**](EnableAutoscalingCommand.md)|  | [optional] 

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

# **autoscaling_sync**
> object autoscaling_sync(autoscaling_sync_command=autoscaling_sync_command)

Sync autoscaling

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.autoscaling_sync_command import AutoscalingSyncCommand
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
    api_instance = taikunpycore.AutoscalingApi(api_client)
    autoscaling_sync_command = {"projectId":1} # AutoscalingSyncCommand |  (optional)

    try:
        # Sync autoscaling
        api_response = api_instance.autoscaling_sync(autoscaling_sync_command=autoscaling_sync_command)
        print("The response of AutoscalingApi->autoscaling_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoscalingApi->autoscaling_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **autoscaling_sync_command** | [**AutoscalingSyncCommand**](AutoscalingSyncCommand.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

