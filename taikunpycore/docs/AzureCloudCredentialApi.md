# taikunpycore.AzureCloudCredentialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**azure_aks_clusters**](AzureCloudCredentialApi.md#azure_aks_clusters) | **POST** /api/v1/azure/aks-clusters | Fetch AKS cluster list
[**azure_create**](AzureCloudCredentialApi.md#azure_create) | **POST** /api/v1/azure/create | Add Azure credentials
[**azure_dashboard**](AzureCloudCredentialApi.md#azure_dashboard) | **POST** /api/v1/azure/quota/list | Fetch Azure quota list
[**azure_list**](AzureCloudCredentialApi.md#azure_list) | **GET** /api/v1/azure/list | Retrieve list of azure cloud credentials
[**azure_locations**](AzureCloudCredentialApi.md#azure_locations) | **POST** /api/v1/azure/locations | Fetch Azure location list
[**azure_offers**](AzureCloudCredentialApi.md#azure_offers) | **GET** /api/v1/azure/offers/{cloudId}/{publisher} | List Azure offer list by publisher
[**azure_publishers**](AzureCloudCredentialApi.md#azure_publishers) | **GET** /api/v1/azure/publishers/{cloudId} | List Azure publishers list
[**azure_skus**](AzureCloudCredentialApi.md#azure_skus) | **GET** /api/v1/azure/skus/{cloudId}/{publisher}/{offer} | List Azure skus list by publisher and offer
[**azure_subscriptions**](AzureCloudCredentialApi.md#azure_subscriptions) | **POST** /api/v1/azure/subscriptions | Azure subscriptions list
[**azure_update**](AzureCloudCredentialApi.md#azure_update) | **POST** /api/v1/azure/update | Update Azure credentials
[**azure_zones**](AzureCloudCredentialApi.md#azure_zones) | **POST** /api/v1/azure/zones | Fetch Azure zone list


# **azure_aks_clusters**
> List[AzureAksClusterDto] azure_aks_clusters(aks_cluster_list_command)

Fetch AKS cluster list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.aks_cluster_list_command import AksClusterListCommand
from taikunpycore.models.azure_aks_cluster_dto import AzureAksClusterDto
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
    api_instance = taikunpycore.AzureCloudCredentialApi(api_client)
    aks_cluster_list_command = taikunpycore.AksClusterListCommand() # AksClusterListCommand | 

    try:
        # Fetch AKS cluster list
        api_response = api_instance.azure_aks_clusters(aks_cluster_list_command)
        print("The response of AzureCloudCredentialApi->azure_aks_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AzureCloudCredentialApi->azure_aks_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aks_cluster_list_command** | [**AksClusterListCommand**](AksClusterListCommand.md)|  | 

### Return type

[**List[AzureAksClusterDto]**](AzureAksClusterDto.md)

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

# **azure_create**
> ApiResponse azure_create(create_azure_cloud_command=create_azure_cloud_command)

Add Azure credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_azure_cloud_command import CreateAzureCloudCommand
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
    api_instance = taikunpycore.AzureCloudCredentialApi(api_client)
    create_azure_cloud_command = {"name":"taikun","azureSubscriptionId":"8fc9a50d-d38d-4954-bec6-f1a82a88fd7a","azureClientId":"10b66731-3ab9-4f50-be3c-c355c83b6c7m","azureClientSecret":"i1T8Q~Kzore4p61zGD3MZWWh1R~VmnrjlOWBsaxm","azureTenantId":"8e15c4c4-8226-4a29-8ffc-9b4004bf3f4m","azureLocation":"Europe","azCount":1,"organizationId":1} # CreateAzureCloudCommand |  (optional)

    try:
        # Add Azure credentials
        api_response = api_instance.azure_create(create_azure_cloud_command=create_azure_cloud_command)
        print("The response of AzureCloudCredentialApi->azure_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AzureCloudCredentialApi->azure_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_azure_cloud_command** | [**CreateAzureCloudCommand**](CreateAzureCloudCommand.md)|  | [optional] 

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

# **azure_dashboard**
> List[AzureQuotaListRecordDto] azure_dashboard(azure_dashboard_command=azure_dashboard_command)

Fetch Azure quota list

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>FilterBy</b> - Options: <i>cpu</i>, <i>storage</i>, <i>gallery</i>, <i>general</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.azure_dashboard_command import AzureDashboardCommand
from taikunpycore.models.azure_quota_list_record_dto import AzureQuotaListRecordDto
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
    api_instance = taikunpycore.AzureCloudCredentialApi(api_client)
    azure_dashboard_command = taikunpycore.AzureDashboardCommand() # AzureDashboardCommand |  (optional)

    try:
        # Fetch Azure quota list
        api_response = api_instance.azure_dashboard(azure_dashboard_command=azure_dashboard_command)
        print("The response of AzureCloudCredentialApi->azure_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AzureCloudCredentialApi->azure_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_dashboard_command** | [**AzureDashboardCommand**](AzureDashboardCommand.md)|  | [optional] 

### Return type

[**List[AzureQuotaListRecordDto]**](AzureQuotaListRecordDto.md)

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

# **azure_list**
> AzureCredentialList azure_list(organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id, limit=limit, offset=offset)

Retrieve list of azure cloud credentials

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>SortBy</b> - Options: <i>azureLocation</i>, <i>organizationName</i>, <i>createdAt</i><li><b>SortDirection</b> - Options: <i>asc</i>, <i>desc</i><li><b>Search</b> - Options: <i>name</i>, <i>organizationName</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.azure_credential_list import AzureCredentialList
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
    api_instance = taikunpycore.AzureCloudCredentialApi(api_client)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Retrieve list of azure cloud credentials
        api_response = api_instance.azure_list(organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id, limit=limit, offset=offset)
        print("The response of AzureCloudCredentialApi->azure_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AzureCloudCredentialApi->azure_list: %s\n" % e)
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

[**AzureCredentialList**](AzureCredentialList.md)

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

# **azure_locations**
> List[str] azure_locations(azure_locations_command=azure_locations_command)

Fetch Azure location list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.azure_locations_command import AzureLocationsCommand
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
    api_instance = taikunpycore.AzureCloudCredentialApi(api_client)
    azure_locations_command = {"azureSubscriptionId":"8fc9a50d-d38d-4954-bec6-f1a82a88fd7a","azureClientId":"10b66731-3ab9-4f50-be3c-c355c83b6c7m","azureClientSecret":"i1T8Q~Kzore4p61zGD3MZWWh1R~VmnrjlOWBsaxm","azureTenantId":"8e15c4c4-8226-4a29-8ffc-9b4004bf3f4m"} # AzureLocationsCommand |  (optional)

    try:
        # Fetch Azure location list
        api_response = api_instance.azure_locations(azure_locations_command=azure_locations_command)
        print("The response of AzureCloudCredentialApi->azure_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AzureCloudCredentialApi->azure_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_locations_command** | [**AzureLocationsCommand**](AzureLocationsCommand.md)|  | [optional] 

### Return type

**List[str]**

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

# **azure_offers**
> AzureOffersList azure_offers(cloud_id, publisher, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)

List Azure offer list by publisher

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>SortBy</b> - Options: <i>name</i><li><b>SortDirection</b> - Options: <i>asc</i>, <i>desc</i><li><b>Search</b> - Options: <i>azureOffer</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.azure_offers_list import AzureOffersList
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
    api_instance = taikunpycore.AzureCloudCredentialApi(api_client)
    cloud_id = 56 # int | 
    publisher = 'publisher_example' # str | 
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Azure offer list by publisher
        api_response = api_instance.azure_offers(cloud_id, publisher, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)
        print("The response of AzureCloudCredentialApi->azure_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AzureCloudCredentialApi->azure_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **publisher** | **str**|  | 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**AzureOffersList**](AzureOffersList.md)

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

# **azure_publishers**
> AzurePublishersList azure_publishers(cloud_id, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)

List Azure publishers list

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>SortBy</b> - Options: <i>name</i><li><b>SortDirection</b> - Options: <i>asc</i>, <i>desc</i><li><b>Search</b> - Options: <i>azurePublisher</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.azure_publishers_list import AzurePublishersList
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
    api_instance = taikunpycore.AzureCloudCredentialApi(api_client)
    cloud_id = 56 # int | 
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Azure publishers list
        api_response = api_instance.azure_publishers(cloud_id, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)
        print("The response of AzureCloudCredentialApi->azure_publishers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AzureCloudCredentialApi->azure_publishers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**AzurePublishersList**](AzurePublishersList.md)

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

# **azure_skus**
> AzureSkusList azure_skus(cloud_id, publisher, offer, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)

List Azure skus list by publisher and offer

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>SortBy</b> - Options: <i>name</i><li><b>SortDirection</b> - Options: <i>asc</i>, <i>desc</i><li><b>Search</b> - Options: <i>azureSku</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.azure_skus_list import AzureSkusList
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
    api_instance = taikunpycore.AzureCloudCredentialApi(api_client)
    cloud_id = 56 # int | 
    publisher = 'publisher_example' # str | 
    offer = 'offer_example' # str | 
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Azure skus list by publisher and offer
        api_response = api_instance.azure_skus(cloud_id, publisher, offer, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)
        print("The response of AzureCloudCredentialApi->azure_skus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AzureCloudCredentialApi->azure_skus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **publisher** | **str**|  | 
 **offer** | **str**|  | 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**AzureSkusList**](AzureSkusList.md)

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

# **azure_subscriptions**
> List[CommonStringBasedDropdownDto] azure_subscriptions(azure_subscription_list_command=azure_subscription_list_command)

Azure subscriptions list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.azure_subscription_list_command import AzureSubscriptionListCommand
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
    api_instance = taikunpycore.AzureCloudCredentialApi(api_client)
    azure_subscription_list_command = {"clientId":"10b66731-3ab9-4f50-be3c-c355c83b6c7m","clientSecret":"i1T8Q~Kzore4p61zGD3MZWWh1R~VmnrjlOWBsaxm","tenantId":"8e15c4c4-8226-4a29-8ffc-9b4004bf3f4m"} # AzureSubscriptionListCommand |  (optional)

    try:
        # Azure subscriptions list
        api_response = api_instance.azure_subscriptions(azure_subscription_list_command=azure_subscription_list_command)
        print("The response of AzureCloudCredentialApi->azure_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AzureCloudCredentialApi->azure_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_subscription_list_command** | [**AzureSubscriptionListCommand**](AzureSubscriptionListCommand.md)|  | [optional] 

### Return type

[**List[CommonStringBasedDropdownDto]**](CommonStringBasedDropdownDto.md)

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

# **azure_update**
> object azure_update(update_azure_command=update_azure_command)

Update Azure credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_azure_command import UpdateAzureCommand
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
    api_instance = taikunpycore.AzureCloudCredentialApi(api_client)
    update_azure_command = {"id":1,"name":"taikun","azureClientSecret":"i1T8Q~Kzore4p61zGD3MZWWh1R~VmnrjlOWBsaxm","azureClientId":"10b66731-3ab9-4f50-be3c-c355c83b6c7m"} # UpdateAzureCommand |  (optional)

    try:
        # Update Azure credentials
        api_response = api_instance.azure_update(update_azure_command=update_azure_command)
        print("The response of AzureCloudCredentialApi->azure_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AzureCloudCredentialApi->azure_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_azure_command** | [**UpdateAzureCommand**](UpdateAzureCommand.md)|  | [optional] 

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

# **azure_zones**
> AzResult azure_zones(azure_zones_command=azure_zones_command)

Fetch Azure zone list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.az_result import AzResult
from taikunpycore.models.azure_zones_command import AzureZonesCommand
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
    api_instance = taikunpycore.AzureCloudCredentialApi(api_client)
    azure_zones_command = {"azureSubscriptionId":"8fc9a50d-d38d-4954-bec6-f1a82a88fd7a","azureClientId":"10b66731-3ab9-4f50-be3c-c355c83b6c7m","azureClientSecret":"i1T8Q~Kzore4p61zGD3MZWWh1R~VmnrjlOWBsaxm","azureTenantId":"8e15c4c4-8226-4a29-8ffc-9b4004bf3f4m","azureLocation":"8e15c4c4-8226-4a29-8ffc-9b4004bf3f4m","cloudId":1} # AzureZonesCommand |  (optional)

    try:
        # Fetch Azure zone list
        api_response = api_instance.azure_zones(azure_zones_command=azure_zones_command)
        print("The response of AzureCloudCredentialApi->azure_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AzureCloudCredentialApi->azure_zones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_zones_command** | [**AzureZonesCommand**](AzureZonesCommand.md)|  | [optional] 

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

