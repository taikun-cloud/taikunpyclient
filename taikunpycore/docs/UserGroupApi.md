# taikunpycore.UserGroupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectgroups_unbind_project_group**](UserGroupApi.md#projectgroups_unbind_project_group) | **POST** /api/v1/projectgroups/unbind-project-group | Unbind project group from user group
[**usergroups_bind_projects_group**](UserGroupApi.md#usergroups_bind_projects_group) | **POST** /api/v1/usergroups/bind-project-groups | Bind project groups
[**usergroups_bind_user**](UserGroupApi.md#usergroups_bind_user) | **POST** /api/v1/usergroups/bind-user | Bind Users to group
[**usergroups_create**](UserGroupApi.md#usergroups_create) | **POST** /api/v1/usergroups/create | Add user groups
[**usergroups_delete**](UserGroupApi.md#usergroups_delete) | **DELETE** /api/v1/usergroups | Remove user group(s)
[**usergroups_list**](UserGroupApi.md#usergroups_list) | **GET** /api/v1/usergroups/list | Retrieve list of user groups
[**usergroups_list_by_project_group_id**](UserGroupApi.md#usergroups_list_by_project_group_id) | **GET** /api/v1/usergroups/list/{projectGroupId} | Dropdown list
[**usergroups_unbind_user**](UserGroupApi.md#usergroups_unbind_user) | **POST** /api/v1/usergroups/unbind-user | Unbind Users from group
[**usergroups_update**](UserGroupApi.md#usergroups_update) | **PUT** /api/v1/usergroups/update/{userGroupId} | Update user groups
[**usergroups_user_group_users**](UserGroupApi.md#usergroups_user_group_users) | **GET** /api/v1/usergroups/{userGroupId}/users | Retrieve list of users by user group id


# **projectgroups_unbind_project_group**
> object projectgroups_unbind_project_group(unbind_project_group_from_user_group_command)

Unbind project group from user group

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.unbind_project_group_from_user_group_command import UnbindProjectGroupFromUserGroupCommand
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
    api_instance = taikunpycore.UserGroupApi(api_client)
    unbind_project_group_from_user_group_command = taikunpycore.UnbindProjectGroupFromUserGroupCommand() # UnbindProjectGroupFromUserGroupCommand | 

    try:
        # Unbind project group from user group
        api_response = api_instance.projectgroups_unbind_project_group(unbind_project_group_from_user_group_command)
        print("The response of UserGroupApi->projectgroups_unbind_project_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->projectgroups_unbind_project_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unbind_project_group_from_user_group_command** | [**UnbindProjectGroupFromUserGroupCommand**](UnbindProjectGroupFromUserGroupCommand.md)|  | 

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

# **usergroups_bind_projects_group**
> object usergroups_bind_projects_group(bind_project_groups_to_user_group_command=bind_project_groups_to_user_group_command)

Bind project groups

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.bind_project_groups_to_user_group_command import BindProjectGroupsToUserGroupCommand
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
    api_instance = taikunpycore.UserGroupApi(api_client)
    bind_project_groups_to_user_group_command = taikunpycore.BindProjectGroupsToUserGroupCommand() # BindProjectGroupsToUserGroupCommand |  (optional)

    try:
        # Bind project groups
        api_response = api_instance.usergroups_bind_projects_group(bind_project_groups_to_user_group_command=bind_project_groups_to_user_group_command)
        print("The response of UserGroupApi->usergroups_bind_projects_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->usergroups_bind_projects_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bind_project_groups_to_user_group_command** | [**BindProjectGroupsToUserGroupCommand**](BindProjectGroupsToUserGroupCommand.md)|  | [optional] 

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

# **usergroups_bind_user**
> object usergroups_bind_user(bind_users_to_user_group_command)

Bind Users to group

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.bind_users_to_user_group_command import BindUsersToUserGroupCommand
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
    api_instance = taikunpycore.UserGroupApi(api_client)
    bind_users_to_user_group_command = taikunpycore.BindUsersToUserGroupCommand() # BindUsersToUserGroupCommand | 

    try:
        # Bind Users to group
        api_response = api_instance.usergroups_bind_user(bind_users_to_user_group_command)
        print("The response of UserGroupApi->usergroups_bind_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->usergroups_bind_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bind_users_to_user_group_command** | [**BindUsersToUserGroupCommand**](BindUsersToUserGroupCommand.md)|  | 

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

# **usergroups_create**
> ApiResponse usergroups_create(create_user_group_command=create_user_group_command)

Add user groups

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_user_group_command import CreateUserGroupCommand
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
    api_instance = taikunpycore.UserGroupApi(api_client)
    create_user_group_command = taikunpycore.CreateUserGroupCommand() # CreateUserGroupCommand |  (optional)

    try:
        # Add user groups
        api_response = api_instance.usergroups_create(create_user_group_command=create_user_group_command)
        print("The response of UserGroupApi->usergroups_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->usergroups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_group_command** | [**CreateUserGroupCommand**](CreateUserGroupCommand.md)|  | [optional] 

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

# **usergroups_delete**
> usergroups_delete(delete_user_group_command)

Remove user group(s)

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_user_group_command import DeleteUserGroupCommand
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
    api_instance = taikunpycore.UserGroupApi(api_client)
    delete_user_group_command = taikunpycore.DeleteUserGroupCommand() # DeleteUserGroupCommand | 

    try:
        # Remove user group(s)
        api_instance.usergroups_delete(delete_user_group_command)
    except Exception as e:
        print("Exception when calling UserGroupApi->usergroups_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_user_group_command** | [**DeleteUserGroupCommand**](DeleteUserGroupCommand.md)|  | 

### Return type

void (empty response body)

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

# **usergroups_list**
> UserGroupList usergroups_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)

Retrieve list of user groups

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.user_group_list import UserGroupList
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
    api_instance = taikunpycore.UserGroupApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve list of user groups
        api_response = api_instance.usergroups_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)
        print("The response of UserGroupApi->usergroups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->usergroups_list: %s\n" % e)
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

[**UserGroupList**](UserGroupList.md)

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

# **usergroups_list_by_project_group_id**
> List[CommonDropdownDto] usergroups_list_by_project_group_id(project_group_id)

Dropdown list

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
    api_instance = taikunpycore.UserGroupApi(api_client)
    project_group_id = 56 # int | 

    try:
        # Dropdown list
        api_response = api_instance.usergroups_list_by_project_group_id(project_group_id)
        print("The response of UserGroupApi->usergroups_list_by_project_group_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->usergroups_list_by_project_group_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_group_id** | **int**|  | 

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

# **usergroups_unbind_user**
> object usergroups_unbind_user(unbind_user_from_user_group_command=unbind_user_from_user_group_command)

Unbind Users from group

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.unbind_user_from_user_group_command import UnbindUserFromUserGroupCommand
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
    api_instance = taikunpycore.UserGroupApi(api_client)
    unbind_user_from_user_group_command = taikunpycore.UnbindUserFromUserGroupCommand() # UnbindUserFromUserGroupCommand |  (optional)

    try:
        # Unbind Users from group
        api_response = api_instance.usergroups_unbind_user(unbind_user_from_user_group_command=unbind_user_from_user_group_command)
        print("The response of UserGroupApi->usergroups_unbind_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->usergroups_unbind_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unbind_user_from_user_group_command** | [**UnbindUserFromUserGroupCommand**](UnbindUserFromUserGroupCommand.md)|  | [optional] 

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

# **usergroups_update**
> object usergroups_update(user_group_id, update_user_group_dto=update_user_group_dto)

Update user groups

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_user_group_dto import UpdateUserGroupDto
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
    api_instance = taikunpycore.UserGroupApi(api_client)
    user_group_id = 56 # int | 
    update_user_group_dto = taikunpycore.UpdateUserGroupDto() # UpdateUserGroupDto |  (optional)

    try:
        # Update user groups
        api_response = api_instance.usergroups_update(user_group_id, update_user_group_dto=update_user_group_dto)
        print("The response of UserGroupApi->usergroups_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->usergroups_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **int**|  | 
 **update_user_group_dto** | [**UpdateUserGroupDto**](UpdateUserGroupDto.md)|  | [optional] 

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

# **usergroups_user_group_users**
> List[CommonStringBasedDropdownDto] usergroups_user_group_users(user_group_id)

Retrieve list of users by user group id

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
    api_instance = taikunpycore.UserGroupApi(api_client)
    user_group_id = 56 # int | 

    try:
        # Retrieve list of users by user group id
        api_response = api_instance.usergroups_user_group_users(user_group_id)
        print("The response of UserGroupApi->usergroups_user_group_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->usergroups_user_group_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **int**|  | 

### Return type

[**List[CommonStringBasedDropdownDto]**](CommonStringBasedDropdownDto.md)

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

