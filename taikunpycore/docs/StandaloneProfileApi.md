# taikunpycore.StandaloneProfileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**standaloneprofile_create**](StandaloneProfileApi.md#standaloneprofile_create) | **POST** /api/v1/standaloneprofile/create | Create standalone profile.
[**standaloneprofile_delete**](StandaloneProfileApi.md#standaloneprofile_delete) | **POST** /api/v1/standaloneprofile/delete | Delete standalone profile.
[**standaloneprofile_dropdown**](StandaloneProfileApi.md#standaloneprofile_dropdown) | **GET** /api/v1/standaloneprofile/list | Retrieve all standalone profiles for organization
[**standaloneprofile_edit**](StandaloneProfileApi.md#standaloneprofile_edit) | **POST** /api/v1/standaloneprofile/edit | Edit standalone profile.
[**standaloneprofile_list**](StandaloneProfileApi.md#standaloneprofile_list) | **GET** /api/v1/standaloneprofile | Retrieve all standalone profiles
[**standaloneprofile_lock_management**](StandaloneProfileApi.md#standaloneprofile_lock_management) | **POST** /api/v1/standaloneprofile/lockmanager | Lock/unlock standalone profile.


# **standaloneprofile_create**
> ApiResponse standaloneprofile_create(stand_alone_profile_create_command=stand_alone_profile_create_command)

Create standalone profile.

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.stand_alone_profile_create_command import StandAloneProfileCreateCommand
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
    api_instance = taikunpycore.StandaloneProfileApi(api_client)
    stand_alone_profile_create_command = taikunpycore.StandAloneProfileCreateCommand() # StandAloneProfileCreateCommand |  (optional)

    try:
        # Create standalone profile.
        api_response = api_instance.standaloneprofile_create(stand_alone_profile_create_command=stand_alone_profile_create_command)
        print("The response of StandaloneProfileApi->standaloneprofile_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneProfileApi->standaloneprofile_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stand_alone_profile_create_command** | [**StandAloneProfileCreateCommand**](StandAloneProfileCreateCommand.md)|  | [optional] 

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

# **standaloneprofile_delete**
> object standaloneprofile_delete(delete_stand_alone_profile_command)

Delete standalone profile.

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_stand_alone_profile_command import DeleteStandAloneProfileCommand
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
    api_instance = taikunpycore.StandaloneProfileApi(api_client)
    delete_stand_alone_profile_command = taikunpycore.DeleteStandAloneProfileCommand() # DeleteStandAloneProfileCommand | 

    try:
        # Delete standalone profile.
        api_response = api_instance.standaloneprofile_delete(delete_stand_alone_profile_command)
        print("The response of StandaloneProfileApi->standaloneprofile_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneProfileApi->standaloneprofile_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_stand_alone_profile_command** | [**DeleteStandAloneProfileCommand**](DeleteStandAloneProfileCommand.md)|  | 

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

# **standaloneprofile_dropdown**
> List[CommonDropdownDto] standaloneprofile_dropdown(organization_id=organization_id, search=search)

Retrieve all standalone profiles for organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_dropdown_dto import CommonDropdownDto
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
    api_instance = taikunpycore.StandaloneProfileApi(api_client)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Retrieve all standalone profiles for organization
        api_response = api_instance.standaloneprofile_dropdown(organization_id=organization_id, search=search)
        print("The response of StandaloneProfileApi->standaloneprofile_dropdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneProfileApi->standaloneprofile_dropdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**List[CommonDropdownDto]**](CommonDropdownDto.md)

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

# **standaloneprofile_edit**
> object standaloneprofile_edit(stand_alone_profile_update_command=stand_alone_profile_update_command)

Edit standalone profile.

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.stand_alone_profile_update_command import StandAloneProfileUpdateCommand
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
    api_instance = taikunpycore.StandaloneProfileApi(api_client)
    stand_alone_profile_update_command = taikunpycore.StandAloneProfileUpdateCommand() # StandAloneProfileUpdateCommand |  (optional)

    try:
        # Edit standalone profile.
        api_response = api_instance.standaloneprofile_edit(stand_alone_profile_update_command=stand_alone_profile_update_command)
        print("The response of StandaloneProfileApi->standaloneprofile_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneProfileApi->standaloneprofile_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stand_alone_profile_update_command** | [**StandAloneProfileUpdateCommand**](StandAloneProfileUpdateCommand.md)|  | [optional] 

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

# **standaloneprofile_list**
> StandAloneProfiles standaloneprofile_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)

Retrieve all standalone profiles

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.stand_alone_profiles import StandAloneProfiles
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
    api_instance = taikunpycore.StandaloneProfileApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve all standalone profiles
        api_response = api_instance.standaloneprofile_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)
        print("The response of StandaloneProfileApi->standaloneprofile_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneProfileApi->standaloneprofile_list: %s\n" % e)
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

[**StandAloneProfiles**](StandAloneProfiles.md)

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

# **standaloneprofile_lock_management**
> object standaloneprofile_lock_management(stand_alone_profile_lock_management_command)

Lock/unlock standalone profile.

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.stand_alone_profile_lock_management_command import StandAloneProfileLockManagementCommand
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
    api_instance = taikunpycore.StandaloneProfileApi(api_client)
    stand_alone_profile_lock_management_command = taikunpycore.StandAloneProfileLockManagementCommand() # StandAloneProfileLockManagementCommand | 

    try:
        # Lock/unlock standalone profile.
        api_response = api_instance.standaloneprofile_lock_management(stand_alone_profile_lock_management_command)
        print("The response of StandaloneProfileApi->standaloneprofile_lock_management:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandaloneProfileApi->standaloneprofile_lock_management: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stand_alone_profile_lock_management_command** | [**StandAloneProfileLockManagementCommand**](StandAloneProfileLockManagementCommand.md)|  | 

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

