# taikunpycore.GoogleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**googlecloud_billing_account_list**](GoogleApi.md#googlecloud_billing_account_list) | **POST** /api/v1/googlecloud/billing-accounts | Retrieve google billing accounts list
[**googlecloud_create**](GoogleApi.md#googlecloud_create) | **POST** /api/v1/googlecloud/create | Create google cloud credential
[**googlecloud_gke_clusters**](GoogleApi.md#googlecloud_gke_clusters) | **POST** /api/v1/googlecloud/gke-clusters | List of gke clusters
[**googlecloud_list**](GoogleApi.md#googlecloud_list) | **GET** /api/v1/googlecloud/list | Retrieve list of google cloud credentials
[**googlecloud_region_list**](GoogleApi.md#googlecloud_region_list) | **POST** /api/v1/googlecloud/regions | Retrieve google region list
[**googlecloud_zone_list**](GoogleApi.md#googlecloud_zone_list) | **POST** /api/v1/googlecloud/zones | Google zones list


# **googlecloud_billing_account_list**
> List[CommonStringBasedDropdownDto] googlecloud_billing_account_list(config=config)

Retrieve google billing accounts list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_string_based_dropdown_dto import CommonStringBasedDropdownDto
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
    api_instance = taikunpycore.GoogleApi(api_client)
    config = None # bytearray |  (optional)

    try:
        # Retrieve google billing accounts list
        api_response = api_instance.googlecloud_billing_account_list(config=config)
        print("The response of GoogleApi->googlecloud_billing_account_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleApi->googlecloud_billing_account_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | **bytearray**|  | [optional] 

### Return type

[**List[CommonStringBasedDropdownDto]**](CommonStringBasedDropdownDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **googlecloud_create**
> ApiResponse googlecloud_create(config=config, name=name, import_project=import_project, folder_id=folder_id, billing_account_id=billing_account_id, az_count=az_count, region=region, organization_id=organization_id)

Create google cloud credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
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
    api_instance = taikunpycore.GoogleApi(api_client)
    config = None # bytearray |  (optional)
    name = 'name_example' # str |  (optional)
    import_project = True # bool |  (optional)
    folder_id = 'folder_id_example' # str |  (optional)
    billing_account_id = 'billing_account_id_example' # str |  (optional)
    az_count = 56 # int |  (optional)
    region = 'region_example' # str |  (optional)
    organization_id = 56 # int |  (optional)

    try:
        # Create google cloud credential
        api_response = api_instance.googlecloud_create(config=config, name=name, import_project=import_project, folder_id=folder_id, billing_account_id=billing_account_id, az_count=az_count, region=region, organization_id=organization_id)
        print("The response of GoogleApi->googlecloud_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleApi->googlecloud_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | **bytearray**|  | [optional] 
 **name** | **str**|  | [optional] 
 **import_project** | **bool**|  | [optional] 
 **folder_id** | **str**|  | [optional] 
 **billing_account_id** | **str**|  | [optional] 
 **az_count** | **int**|  | [optional] 
 **region** | **str**|  | [optional] 
 **organization_id** | **int**|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **googlecloud_gke_clusters**
> List[GkeClusterDto] googlecloud_gke_clusters(gke_clusters_list_command=gke_clusters_list_command)

List of gke clusters

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.gke_cluster_dto import GkeClusterDto
from taikunpycore.models.gke_clusters_list_command import GkeClustersListCommand
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
    api_instance = taikunpycore.GoogleApi(api_client)
    gke_clusters_list_command = taikunpycore.GkeClustersListCommand() # GkeClustersListCommand |  (optional)

    try:
        # List of gke clusters
        api_response = api_instance.googlecloud_gke_clusters(gke_clusters_list_command=gke_clusters_list_command)
        print("The response of GoogleApi->googlecloud_gke_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleApi->googlecloud_gke_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gke_clusters_list_command** | [**GkeClustersListCommand**](GkeClustersListCommand.md)|  | [optional] 

### Return type

[**List[GkeClusterDto]**](GkeClusterDto.md)

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

# **googlecloud_list**
> GoogleCredentialList googlecloud_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)

Retrieve list of google cloud credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.google_credential_list import GoogleCredentialList
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
    api_instance = taikunpycore.GoogleApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve list of google cloud credentials
        api_response = api_instance.googlecloud_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)
        print("The response of GoogleApi->googlecloud_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleApi->googlecloud_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 

### Return type

[**GoogleCredentialList**](GoogleCredentialList.md)

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

# **googlecloud_region_list**
> List[str] googlecloud_region_list(config=config)

Retrieve google region list

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
    api_instance = taikunpycore.GoogleApi(api_client)
    config = None # bytearray |  (optional)

    try:
        # Retrieve google region list
        api_response = api_instance.googlecloud_region_list(config=config)
        print("The response of GoogleApi->googlecloud_region_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleApi->googlecloud_region_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | **bytearray**|  | [optional] 

### Return type

**List[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **googlecloud_zone_list**
> AzResult googlecloud_zone_list(config=config, region=region, cloud_id=cloud_id)

Google zones list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.az_result import AzResult
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
    api_instance = taikunpycore.GoogleApi(api_client)
    config = None # bytearray |  (optional)
    region = 'region_example' # str |  (optional)
    cloud_id = 56 # int |  (optional)

    try:
        # Google zones list
        api_response = api_instance.googlecloud_zone_list(config=config, region=region, cloud_id=cloud_id)
        print("The response of GoogleApi->googlecloud_zone_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleApi->googlecloud_zone_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | **bytearray**|  | [optional] 
 **region** | **str**|  | [optional] 
 **cloud_id** | **int**|  | [optional] 

### Return type

[**AzResult**](AzResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

