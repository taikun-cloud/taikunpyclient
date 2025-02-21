# taikunpycore.PackageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**package_details**](PackageApi.md#package_details) | **GET** /api/v1/package/{repoName}/{packageName} | Available helm package details
[**package_list**](PackageApi.md#package_list) | **GET** /api/v1/package/list | Retrieve all available packages
[**package_value**](PackageApi.md#package_value) | **POST** /api/v1/package/value | Get yaml based value
[**package_value_autocomplete**](PackageApi.md#package_value_autocomplete) | **POST** /api/v1/package/value-autocomplete | Get autocomplete dictionary
[**package_versions**](PackageApi.md#package_versions) | **POST** /api/v1/package/versions | Get available versions


# **package_details**
> AvailablePackageDetailsDto package_details(repo_name, package_name, organization_id=organization_id)

Available helm package details

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.available_package_details_dto import AvailablePackageDetailsDto
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
    api_instance = taikunpycore.PackageApi(api_client)
    repo_name = 'repo_name_example' # str | 
    package_name = 'package_name_example' # str | 
    organization_id = 56 # int |  (optional)

    try:
        # Available helm package details
        api_response = api_instance.package_details(repo_name, package_name, organization_id=organization_id)
        print("The response of PackageApi->package_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageApi->package_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**|  | 
 **package_name** | **str**|  | 
 **organization_id** | **int**|  | [optional] 

### Return type

[**AvailablePackageDetailsDto**](AvailablePackageDetailsDto.md)

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

# **package_list**
> AvailablePackagesList package_list(offset=offset, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id, catalog_id=catalog_id, is_private=is_private, filter_by=filter_by, organization_id=organization_id)

Retrieve all available packages

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.available_packages_list import AvailablePackagesList
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
    api_instance = taikunpycore.PackageApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    catalog_id = 56 # int |  (optional)
    is_private = True # bool |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)
    organization_id = 56 # int |  (optional)

    try:
        # Retrieve all available packages
        api_response = api_instance.package_list(offset=offset, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id, catalog_id=catalog_id, is_private=is_private, filter_by=filter_by, organization_id=organization_id)
        print("The response of PackageApi->package_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageApi->package_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **catalog_id** | **int**|  | [optional] 
 **is_private** | **bool**|  | [optional] 
 **filter_by** | **str**|  | [optional] 
 **organization_id** | **int**|  | [optional] 

### Return type

[**AvailablePackagesList**](AvailablePackagesList.md)

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

# **package_value**
> str package_value(get_catalog_app_value_command)

Get yaml based value

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.get_catalog_app_value_command import GetCatalogAppValueCommand
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
    api_instance = taikunpycore.PackageApi(api_client)
    get_catalog_app_value_command = taikunpycore.GetCatalogAppValueCommand() # GetCatalogAppValueCommand | 

    try:
        # Get yaml based value
        api_response = api_instance.package_value(get_catalog_app_value_command)
        print("The response of PackageApi->package_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageApi->package_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_catalog_app_value_command** | [**GetCatalogAppValueCommand**](GetCatalogAppValueCommand.md)|  | 

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

# **package_value_autocomplete**
> List[PackageAutocompleteDto] package_value_autocomplete(get_catalog_app_value_autocomplete_command)

Get autocomplete dictionary

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.get_catalog_app_value_autocomplete_command import GetCatalogAppValueAutocompleteCommand
from taikunpycore.models.package_autocomplete_dto import PackageAutocompleteDto
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
    api_instance = taikunpycore.PackageApi(api_client)
    get_catalog_app_value_autocomplete_command = taikunpycore.GetCatalogAppValueAutocompleteCommand() # GetCatalogAppValueAutocompleteCommand | 

    try:
        # Get autocomplete dictionary
        api_response = api_instance.package_value_autocomplete(get_catalog_app_value_autocomplete_command)
        print("The response of PackageApi->package_value_autocomplete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageApi->package_value_autocomplete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_catalog_app_value_autocomplete_command** | [**GetCatalogAppValueAutocompleteCommand**](GetCatalogAppValueAutocompleteCommand.md)|  | 

### Return type

[**List[PackageAutocompleteDto]**](PackageAutocompleteDto.md)

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

# **package_versions**
> List[str] package_versions(list_catalog_app_available_versions_command)

Get available versions

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.list_catalog_app_available_versions_command import ListCatalogAppAvailableVersionsCommand
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
    api_instance = taikunpycore.PackageApi(api_client)
    list_catalog_app_available_versions_command = taikunpycore.ListCatalogAppAvailableVersionsCommand() # ListCatalogAppAvailableVersionsCommand | 

    try:
        # Get available versions
        api_response = api_instance.package_versions(list_catalog_app_available_versions_command)
        print("The response of PackageApi->package_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageApi->package_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_catalog_app_available_versions_command** | [**ListCatalogAppAvailableVersionsCommand**](ListCatalogAppAvailableVersionsCommand.md)|  | 

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

