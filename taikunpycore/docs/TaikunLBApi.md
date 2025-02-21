# taikunpycore.TaikunLBApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taikun_lb_create_taikun_lb**](TaikunLBApi.md#taikun_lb_create_taikun_lb) | **POST** /api/v1/taikun-lb/create/{projectId} | Create Taikun LB
[**taikun_lb_delete_taikun_lb**](TaikunLBApi.md#taikun_lb_delete_taikun_lb) | **POST** /api/v1/taikun-lb/delete/{projectId} | Delete Taikun LB
[**taikun_lb_list_taikun_lb**](TaikunLBApi.md#taikun_lb_list_taikun_lb) | **GET** /api/v1/taikun-lb/list/{projectId} | Retrieve taikun lbs for project


# **taikun_lb_create_taikun_lb**
> TaikunLbResponseDto taikun_lb_create_taikun_lb(project_id, create_generic_taikun_lb_dto=create_generic_taikun_lb_dto)

Create Taikun LB

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.create_generic_taikun_lb_dto import CreateGenericTaikunLbDto
from taikunpycore.models.taikun_lb_response_dto import TaikunLbResponseDto
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
    api_instance = taikunpycore.TaikunLBApi(api_client)
    project_id = 56 # int | 
    create_generic_taikun_lb_dto = taikunpycore.CreateGenericTaikunLbDto() # CreateGenericTaikunLbDto |  (optional)

    try:
        # Create Taikun LB
        api_response = api_instance.taikun_lb_create_taikun_lb(project_id, create_generic_taikun_lb_dto=create_generic_taikun_lb_dto)
        print("The response of TaikunLBApi->taikun_lb_create_taikun_lb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaikunLBApi->taikun_lb_create_taikun_lb: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **create_generic_taikun_lb_dto** | [**CreateGenericTaikunLbDto**](CreateGenericTaikunLbDto.md)|  | [optional] 

### Return type

[**TaikunLbResponseDto**](TaikunLbResponseDto.md)

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

# **taikun_lb_delete_taikun_lb**
> object taikun_lb_delete_taikun_lb(project_id, create_generic_taikun_lb_dto=create_generic_taikun_lb_dto)

Delete Taikun LB

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.create_generic_taikun_lb_dto import CreateGenericTaikunLbDto
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
    api_instance = taikunpycore.TaikunLBApi(api_client)
    project_id = 56 # int | 
    create_generic_taikun_lb_dto = taikunpycore.CreateGenericTaikunLbDto() # CreateGenericTaikunLbDto |  (optional)

    try:
        # Delete Taikun LB
        api_response = api_instance.taikun_lb_delete_taikun_lb(project_id, create_generic_taikun_lb_dto=create_generic_taikun_lb_dto)
        print("The response of TaikunLBApi->taikun_lb_delete_taikun_lb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaikunLBApi->taikun_lb_delete_taikun_lb: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **create_generic_taikun_lb_dto** | [**CreateGenericTaikunLbDto**](CreateGenericTaikunLbDto.md)|  | [optional] 

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

# **taikun_lb_list_taikun_lb**
> List[TaikunLbResponseDto] taikun_lb_list_taikun_lb(project_id, svc_name=svc_name, svc_name_space=svc_name_space)

Retrieve taikun lbs for project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.taikun_lb_response_dto import TaikunLbResponseDto
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
    api_instance = taikunpycore.TaikunLBApi(api_client)
    project_id = 56 # int | 
    svc_name = 'svc_name_example' # str |  (optional)
    svc_name_space = 'svc_name_space_example' # str |  (optional)

    try:
        # Retrieve taikun lbs for project
        api_response = api_instance.taikun_lb_list_taikun_lb(project_id, svc_name=svc_name, svc_name_space=svc_name_space)
        print("The response of TaikunLBApi->taikun_lb_list_taikun_lb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaikunLBApi->taikun_lb_list_taikun_lb: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **svc_name** | **str**|  | [optional] 
 **svc_name_space** | **str**|  | [optional] 

### Return type

[**List[TaikunLbResponseDto]**](TaikunLbResponseDto.md)

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

