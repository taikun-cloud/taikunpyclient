# taikunpycore.OpaProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**opaprofiles_create**](OpaProfilesApi.md#opaprofiles_create) | **POST** /api/v1/opaprofiles/create | Add policy profile
[**opaprofiles_delete**](OpaProfilesApi.md#opaprofiles_delete) | **DELETE** /api/v1/opaprofiles/{id} | Remove Opa profile by Id
[**opaprofiles_dropdown**](OpaProfilesApi.md#opaprofiles_dropdown) | **GET** /api/v1/opaprofiles/list | Retrieve policy profiles for organization
[**opaprofiles_list**](OpaProfilesApi.md#opaprofiles_list) | **GET** /api/v1/opaprofiles | Retrieve all policy profiles
[**opaprofiles_lock_manager**](OpaProfilesApi.md#opaprofiles_lock_manager) | **POST** /api/v1/opaprofiles/lockmanager | Lock/Unlock policy profile
[**opaprofiles_make_default**](OpaProfilesApi.md#opaprofiles_make_default) | **POST** /api/v1/opaprofiles/make-default | Choose default policy profile
[**opaprofiles_sync**](OpaProfilesApi.md#opaprofiles_sync) | **POST** /api/v1/opaprofiles/sync | Sync policy profile
[**opaprofiles_update**](OpaProfilesApi.md#opaprofiles_update) | **PUT** /api/v1/opaprofiles | Update policy profile


# **opaprofiles_create**
> ApiResponse opaprofiles_create(create_opa_profile_command)

Add policy profile

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_opa_profile_command import CreateOpaProfileCommand
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
    api_instance = taikunpycore.OpaProfilesApi(api_client)
    create_opa_profile_command = taikunpycore.CreateOpaProfileCommand() # CreateOpaProfileCommand | 

    try:
        # Add policy profile
        api_response = api_instance.opaprofiles_create(create_opa_profile_command)
        print("The response of OpaProfilesApi->opaprofiles_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpaProfilesApi->opaprofiles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_opa_profile_command** | [**CreateOpaProfileCommand**](CreateOpaProfileCommand.md)|  | 

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

# **opaprofiles_delete**
> opaprofiles_delete(id)

Remove Opa profile by Id

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
    api_instance = taikunpycore.OpaProfilesApi(api_client)
    id = 56 # int | 

    try:
        # Remove Opa profile by Id
        api_instance.opaprofiles_delete(id)
    except Exception as e:
        print("Exception when calling OpaProfilesApi->opaprofiles_delete: %s\n" % e)
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

# **opaprofiles_dropdown**
> List[CommonExtendedDropdownDto] opaprofiles_dropdown(organization_id=organization_id, search=search)

Retrieve policy profiles for organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_extended_dropdown_dto import CommonExtendedDropdownDto
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
    api_instance = taikunpycore.OpaProfilesApi(api_client)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Retrieve policy profiles for organization
        api_response = api_instance.opaprofiles_dropdown(organization_id=organization_id, search=search)
        print("The response of OpaProfilesApi->opaprofiles_dropdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpaProfilesApi->opaprofiles_dropdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**List[CommonExtendedDropdownDto]**](CommonExtendedDropdownDto.md)

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

# **opaprofiles_list**
> OpaProfileList opaprofiles_list(organization_id=organization_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id, search_id=search_id)

Retrieve all policy profiles

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.opa_profile_list import OpaProfileList
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
    api_instance = taikunpycore.OpaProfilesApi(api_client)
    organization_id = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    id = 56 # int |  (optional)
    search_id = 'search_id_example' # str |  (optional)

    try:
        # Retrieve all policy profiles
        api_response = api_instance.opaprofiles_list(organization_id=organization_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id, search_id=search_id)
        print("The response of OpaProfilesApi->opaprofiles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpaProfilesApi->opaprofiles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **search_id** | **str**|  | [optional] 

### Return type

[**OpaProfileList**](OpaProfileList.md)

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

# **opaprofiles_lock_manager**
> object opaprofiles_lock_manager(opa_profile_lock_manager_command)

Lock/Unlock policy profile

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.opa_profile_lock_manager_command import OpaProfileLockManagerCommand
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
    api_instance = taikunpycore.OpaProfilesApi(api_client)
    opa_profile_lock_manager_command = taikunpycore.OpaProfileLockManagerCommand() # OpaProfileLockManagerCommand | 

    try:
        # Lock/Unlock policy profile
        api_response = api_instance.opaprofiles_lock_manager(opa_profile_lock_manager_command)
        print("The response of OpaProfilesApi->opaprofiles_lock_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpaProfilesApi->opaprofiles_lock_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opa_profile_lock_manager_command** | [**OpaProfileLockManagerCommand**](OpaProfileLockManagerCommand.md)|  | 

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

# **opaprofiles_make_default**
> object opaprofiles_make_default(opa_make_default_command)

Choose default policy profile

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.opa_make_default_command import OpaMakeDefaultCommand
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
    api_instance = taikunpycore.OpaProfilesApi(api_client)
    opa_make_default_command = taikunpycore.OpaMakeDefaultCommand() # OpaMakeDefaultCommand | 

    try:
        # Choose default policy profile
        api_response = api_instance.opaprofiles_make_default(opa_make_default_command)
        print("The response of OpaProfilesApi->opaprofiles_make_default:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpaProfilesApi->opaprofiles_make_default: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opa_make_default_command** | [**OpaMakeDefaultCommand**](OpaMakeDefaultCommand.md)|  | 

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

# **opaprofiles_sync**
> object opaprofiles_sync(opa_profile_sync_command)

Sync policy profile

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.opa_profile_sync_command import OpaProfileSyncCommand
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
    api_instance = taikunpycore.OpaProfilesApi(api_client)
    opa_profile_sync_command = taikunpycore.OpaProfileSyncCommand() # OpaProfileSyncCommand | 

    try:
        # Sync policy profile
        api_response = api_instance.opaprofiles_sync(opa_profile_sync_command)
        print("The response of OpaProfilesApi->opaprofiles_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpaProfilesApi->opaprofiles_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opa_profile_sync_command** | [**OpaProfileSyncCommand**](OpaProfileSyncCommand.md)|  | 

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

# **opaprofiles_update**
> object opaprofiles_update(opa_profile_update_command=opa_profile_update_command)

Update policy profile

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.opa_profile_update_command import OpaProfileUpdateCommand
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
    api_instance = taikunpycore.OpaProfilesApi(api_client)
    opa_profile_update_command = taikunpycore.OpaProfileUpdateCommand() # OpaProfileUpdateCommand |  (optional)

    try:
        # Update policy profile
        api_response = api_instance.opaprofiles_update(opa_profile_update_command=opa_profile_update_command)
        print("The response of OpaProfilesApi->opaprofiles_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpaProfilesApi->opaprofiles_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opa_profile_update_command** | [**OpaProfileUpdateCommand**](OpaProfileUpdateCommand.md)|  | [optional] 

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

