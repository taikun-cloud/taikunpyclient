# taikunpycore.CatalogAppApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_app_create**](CatalogAppApi.md#catalog_app_create) | **POST** /api/v1/catalog-app/create | Create catalog app
[**catalog_app_delete**](CatalogAppApi.md#catalog_app_delete) | **DELETE** /api/v1/catalog-app/{id} | Delete catalog app
[**catalog_app_details**](CatalogAppApi.md#catalog_app_details) | **GET** /api/v1/catalog-app/{catalogAppId} | Catalog App details
[**catalog_app_edit_params**](CatalogAppApi.md#catalog_app_edit_params) | **PUT** /api/v1/catalog-app/edit/params | Edit catalog app params
[**catalog_app_edit_version**](CatalogAppApi.md#catalog_app_edit_version) | **PUT** /api/v1/catalog-app/edit/version | Edit catalog app version
[**catalog_app_list**](CatalogAppApi.md#catalog_app_list) | **GET** /api/v1/catalog-app/list | Catalog App list
[**catalog_app_lock_manager**](CatalogAppApi.md#catalog_app_lock_manager) | **POST** /api/v1/catalog-app/lockmanager | Lock catalog app
[**catalog_app_param_details**](CatalogAppApi.md#catalog_app_param_details) | **GET** /api/v1/catalog-app/params/{catalogAppId} | Catalog App param details


# **catalog_app_create**
> CatalogAppDetailsDto catalog_app_create(create_catalog_app_command=create_catalog_app_command)

Create catalog app

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.catalog_app_details_dto import CatalogAppDetailsDto
from taikunpycore.models.create_catalog_app_command import CreateCatalogAppCommand
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
    api_instance = taikunpycore.CatalogAppApi(api_client)
    create_catalog_app_command = taikunpycore.CreateCatalogAppCommand() # CreateCatalogAppCommand |  (optional)

    try:
        # Create catalog app
        api_response = api_instance.catalog_app_create(create_catalog_app_command=create_catalog_app_command)
        print("The response of CatalogAppApi->catalog_app_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogAppApi->catalog_app_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_catalog_app_command** | [**CreateCatalogAppCommand**](CreateCatalogAppCommand.md)|  | [optional] 

### Return type

[**CatalogAppDetailsDto**](CatalogAppDetailsDto.md)

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

# **catalog_app_delete**
> catalog_app_delete(id)

Delete catalog app

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
    api_instance = taikunpycore.CatalogAppApi(api_client)
    id = 56 # int | 

    try:
        # Delete catalog app
        api_instance.catalog_app_delete(id)
    except Exception as e:
        print("Exception when calling CatalogAppApi->catalog_app_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

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

# **catalog_app_details**
> CatalogAppDetailsDto catalog_app_details(catalog_app_id)

Catalog App details

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.catalog_app_details_dto import CatalogAppDetailsDto
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
    api_instance = taikunpycore.CatalogAppApi(api_client)
    catalog_app_id = 56 # int | 

    try:
        # Catalog App details
        api_response = api_instance.catalog_app_details(catalog_app_id)
        print("The response of CatalogAppApi->catalog_app_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogAppApi->catalog_app_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_app_id** | **int**|  | 

### Return type

[**CatalogAppDetailsDto**](CatalogAppDetailsDto.md)

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

# **catalog_app_edit_params**
> object catalog_app_edit_params(edit_catalog_app_param_command=edit_catalog_app_param_command)

Edit catalog app params

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.edit_catalog_app_param_command import EditCatalogAppParamCommand
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
    api_instance = taikunpycore.CatalogAppApi(api_client)
    edit_catalog_app_param_command = taikunpycore.EditCatalogAppParamCommand() # EditCatalogAppParamCommand |  (optional)

    try:
        # Edit catalog app params
        api_response = api_instance.catalog_app_edit_params(edit_catalog_app_param_command=edit_catalog_app_param_command)
        print("The response of CatalogAppApi->catalog_app_edit_params:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogAppApi->catalog_app_edit_params: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_catalog_app_param_command** | [**EditCatalogAppParamCommand**](EditCatalogAppParamCommand.md)|  | [optional] 

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

# **catalog_app_edit_version**
> object catalog_app_edit_version(edit_catalog_app_version_command)

Edit catalog app version

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.edit_catalog_app_version_command import EditCatalogAppVersionCommand
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
    api_instance = taikunpycore.CatalogAppApi(api_client)
    edit_catalog_app_version_command = taikunpycore.EditCatalogAppVersionCommand() # EditCatalogAppVersionCommand | 

    try:
        # Edit catalog app version
        api_response = api_instance.catalog_app_edit_version(edit_catalog_app_version_command)
        print("The response of CatalogAppApi->catalog_app_edit_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogAppApi->catalog_app_edit_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_catalog_app_version_command** | [**EditCatalogAppVersionCommand**](EditCatalogAppVersionCommand.md)|  | 

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

# **catalog_app_list**
> CatalogAppList catalog_app_list(organization_id=organization_id, catalog_id=catalog_id, search=search, sort_by=sort_by, sort_direction=sort_direction, offset=offset, limit=limit)

Catalog App list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.catalog_app_list import CatalogAppList
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
    api_instance = taikunpycore.CatalogAppApi(api_client)
    organization_id = 56 # int |  (optional)
    catalog_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # Catalog App list
        api_response = api_instance.catalog_app_list(organization_id=organization_id, catalog_id=catalog_id, search=search, sort_by=sort_by, sort_direction=sort_direction, offset=offset, limit=limit)
        print("The response of CatalogAppApi->catalog_app_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogAppApi->catalog_app_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **catalog_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**CatalogAppList**](CatalogAppList.md)

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

# **catalog_app_lock_manager**
> object catalog_app_lock_manager(catalog_app_lock_management)

Lock catalog app

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.catalog_app_lock_management import CatalogAppLockManagement
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
    api_instance = taikunpycore.CatalogAppApi(api_client)
    catalog_app_lock_management = taikunpycore.CatalogAppLockManagement() # CatalogAppLockManagement | 

    try:
        # Lock catalog app
        api_response = api_instance.catalog_app_lock_manager(catalog_app_lock_management)
        print("The response of CatalogAppApi->catalog_app_lock_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogAppApi->catalog_app_lock_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_app_lock_management** | [**CatalogAppLockManagement**](CatalogAppLockManagement.md)|  | 

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

# **catalog_app_param_details**
> List[CatalogAppParamsDetailsDto] catalog_app_param_details(catalog_app_id)

Catalog App param details

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.catalog_app_params_details_dto import CatalogAppParamsDetailsDto
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
    api_instance = taikunpycore.CatalogAppApi(api_client)
    catalog_app_id = 56 # int | 

    try:
        # Catalog App param details
        api_response = api_instance.catalog_app_param_details(catalog_app_id)
        print("The response of CatalogAppApi->catalog_app_param_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogAppApi->catalog_app_param_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_app_id** | **int**|  | 

### Return type

[**List[CatalogAppParamsDetailsDto]**](CatalogAppParamsDetailsDto.md)

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

