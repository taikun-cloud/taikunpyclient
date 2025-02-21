# taikunpycore.FlavorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flavors_aws_instance_types**](FlavorsApi.md#flavors_aws_instance_types) | **GET** /api/v1/flavors/aws/{cloudId} | Retrieve awz instance types
[**flavors_azure_vm_sizes**](FlavorsApi.md#flavors_azure_vm_sizes) | **GET** /api/v1/flavors/azure/{cloudId} | Retrieve azure vm sizes
[**flavors_bind_to_project**](FlavorsApi.md#flavors_bind_to_project) | **POST** /api/v1/flavors/bind | Bind flavors to project
[**flavors_dropdown_flavors**](FlavorsApi.md#flavors_dropdown_flavors) | **GET** /api/v1/flavors/credentials/dropdown/list | Retrieve cloud credentials dropdown list
[**flavors_google_machine_types**](FlavorsApi.md#flavors_google_machine_types) | **GET** /api/v1/flavors/google/{cloudId} | Retrieve google machine types
[**flavors_openshift_flavors**](FlavorsApi.md#flavors_openshift_flavors) | **GET** /api/v1/flavors/openshift/{cloudId} | Retrieve openshift flavors
[**flavors_openstack_flavors**](FlavorsApi.md#flavors_openstack_flavors) | **GET** /api/v1/flavors/openstack/{cloudId} | Retrieve openstack flavors
[**flavors_proxmox_flavors**](FlavorsApi.md#flavors_proxmox_flavors) | **GET** /api/v1/flavors/proxmox/{cloudId} | Retrieve proxmox flavors
[**flavors_selected_flavors_for_project**](FlavorsApi.md#flavors_selected_flavors_for_project) | **GET** /api/v1/flavors/projects/list | Retrieve selected flavors for project
[**flavors_tanzu_flavors**](FlavorsApi.md#flavors_tanzu_flavors) | **GET** /api/v1/flavors/tanzu/{cloudId} | Retrieve tanzu flavors
[**flavors_unbind_from_project**](FlavorsApi.md#flavors_unbind_from_project) | **POST** /api/v1/flavors/unbind | Unbind flavors from project
[**flavors_vsphere_flavors**](FlavorsApi.md#flavors_vsphere_flavors) | **GET** /api/v1/flavors/vsphere/{cloudId} | Retrieve vsphere flavors
[**flavors_zadara_instance_types**](FlavorsApi.md#flavors_zadara_instance_types) | **GET** /api/v1/flavors/zadara/{cloudId} | Retrieve zadara instance types
[**flavors_zededa_flavors**](FlavorsApi.md#flavors_zededa_flavors) | **GET** /api/v1/flavors/zededa/{cloudId} | Retrieve zededa flavors


# **flavors_aws_instance_types**
> AwsFlavorList flavors_aws_instance_types(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)

Retrieve awz instance types

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.aws_flavor_list import AwsFlavorList
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve awz instance types
        api_response = api_instance.flavors_aws_instance_types(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)
        print("The response of FlavorsApi->flavors_aws_instance_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_aws_instance_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **start_ram** | **float**|  | [optional] 
 **end_ram** | **float**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**AwsFlavorList**](AwsFlavorList.md)

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

# **flavors_azure_vm_sizes**
> AzureFlavorList flavors_azure_vm_sizes(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)

Retrieve azure vm sizes

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.azure_flavor_list import AzureFlavorList
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve azure vm sizes
        api_response = api_instance.flavors_azure_vm_sizes(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)
        print("The response of FlavorsApi->flavors_azure_vm_sizes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_azure_vm_sizes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **start_ram** | **float**|  | [optional] 
 **end_ram** | **float**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**AzureFlavorList**](AzureFlavorList.md)

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

# **flavors_bind_to_project**
> object flavors_bind_to_project(bind_flavor_to_project_command=bind_flavor_to_project_command)

Bind flavors to project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.bind_flavor_to_project_command import BindFlavorToProjectCommand
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    bind_flavor_to_project_command = taikunpycore.BindFlavorToProjectCommand() # BindFlavorToProjectCommand |  (optional)

    try:
        # Bind flavors to project
        api_response = api_instance.flavors_bind_to_project(bind_flavor_to_project_command=bind_flavor_to_project_command)
        print("The response of FlavorsApi->flavors_bind_to_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_bind_to_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bind_flavor_to_project_command** | [**BindFlavorToProjectCommand**](BindFlavorToProjectCommand.md)|  | [optional] 

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

# **flavors_dropdown_flavors**
> List[CloudCredentialsDropdownRecordDto] flavors_dropdown_flavors(organization_id=organization_id, filter_by=filter_by, search=search, is_infra=is_infra)

Retrieve cloud credentials dropdown list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.cloud_credentials_dropdown_record_dto import CloudCredentialsDropdownRecordDto
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    organization_id = 56 # int |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    is_infra = True # bool |  (optional)

    try:
        # Retrieve cloud credentials dropdown list
        api_response = api_instance.flavors_dropdown_flavors(organization_id=organization_id, filter_by=filter_by, search=search, is_infra=is_infra)
        print("The response of FlavorsApi->flavors_dropdown_flavors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_dropdown_flavors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **filter_by** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **is_infra** | **bool**|  | [optional] 

### Return type

[**List[CloudCredentialsDropdownRecordDto]**](CloudCredentialsDropdownRecordDto.md)

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

# **flavors_google_machine_types**
> GoogleFlavorList flavors_google_machine_types(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)

Retrieve google machine types

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.google_flavor_list import GoogleFlavorList
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve google machine types
        api_response = api_instance.flavors_google_machine_types(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)
        print("The response of FlavorsApi->flavors_google_machine_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_google_machine_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **start_ram** | **float**|  | [optional] 
 **end_ram** | **float**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**GoogleFlavorList**](GoogleFlavorList.md)

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

# **flavors_openshift_flavors**
> OpenshiftFlavorList flavors_openshift_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)

Retrieve openshift flavors

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.openshift_flavor_list import OpenshiftFlavorList
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve openshift flavors
        api_response = api_instance.flavors_openshift_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)
        print("The response of FlavorsApi->flavors_openshift_flavors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_openshift_flavors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **start_ram** | **float**|  | [optional] 
 **end_ram** | **float**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**OpenshiftFlavorList**](OpenshiftFlavorList.md)

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

# **flavors_openstack_flavors**
> OpenstackFlavorList flavors_openstack_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)

Retrieve openstack flavors

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.openstack_flavor_list import OpenstackFlavorList
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve openstack flavors
        api_response = api_instance.flavors_openstack_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)
        print("The response of FlavorsApi->flavors_openstack_flavors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_openstack_flavors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **start_ram** | **float**|  | [optional] 
 **end_ram** | **float**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**OpenstackFlavorList**](OpenstackFlavorList.md)

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

# **flavors_proxmox_flavors**
> ProxmoxFlavorList flavors_proxmox_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)

Retrieve proxmox flavors

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.proxmox_flavor_list import ProxmoxFlavorList
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve proxmox flavors
        api_response = api_instance.flavors_proxmox_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)
        print("The response of FlavorsApi->flavors_proxmox_flavors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_proxmox_flavors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **start_ram** | **float**|  | [optional] 
 **end_ram** | **float**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**ProxmoxFlavorList**](ProxmoxFlavorList.md)

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

# **flavors_selected_flavors_for_project**
> BoundFlavorsForProjectsList flavors_selected_flavors_for_project(limit=limit, offset=offset, project_id=project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, filter_by=filter_by, organization_id=organization_id, flavor_name=flavor_name, with_price=with_price)

Retrieve selected flavors for project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.bound_flavors_for_projects_list import BoundFlavorsForProjectsList
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    project_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)
    organization_id = 56 # int |  (optional)
    flavor_name = 'flavor_name_example' # str |  (optional)
    with_price = True # bool |  (optional)

    try:
        # Retrieve selected flavors for project
        api_response = api_instance.flavors_selected_flavors_for_project(limit=limit, offset=offset, project_id=project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, filter_by=filter_by, organization_id=organization_id, flavor_name=flavor_name, with_price=with_price)
        print("The response of FlavorsApi->flavors_selected_flavors_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_selected_flavors_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **project_id** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **flavor_name** | **str**|  | [optional] 
 **with_price** | **bool**|  | [optional] 

### Return type

[**BoundFlavorsForProjectsList**](BoundFlavorsForProjectsList.md)

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

# **flavors_tanzu_flavors**
> TanzuFlavorList flavors_tanzu_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)

Retrieve tanzu flavors

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.tanzu_flavor_list import TanzuFlavorList
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve tanzu flavors
        api_response = api_instance.flavors_tanzu_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)
        print("The response of FlavorsApi->flavors_tanzu_flavors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_tanzu_flavors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **start_ram** | **float**|  | [optional] 
 **end_ram** | **float**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**TanzuFlavorList**](TanzuFlavorList.md)

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

# **flavors_unbind_from_project**
> object flavors_unbind_from_project(unbind_flavor_from_project_command)

Unbind flavors from project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.unbind_flavor_from_project_command import UnbindFlavorFromProjectCommand
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    unbind_flavor_from_project_command = taikunpycore.UnbindFlavorFromProjectCommand() # UnbindFlavorFromProjectCommand | 

    try:
        # Unbind flavors from project
        api_response = api_instance.flavors_unbind_from_project(unbind_flavor_from_project_command)
        print("The response of FlavorsApi->flavors_unbind_from_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_unbind_from_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unbind_flavor_from_project_command** | [**UnbindFlavorFromProjectCommand**](UnbindFlavorFromProjectCommand.md)|  | 

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

# **flavors_vsphere_flavors**
> VsphereFlavorList flavors_vsphere_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)

Retrieve vsphere flavors

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.vsphere_flavor_list import VsphereFlavorList
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve vsphere flavors
        api_response = api_instance.flavors_vsphere_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)
        print("The response of FlavorsApi->flavors_vsphere_flavors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_vsphere_flavors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **start_ram** | **float**|  | [optional] 
 **end_ram** | **float**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**VsphereFlavorList**](VsphereFlavorList.md)

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

# **flavors_zadara_instance_types**
> AwsFlavorList flavors_zadara_instance_types(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)

Retrieve zadara instance types

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.aws_flavor_list import AwsFlavorList
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve zadara instance types
        api_response = api_instance.flavors_zadara_instance_types(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)
        print("The response of FlavorsApi->flavors_zadara_instance_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_zadara_instance_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **start_ram** | **float**|  | [optional] 
 **end_ram** | **float**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**AwsFlavorList**](AwsFlavorList.md)

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

# **flavors_zededa_flavors**
> ZededaFlavorList flavors_zededa_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)

Retrieve zededa flavors

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.zededa_flavor_list import ZededaFlavorList
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
    api_instance = taikunpycore.FlavorsApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve zededa flavors
        api_response = api_instance.flavors_zededa_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction, project_id=project_id)
        print("The response of FlavorsApi->flavors_zededa_flavors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorsApi->flavors_zededa_flavors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **start_ram** | **float**|  | [optional] 
 **end_ram** | **float**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**ZededaFlavorList**](ZededaFlavorList.md)

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

