# taikunpycore.ZadaraCloudCredentialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zadara_create**](ZadaraCloudCredentialApi.md#zadara_create) | **POST** /api/v1/zadara/create | Add Zadara credentials
[**zadara_list**](ZadaraCloudCredentialApi.md#zadara_list) | **GET** /api/v1/zadara/list | Retrieve list of Zadara cloud credentials
[**zadara_regionlist**](ZadaraCloudCredentialApi.md#zadara_regionlist) | **POST** /api/v1/zadara/regions | Retrieve zadara regions list
[**zadara_update**](ZadaraCloudCredentialApi.md#zadara_update) | **POST** /api/v1/zadara/update | Update zadara cloud credential
[**zadara_volume_type_list**](ZadaraCloudCredentialApi.md#zadara_volume_type_list) | **GET** /api/v1/zadara/volume-types | Retrieve volume type list
[**zadara_zonelist**](ZadaraCloudCredentialApi.md#zadara_zonelist) | **POST** /api/v1/zadara/zones | Retrieve zadara zone list


# **zadara_create**
> ApiResponse zadara_create(create_zadara_cloud_command=create_zadara_cloud_command)

Add Zadara credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_zadara_cloud_command import CreateZadaraCloudCommand
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
    api_instance = taikunpycore.ZadaraCloudCredentialApi(api_client)
    create_zadara_cloud_command = {"name":"taikun","zadaraUrl":"https://www.google.com","zadaraSecretAccessKey":"rd98DUXrLkcxI5rqcimJD2BkrsRUZmbqBSwcAcIm","zadaraAccessKeyId":"X9BZGP8TSTB7D4K6N9U8","zadaraRegion":"ap-south-1","organizationId":1,"azCount":1,"zadaraContinent":"Europe","zadaraVolumeType":"taikun"} # CreateZadaraCloudCommand |  (optional)

    try:
        # Add Zadara credentials
        api_response = api_instance.zadara_create(create_zadara_cloud_command=create_zadara_cloud_command)
        print("The response of ZadaraCloudCredentialApi->zadara_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZadaraCloudCredentialApi->zadara_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_zadara_cloud_command** | [**CreateZadaraCloudCommand**](CreateZadaraCloudCommand.md)|  | [optional] 

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

# **zadara_list**
> ZadaraCredentialList zadara_list(organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id, limit=limit, offset=offset)

Retrieve list of Zadara cloud credentials

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>SortBy</b> - Options: <i>zadaraRegion</i>, <i>organizationName</i>, <i>createdAt</i><li><b>SortDirection</b> - Options: <i>asc</i>, <i>desc</i><li><b>Search</b> - Options: <i>name</i>, <i>organizationName</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.zadara_credential_list import ZadaraCredentialList
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
    api_instance = taikunpycore.ZadaraCloudCredentialApi(api_client)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Retrieve list of Zadara cloud credentials
        api_response = api_instance.zadara_list(organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id, limit=limit, offset=offset)
        print("The response of ZadaraCloudCredentialApi->zadara_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZadaraCloudCredentialApi->zadara_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ZadaraCredentialList**](ZadaraCredentialList.md)

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

# **zadara_regionlist**
> List[AwsRegionDto] zadara_regionlist(zadara_region_list_command=zadara_region_list_command)

Retrieve zadara regions list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.aws_region_dto import AwsRegionDto
from taikunpycore.models.zadara_region_list_command import ZadaraRegionListCommand
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
    api_instance = taikunpycore.ZadaraCloudCredentialApi(api_client)
    zadara_region_list_command = {"url":"https://www.google.com","zadaraAccessKeyId":"X9BZGP8TSTB7D4K6N9U8","zadaraSecretAccessKey":"rd98DUXrLkcxI5rqcimJD2BkrsRUZmbqBSwcAcIm"} # ZadaraRegionListCommand |  (optional)

    try:
        # Retrieve zadara regions list
        api_response = api_instance.zadara_regionlist(zadara_region_list_command=zadara_region_list_command)
        print("The response of ZadaraCloudCredentialApi->zadara_regionlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZadaraCloudCredentialApi->zadara_regionlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zadara_region_list_command** | [**ZadaraRegionListCommand**](ZadaraRegionListCommand.md)|  | [optional] 

### Return type

[**List[AwsRegionDto]**](AwsRegionDto.md)

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

# **zadara_update**
> object zadara_update(update_zadara_command=update_zadara_command)

Update zadara cloud credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_zadara_command import UpdateZadaraCommand
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
    api_instance = taikunpycore.ZadaraCloudCredentialApi(api_client)
    update_zadara_command = {"id":1,"name":"taikun","zadaraSecretAccessKey":"rd98DUXrLkcxI5rqcimJD2BkrsRUZmbqBSwcAcIm","zadaraAccessKeyId":"X9BZGP8TSTB7D4K6N9U8"} # UpdateZadaraCommand |  (optional)

    try:
        # Update zadara cloud credential
        api_response = api_instance.zadara_update(update_zadara_command=update_zadara_command)
        print("The response of ZadaraCloudCredentialApi->zadara_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZadaraCloudCredentialApi->zadara_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_zadara_command** | [**UpdateZadaraCommand**](UpdateZadaraCommand.md)|  | [optional] 

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

# **zadara_volume_type_list**
> List[str] zadara_volume_type_list()

Retrieve volume type list

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
    api_instance = taikunpycore.ZadaraCloudCredentialApi(api_client)

    try:
        # Retrieve volume type list
        api_response = api_instance.zadara_volume_type_list()
        print("The response of ZadaraCloudCredentialApi->zadara_volume_type_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZadaraCloudCredentialApi->zadara_volume_type_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **zadara_zonelist**
> AzResult zadara_zonelist(zadara_availability_zones_command=zadara_availability_zones_command)

Retrieve zadara zone list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.az_result import AzResult
from taikunpycore.models.zadara_availability_zones_command import ZadaraAvailabilityZonesCommand
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
    api_instance = taikunpycore.ZadaraCloudCredentialApi(api_client)
    zadara_availability_zones_command = {"url":"https://www.google.com","zadaraAccessKeyId":"X9BZGP8TSTB7D4K6N9U8","zadaraSecretAccessKey":"rd98DUXrLkcxI5rqcimJD2BkrsRUZmbqBSwcAcIm","cloudId":1} # ZadaraAvailabilityZonesCommand |  (optional)

    try:
        # Retrieve zadara zone list
        api_response = api_instance.zadara_zonelist(zadara_availability_zones_command=zadara_availability_zones_command)
        print("The response of ZadaraCloudCredentialApi->zadara_zonelist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZadaraCloudCredentialApi->zadara_zonelist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zadara_availability_zones_command** | [**ZadaraAvailabilityZonesCommand**](ZadaraAvailabilityZonesCommand.md)|  | [optional] 

### Return type

[**AzResult**](AzResult.md)

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

