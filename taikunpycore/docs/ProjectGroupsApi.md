# taikunpycore.ProjectGroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectgroups_bind_project**](ProjectGroupsApi.md#projectgroups_bind_project) | **POST** /api/v1/projectgroups/bind-project | Bind Projects to group
[**projectgroups_bind_user_group**](ProjectGroupsApi.md#projectgroups_bind_user_group) | **POST** /api/v1/projectgroups/bind-user-group | Bind User groups
[**projectgroups_create**](ProjectGroupsApi.md#projectgroups_create) | **POST** /api/v1/projectgroups/create | Add Project groups
[**projectgroups_delete**](ProjectGroupsApi.md#projectgroups_delete) | **DELETE** /api/v1/projectgroups | Remove Project group(s)
[**projectgroups_list**](ProjectGroupsApi.md#projectgroups_list) | **GET** /api/v1/projectgroups/list | Retrieve list of Project groups
[**projectgroups_list_by_user_id**](ProjectGroupsApi.md#projectgroups_list_by_user_id) | **GET** /api/v1/projectgroups/list/{userGroupId} | Retrieve list of Project groups by user group id for dropdown
[**projectgroups_project_list**](ProjectGroupsApi.md#projectgroups_project_list) | **GET** /api/v1/projectgroups/{projectGroupId}/projects | Retrieve list of projects by project group id
[**projectgroups_unbind_project**](ProjectGroupsApi.md#projectgroups_unbind_project) | **POST** /api/v1/projectgroups/unbind-project | Unbind Projects from group
[**projectgroups_unbind_user_group**](ProjectGroupsApi.md#projectgroups_unbind_user_group) | **POST** /api/v1/projectgroups/unbind-user-group | Unbind user group from project group


# **projectgroups_bind_project**
> object projectgroups_bind_project(bind_projects_to_project_group_command)

Bind Projects to group

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.bind_projects_to_project_group_command import BindProjectsToProjectGroupCommand
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
    api_instance = taikunpycore.ProjectGroupsApi(api_client)
    bind_projects_to_project_group_command = taikunpycore.BindProjectsToProjectGroupCommand() # BindProjectsToProjectGroupCommand | 

    try:
        # Bind Projects to group
        api_response = api_instance.projectgroups_bind_project(bind_projects_to_project_group_command)
        print("The response of ProjectGroupsApi->projectgroups_bind_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectGroupsApi->projectgroups_bind_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bind_projects_to_project_group_command** | [**BindProjectsToProjectGroupCommand**](BindProjectsToProjectGroupCommand.md)|  | 

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

# **projectgroups_bind_user_group**
> object projectgroups_bind_user_group(bind_user_groups_to_project_group_command=bind_user_groups_to_project_group_command)

Bind User groups

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.bind_user_groups_to_project_group_command import BindUserGroupsToProjectGroupCommand
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
    api_instance = taikunpycore.ProjectGroupsApi(api_client)
    bind_user_groups_to_project_group_command = taikunpycore.BindUserGroupsToProjectGroupCommand() # BindUserGroupsToProjectGroupCommand |  (optional)

    try:
        # Bind User groups
        api_response = api_instance.projectgroups_bind_user_group(bind_user_groups_to_project_group_command=bind_user_groups_to_project_group_command)
        print("The response of ProjectGroupsApi->projectgroups_bind_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectGroupsApi->projectgroups_bind_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bind_user_groups_to_project_group_command** | [**BindUserGroupsToProjectGroupCommand**](BindUserGroupsToProjectGroupCommand.md)|  | [optional] 

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

# **projectgroups_create**
> ApiResponse projectgroups_create(create_project_group_command=create_project_group_command)

Add Project groups

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_project_group_command import CreateProjectGroupCommand
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
    api_instance = taikunpycore.ProjectGroupsApi(api_client)
    create_project_group_command = taikunpycore.CreateProjectGroupCommand() # CreateProjectGroupCommand |  (optional)

    try:
        # Add Project groups
        api_response = api_instance.projectgroups_create(create_project_group_command=create_project_group_command)
        print("The response of ProjectGroupsApi->projectgroups_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectGroupsApi->projectgroups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project_group_command** | [**CreateProjectGroupCommand**](CreateProjectGroupCommand.md)|  | [optional] 

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

# **projectgroups_delete**
> projectgroups_delete(request_body=request_body)

Remove Project group(s)

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
    api_instance = taikunpycore.ProjectGroupsApi(api_client)
    request_body = [56] # List[int] |  (optional)

    try:
        # Remove Project group(s)
        api_instance.projectgroups_delete(request_body=request_body)
    except Exception as e:
        print("Exception when calling ProjectGroupsApi->projectgroups_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)|  | [optional] 

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

# **projectgroups_list**
> ProjectGroupList projectgroups_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)

Retrieve list of Project groups

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_group_list import ProjectGroupList
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
    api_instance = taikunpycore.ProjectGroupsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve list of Project groups
        api_response = api_instance.projectgroups_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)
        print("The response of ProjectGroupsApi->projectgroups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectGroupsApi->projectgroups_list: %s\n" % e)
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

[**ProjectGroupList**](ProjectGroupList.md)

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

# **projectgroups_list_by_user_id**
> List[CommonDropdownDto] projectgroups_list_by_user_id(user_group_id)

Retrieve list of Project groups by user group id for dropdown

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
    api_instance = taikunpycore.ProjectGroupsApi(api_client)
    user_group_id = 56 # int | 

    try:
        # Retrieve list of Project groups by user group id for dropdown
        api_response = api_instance.projectgroups_list_by_user_id(user_group_id)
        print("The response of ProjectGroupsApi->projectgroups_list_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectGroupsApi->projectgroups_list_by_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **int**|  | 

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

# **projectgroups_project_list**
> List[CommonDropdownDto] projectgroups_project_list(project_group_id)

Retrieve list of projects by project group id

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
    api_instance = taikunpycore.ProjectGroupsApi(api_client)
    project_group_id = 56 # int | 

    try:
        # Retrieve list of projects by project group id
        api_response = api_instance.projectgroups_project_list(project_group_id)
        print("The response of ProjectGroupsApi->projectgroups_project_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectGroupsApi->projectgroups_project_list: %s\n" % e)
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

# **projectgroups_unbind_project**
> object projectgroups_unbind_project(unbind_project_from_project_group_command=unbind_project_from_project_group_command)

Unbind Projects from group

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.unbind_project_from_project_group_command import UnbindProjectFromProjectGroupCommand
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
    api_instance = taikunpycore.ProjectGroupsApi(api_client)
    unbind_project_from_project_group_command = taikunpycore.UnbindProjectFromProjectGroupCommand() # UnbindProjectFromProjectGroupCommand |  (optional)

    try:
        # Unbind Projects from group
        api_response = api_instance.projectgroups_unbind_project(unbind_project_from_project_group_command=unbind_project_from_project_group_command)
        print("The response of ProjectGroupsApi->projectgroups_unbind_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectGroupsApi->projectgroups_unbind_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unbind_project_from_project_group_command** | [**UnbindProjectFromProjectGroupCommand**](UnbindProjectFromProjectGroupCommand.md)|  | [optional] 

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

# **projectgroups_unbind_user_group**
> object projectgroups_unbind_user_group(unbind_user_group_from_project_group_command)

Unbind user group from project group

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.unbind_user_group_from_project_group_command import UnbindUserGroupFromProjectGroupCommand
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
    api_instance = taikunpycore.ProjectGroupsApi(api_client)
    unbind_user_group_from_project_group_command = taikunpycore.UnbindUserGroupFromProjectGroupCommand() # UnbindUserGroupFromProjectGroupCommand | 

    try:
        # Unbind user group from project group
        api_response = api_instance.projectgroups_unbind_user_group(unbind_user_group_from_project_group_command)
        print("The response of ProjectGroupsApi->projectgroups_unbind_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectGroupsApi->projectgroups_unbind_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unbind_user_group_from_project_group_command** | [**UnbindUserGroupFromProjectGroupCommand**](UnbindUserGroupFromProjectGroupCommand.md)|  | 

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

