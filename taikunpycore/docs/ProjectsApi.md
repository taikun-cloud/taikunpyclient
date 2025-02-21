# taikunpycore.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_add_project_users**](ProjectsApi.md#projects_add_project_users) | **POST** /api/v1/projects/{id}/users | Add users to project
[**projects_ai_analyzer**](ProjectsApi.md#projects_ai_analyzer) | **GET** /api/v1/projects/ai-analyze/{projectId} | Analyze cluster by AI model
[**projects_alerts**](ProjectsApi.md#projects_alerts) | **POST** /api/v1/projects/alerts | Project alerts
[**projects_can_add_vcluster**](ProjectsApi.md#projects_can_add_vcluster) | **GET** /api/v1/projects/can-add-vcluster/{projectId} | Visibility of adding vcluster
[**projects_chat_completions**](ProjectsApi.md#projects_chat_completions) | **POST** /api/v1/projects/chat/completions | AI Chat completions
[**projects_create**](ProjectsApi.md#projects_create) | **POST** /api/v1/projects | Create a new project
[**projects_delete**](ProjectsApi.md#projects_delete) | **POST** /api/v1/projects/delete | Delete the project. The project must be empty (no server) and in READY state
[**projects_delete_project_users**](ProjectsApi.md#projects_delete_project_users) | **PUT** /api/v1/projects/{id}/users | Delete users from project
[**projects_describe**](ProjectsApi.md#projects_describe) | **GET** /api/v1/projects/describe/{projectId} | Describe project by Id
[**projects_dropdown**](ProjectsApi.md#projects_dropdown) | **GET** /api/v1/projects/list | Retrieve list of projects for dropdown
[**projects_edit_health**](ProjectsApi.md#projects_edit_health) | **PUT** /api/v1/projects/edit/health | Update health status of the project by Id
[**projects_edit_status**](ProjectsApi.md#projects_edit_status) | **PUT** /api/v1/projects/edit/status | Change the project status for the given project. Only available for admin.
[**projects_extend_lifetime**](ProjectsApi.md#projects_extend_lifetime) | **POST** /api/v1/projects/extend/lifetime | Extend life time of project
[**projects_for_alerting**](ProjectsApi.md#projects_for_alerting) | **GET** /api/v1/projects/foralerting | Retrieve a list of projects for alert poller. Only available for admins.
[**projects_for_billing**](ProjectsApi.md#projects_for_billing) | **GET** /api/v1/projects/forbilling | Retrieve a list of projects for billing
[**projects_imported_cluster_details**](ProjectsApi.md#projects_imported_cluster_details) | **GET** /api/v1/projects/imported/details/{projectId} | Imported cluster details
[**projects_list**](ProjectsApi.md#projects_list) | **GET** /api/v1/projects | Retrieve all projects
[**projects_lock_manager**](ProjectsApi.md#projects_lock_manager) | **POST** /api/v1/projects/lockmanager | Lock/Unlock project
[**projects_loki_logs**](ProjectsApi.md#projects_loki_logs) | **POST** /api/v1/projects/lokilogs | Retrieve loki logs
[**projects_maintenance_manager**](ProjectsApi.md#projects_maintenance_manager) | **POST** /api/v1/projects/maintenance-manager | Enable/disable project&#39;s maintenance mode
[**projects_monitoring_alerts**](ProjectsApi.md#projects_monitoring_alerts) | **POST** /api/v1/projects/monitoringalerts | Monitoring alerts for project
[**projects_prometheus_metrics**](ProjectsApi.md#projects_prometheus_metrics) | **POST** /api/v1/projects/prometheusmetrics | Prometheus metrics data project
[**projects_prometheus_metrics_autocomplete**](ProjectsApi.md#projects_prometheus_metrics_autocomplete) | **POST** /api/v1/projects/prometheusmetrics/autocomplete | Prometheus metrics autocomplete values
[**projects_toggle_full_spot**](ProjectsApi.md#projects_toggle_full_spot) | **POST** /api/v1/projects/toggle-full-spot | Full spot operations enable/disable
[**projects_toggle_spot_vms**](ProjectsApi.md#projects_toggle_spot_vms) | **POST** /api/v1/projects/toggle-spot-vms | Spot vm(s) operations enable/disable
[**projects_toggle_spot_workers**](ProjectsApi.md#projects_toggle_spot_workers) | **POST** /api/v1/projects/toggle-spot-workers | Spot worker(s) operations enable/disable
[**projects_visibility**](ProjectsApi.md#projects_visibility) | **GET** /api/v1/projects/visibility/{projectId} | Visibility of project actions


# **projects_add_project_users**
> object projects_add_project_users(id, request_body=request_body)

Add users to project

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
    api_instance = taikunpycore.ProjectsApi(api_client)
    id = 56 # int | 
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Add users to project
        api_response = api_instance.projects_add_project_users(id, request_body=request_body)
        print("The response of ProjectsApi->projects_add_project_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_add_project_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

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

# **projects_ai_analyzer**
> AiListDto projects_ai_analyzer(project_id)

Analyze cluster by AI model

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.ai_list_dto import AiListDto
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    project_id = 56 # int | 

    try:
        # Analyze cluster by AI model
        api_response = api_instance.projects_ai_analyzer(project_id)
        print("The response of ProjectsApi->projects_ai_analyzer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_ai_analyzer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**AiListDto**](AiListDto.md)

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

# **projects_alerts**
> List[ProjectDetailsErrorListDto] projects_alerts(project_alerts_query)

Project alerts

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_alerts_query import ProjectAlertsQuery
from taikunpycore.models.project_details_error_list_dto import ProjectDetailsErrorListDto
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    project_alerts_query = taikunpycore.ProjectAlertsQuery() # ProjectAlertsQuery | 

    try:
        # Project alerts
        api_response = api_instance.projects_alerts(project_alerts_query)
        print("The response of ProjectsApi->projects_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_alerts_query** | [**ProjectAlertsQuery**](ProjectAlertsQuery.md)|  | 

### Return type

[**List[ProjectDetailsErrorListDto]**](ProjectDetailsErrorListDto.md)

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

# **projects_can_add_vcluster**
> ProjectCanAddVClusterDto projects_can_add_vcluster(project_id)

Visibility of adding vcluster

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_can_add_v_cluster_dto import ProjectCanAddVClusterDto
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    project_id = 56 # int | 

    try:
        # Visibility of adding vcluster
        api_response = api_instance.projects_can_add_vcluster(project_id)
        print("The response of ProjectsApi->projects_can_add_vcluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_can_add_vcluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**ProjectCanAddVClusterDto**](ProjectCanAddVClusterDto.md)

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

# **projects_chat_completions**
> object projects_chat_completions(chat_completions_command)

AI Chat completions

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.chat_completions_command import ChatCompletionsCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    chat_completions_command = taikunpycore.ChatCompletionsCommand() # ChatCompletionsCommand | 

    try:
        # AI Chat completions
        api_response = api_instance.projects_chat_completions(chat_completions_command)
        print("The response of ProjectsApi->projects_chat_completions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_chat_completions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_completions_command** | [**ChatCompletionsCommand**](ChatCompletionsCommand.md)|  | 

### Return type

**object**

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

# **projects_create**
> ApiResponse projects_create(create_project_command=create_project_command)

Create a new project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_project_command import CreateProjectCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    create_project_command = taikunpycore.CreateProjectCommand() # CreateProjectCommand |  (optional)

    try:
        # Create a new project
        api_response = api_instance.projects_create(create_project_command=create_project_command)
        print("The response of ProjectsApi->projects_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project_command** | [**CreateProjectCommand**](CreateProjectCommand.md)|  | [optional] 

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

# **projects_delete**
> projects_delete(delete_project_command)

Delete the project. The project must be empty (no server) and in READY state

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_project_command import DeleteProjectCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    delete_project_command = taikunpycore.DeleteProjectCommand() # DeleteProjectCommand | 

    try:
        # Delete the project. The project must be empty (no server) and in READY state
        api_instance.projects_delete(delete_project_command)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_project_command** | [**DeleteProjectCommand**](DeleteProjectCommand.md)|  | 

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

# **projects_delete_project_users**
> object projects_delete_project_users(id, request_body=request_body)

Delete users from project

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
    api_instance = taikunpycore.ProjectsApi(api_client)
    id = 56 # int | 
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Delete users from project
        api_response = api_instance.projects_delete_project_users(id, request_body=request_body)
        print("The response of ProjectsApi->projects_delete_project_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_delete_project_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

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

# **projects_describe**
> object projects_describe(project_id, is_yaml)

Describe project by Id

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
    api_instance = taikunpycore.ProjectsApi(api_client)
    project_id = 56 # int | 
    is_yaml = True # bool | 

    try:
        # Describe project by Id
        api_response = api_instance.projects_describe(project_id, is_yaml)
        print("The response of ProjectsApi->projects_describe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_describe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **is_yaml** | **bool**|  | 

### Return type

**object**

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

# **projects_dropdown**
> List[CommonDropdownIsBoundDtoForProject] projects_dropdown(organization_id=organization_id, search=search, catalog_id=catalog_id, healthy=healthy, user_id=user_id, ready=ready, is_bound_to_catalog=is_bound_to_catalog)

Retrieve list of projects for dropdown

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_dropdown_is_bound_dto_for_project import CommonDropdownIsBoundDtoForProject
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    catalog_id = 56 # int |  (optional)
    healthy = True # bool |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    ready = True # bool |  (optional)
    is_bound_to_catalog = True # bool |  (optional)

    try:
        # Retrieve list of projects for dropdown
        api_response = api_instance.projects_dropdown(organization_id=organization_id, search=search, catalog_id=catalog_id, healthy=healthy, user_id=user_id, ready=ready, is_bound_to_catalog=is_bound_to_catalog)
        print("The response of ProjectsApi->projects_dropdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_dropdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **catalog_id** | **int**|  | [optional] 
 **healthy** | **bool**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **ready** | **bool**|  | [optional] 
 **is_bound_to_catalog** | **bool**|  | [optional] 

### Return type

[**List[CommonDropdownIsBoundDtoForProject]**](CommonDropdownIsBoundDtoForProject.md)

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

# **projects_edit_health**
> object projects_edit_health(update_health_status_command=update_health_status_command)

Update health status of the project by Id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_health_status_command import UpdateHealthStatusCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    update_health_status_command = taikunpycore.UpdateHealthStatusCommand() # UpdateHealthStatusCommand |  (optional)

    try:
        # Update health status of the project by Id
        api_response = api_instance.projects_edit_health(update_health_status_command=update_health_status_command)
        print("The response of ProjectsApi->projects_edit_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_edit_health: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_health_status_command** | [**UpdateHealthStatusCommand**](UpdateHealthStatusCommand.md)|  | [optional] 

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

# **projects_edit_status**
> object projects_edit_status(reset_project_status_command)

Change the project status for the given project. Only available for admin.

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.reset_project_status_command import ResetProjectStatusCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    reset_project_status_command = taikunpycore.ResetProjectStatusCommand() # ResetProjectStatusCommand | 

    try:
        # Change the project status for the given project. Only available for admin.
        api_response = api_instance.projects_edit_status(reset_project_status_command)
        print("The response of ProjectsApi->projects_edit_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_edit_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_project_status_command** | [**ResetProjectStatusCommand**](ResetProjectStatusCommand.md)|  | 

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

# **projects_extend_lifetime**
> object projects_extend_lifetime(project_extend_life_time_command)

Extend life time of project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_extend_life_time_command import ProjectExtendLifeTimeCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    project_extend_life_time_command = taikunpycore.ProjectExtendLifeTimeCommand() # ProjectExtendLifeTimeCommand | 

    try:
        # Extend life time of project
        api_response = api_instance.projects_extend_lifetime(project_extend_life_time_command)
        print("The response of ProjectsApi->projects_extend_lifetime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_extend_lifetime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_extend_life_time_command** | [**ProjectExtendLifeTimeCommand**](ProjectExtendLifeTimeCommand.md)|  | 

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

# **projects_for_alerting**
> List[ProjectListForAlert] projects_for_alerting(limit=limit, offset=offset, status=status, project_id=project_id)

Retrieve a list of projects for alert poller. Only available for admins.

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_list_for_alert import ProjectListForAlert
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    status = 'status_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve a list of projects for alert poller. Only available for admins.
        api_response = api_instance.projects_for_alerting(limit=limit, offset=offset, status=status, project_id=project_id)
        print("The response of ProjectsApi->projects_for_alerting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_for_alerting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **status** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**List[ProjectListForAlert]**](ProjectListForAlert.md)

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

# **projects_for_billing**
> List[ProjectsForBillingDto] projects_for_billing()

Retrieve a list of projects for billing

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.projects_for_billing_dto import ProjectsForBillingDto
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
    api_instance = taikunpycore.ProjectsApi(api_client)

    try:
        # Retrieve a list of projects for billing
        api_response = api_instance.projects_for_billing()
        print("The response of ProjectsApi->projects_for_billing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_for_billing: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ProjectsForBillingDto]**](ProjectsForBillingDto.md)

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

# **projects_imported_cluster_details**
> ImportedClusterDetailsDto projects_imported_cluster_details(project_id)

Imported cluster details

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.imported_cluster_details_dto import ImportedClusterDetailsDto
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    project_id = 56 # int | 

    try:
        # Imported cluster details
        api_response = api_instance.projects_imported_cluster_details(project_id)
        print("The response of ProjectsApi->projects_imported_cluster_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_imported_cluster_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**ImportedClusterDetailsDto**](ImportedClusterDetailsDto.md)

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

# **projects_list**
> ProjectsList projects_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, updated_at=updated_at, search_id=search_id, id=id, backup_credential_id=backup_credential_id, healthy=healthy)

Retrieve all projects

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.projects_list import ProjectsList
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    updated_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)
    backup_credential_id = 56 # int |  (optional)
    healthy = True # bool |  (optional)

    try:
        # Retrieve all projects
        api_response = api_instance.projects_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, updated_at=updated_at, search_id=search_id, id=id, backup_credential_id=backup_credential_id, healthy=healthy)
        print("The response of ProjectsApi->projects_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_list: %s\n" % e)
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
 **updated_at** | **datetime**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **backup_credential_id** | **int**|  | [optional] 
 **healthy** | **bool**|  | [optional] 

### Return type

[**ProjectsList**](ProjectsList.md)

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

# **projects_lock_manager**
> object projects_lock_manager(project_lock_manager_command)

Lock/Unlock project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_lock_manager_command import ProjectLockManagerCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    project_lock_manager_command = taikunpycore.ProjectLockManagerCommand() # ProjectLockManagerCommand | 

    try:
        # Lock/Unlock project
        api_response = api_instance.projects_lock_manager(project_lock_manager_command)
        print("The response of ProjectsApi->projects_lock_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_lock_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_lock_manager_command** | [**ProjectLockManagerCommand**](ProjectLockManagerCommand.md)|  | 

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

# **projects_loki_logs**
> projects_loki_logs(loki_response_dto=loki_response_dto)

Retrieve loki logs

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.loki_response_dto import LokiResponseDto
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    loki_response_dto = taikunpycore.LokiResponseDto() # LokiResponseDto |  (optional)

    try:
        # Retrieve loki logs
        api_instance.projects_loki_logs(loki_response_dto=loki_response_dto)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_loki_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loki_response_dto** | [**LokiResponseDto**](LokiResponseDto.md)|  | [optional] 

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

# **projects_maintenance_manager**
> object projects_maintenance_manager(project_maintenance_mode_command)

Enable/disable project's maintenance mode

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_maintenance_mode_command import ProjectMaintenanceModeCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    project_maintenance_mode_command = taikunpycore.ProjectMaintenanceModeCommand() # ProjectMaintenanceModeCommand | 

    try:
        # Enable/disable project's maintenance mode
        api_response = api_instance.projects_maintenance_manager(project_maintenance_mode_command)
        print("The response of ProjectsApi->projects_maintenance_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_maintenance_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_maintenance_mode_command** | [**ProjectMaintenanceModeCommand**](ProjectMaintenanceModeCommand.md)|  | 

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

# **projects_monitoring_alerts**
> ProjectMonitoringAlertsDto projects_monitoring_alerts(projects_monitoring_alerts_command)

Monitoring alerts for project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_monitoring_alerts_dto import ProjectMonitoringAlertsDto
from taikunpycore.models.projects_monitoring_alerts_command import ProjectsMonitoringAlertsCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    projects_monitoring_alerts_command = taikunpycore.ProjectsMonitoringAlertsCommand() # ProjectsMonitoringAlertsCommand | 

    try:
        # Monitoring alerts for project
        api_response = api_instance.projects_monitoring_alerts(projects_monitoring_alerts_command)
        print("The response of ProjectsApi->projects_monitoring_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_monitoring_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_monitoring_alerts_command** | [**ProjectsMonitoringAlertsCommand**](ProjectsMonitoringAlertsCommand.md)|  | 

### Return type

[**ProjectMonitoringAlertsDto**](ProjectMonitoringAlertsDto.md)

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

# **projects_prometheus_metrics**
> PrometheusMetricListDto projects_prometheus_metrics(prometheus_metrics_command=prometheus_metrics_command)

Prometheus metrics data project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.prometheus_metric_list_dto import PrometheusMetricListDto
from taikunpycore.models.prometheus_metrics_command import PrometheusMetricsCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    prometheus_metrics_command = taikunpycore.PrometheusMetricsCommand() # PrometheusMetricsCommand |  (optional)

    try:
        # Prometheus metrics data project
        api_response = api_instance.projects_prometheus_metrics(prometheus_metrics_command=prometheus_metrics_command)
        print("The response of ProjectsApi->projects_prometheus_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_prometheus_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prometheus_metrics_command** | [**PrometheusMetricsCommand**](PrometheusMetricsCommand.md)|  | [optional] 

### Return type

[**PrometheusMetricListDto**](PrometheusMetricListDto.md)

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

# **projects_prometheus_metrics_autocomplete**
> List[str] projects_prometheus_metrics_autocomplete(prometheus_metrics_autocomplete_command=prometheus_metrics_autocomplete_command)

Prometheus metrics autocomplete values

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.prometheus_metrics_autocomplete_command import PrometheusMetricsAutocompleteCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    prometheus_metrics_autocomplete_command = taikunpycore.PrometheusMetricsAutocompleteCommand() # PrometheusMetricsAutocompleteCommand |  (optional)

    try:
        # Prometheus metrics autocomplete values
        api_response = api_instance.projects_prometheus_metrics_autocomplete(prometheus_metrics_autocomplete_command=prometheus_metrics_autocomplete_command)
        print("The response of ProjectsApi->projects_prometheus_metrics_autocomplete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_prometheus_metrics_autocomplete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prometheus_metrics_autocomplete_command** | [**PrometheusMetricsAutocompleteCommand**](PrometheusMetricsAutocompleteCommand.md)|  | [optional] 

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

# **projects_toggle_full_spot**
> object projects_toggle_full_spot(full_spot_operation_command)

Full spot operations enable/disable

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.full_spot_operation_command import FullSpotOperationCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    full_spot_operation_command = taikunpycore.FullSpotOperationCommand() # FullSpotOperationCommand | 

    try:
        # Full spot operations enable/disable
        api_response = api_instance.projects_toggle_full_spot(full_spot_operation_command)
        print("The response of ProjectsApi->projects_toggle_full_spot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_toggle_full_spot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_spot_operation_command** | [**FullSpotOperationCommand**](FullSpotOperationCommand.md)|  | 

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

# **projects_toggle_spot_vms**
> object projects_toggle_spot_vms(spot_vm_operation_command)

Spot vm(s) operations enable/disable

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.spot_vm_operation_command import SpotVmOperationCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    spot_vm_operation_command = taikunpycore.SpotVmOperationCommand() # SpotVmOperationCommand | 

    try:
        # Spot vm(s) operations enable/disable
        api_response = api_instance.projects_toggle_spot_vms(spot_vm_operation_command)
        print("The response of ProjectsApi->projects_toggle_spot_vms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_toggle_spot_vms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spot_vm_operation_command** | [**SpotVmOperationCommand**](SpotVmOperationCommand.md)|  | 

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

# **projects_toggle_spot_workers**
> object projects_toggle_spot_workers(spot_worker_operation_command)

Spot worker(s) operations enable/disable

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.spot_worker_operation_command import SpotWorkerOperationCommand
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    spot_worker_operation_command = taikunpycore.SpotWorkerOperationCommand() # SpotWorkerOperationCommand | 

    try:
        # Spot worker(s) operations enable/disable
        api_response = api_instance.projects_toggle_spot_workers(spot_worker_operation_command)
        print("The response of ProjectsApi->projects_toggle_spot_workers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_toggle_spot_workers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spot_worker_operation_command** | [**SpotWorkerOperationCommand**](SpotWorkerOperationCommand.md)|  | 

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

# **projects_visibility**
> ProjectActionVisibilityDto projects_visibility(project_id)

Visibility of project actions

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_action_visibility_dto import ProjectActionVisibilityDto
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
    api_instance = taikunpycore.ProjectsApi(api_client)
    project_id = 56 # int | 

    try:
        # Visibility of project actions
        api_response = api_instance.projects_visibility(project_id)
        print("The response of ProjectsApi->projects_visibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_visibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**ProjectActionVisibilityDto**](ProjectActionVisibilityDto.md)

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

