# taikunpycore.OpenstackCloudCredentialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openstack_create**](OpenstackCloudCredentialApi.md#openstack_create) | **POST** /api/v1/openstack/create | Add Openstack credentials
[**openstack_list**](OpenstackCloudCredentialApi.md#openstack_list) | **GET** /api/v1/openstack/list | Retrieve list of openstack cloud credentials
[**openstack_networks**](OpenstackCloudCredentialApi.md#openstack_networks) | **POST** /api/v1/openstack/networks | Openstack network list
[**openstack_projects**](OpenstackCloudCredentialApi.md#openstack_projects) | **POST** /api/v1/openstack/projects | Openstack project list
[**openstack_quotas**](OpenstackCloudCredentialApi.md#openstack_quotas) | **POST** /api/v1/openstack/quotas | Openstack quota list
[**openstack_region_list**](OpenstackCloudCredentialApi.md#openstack_region_list) | **POST** /api/v1/openstack/regions | Retrieve Openstack regions
[**openstack_subnet**](OpenstackCloudCredentialApi.md#openstack_subnet) | **POST** /api/v1/openstack/subnets | Retrieve Openstack subnets
[**openstack_update**](OpenstackCloudCredentialApi.md#openstack_update) | **POST** /api/v1/openstack/update | Update Openstack credentials
[**openstack_volumes**](OpenstackCloudCredentialApi.md#openstack_volumes) | **POST** /api/v1/openstack/volumes | Openstack volume list
[**openstack_zones**](OpenstackCloudCredentialApi.md#openstack_zones) | **POST** /api/v1/openstack/zones | Fetch Openstack zones


# **openstack_create**
> ApiResponse openstack_create(create_openstack_cloud_command)

Add Openstack credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_openstack_cloud_command import CreateOpenstackCloudCommand
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
    api_instance = taikunpycore.OpenstackCloudCredentialApi(api_client)
    create_openstack_cloud_command = taikunpycore.CreateOpenstackCloudCommand() # CreateOpenstackCloudCommand | 

    try:
        # Add Openstack credentials
        api_response = api_instance.openstack_create(create_openstack_cloud_command)
        print("The response of OpenstackCloudCredentialApi->openstack_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenstackCloudCredentialApi->openstack_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_openstack_cloud_command** | [**CreateOpenstackCloudCommand**](CreateOpenstackCloudCommand.md)|  | 

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

# **openstack_list**
> OpenstackCredentialList openstack_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id, is_infra=is_infra)

Retrieve list of openstack cloud credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.openstack_credential_list import OpenstackCredentialList
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
    api_instance = taikunpycore.OpenstackCloudCredentialApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)
    is_infra = True # bool |  (optional)

    try:
        # Retrieve list of openstack cloud credentials
        api_response = api_instance.openstack_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id, is_infra=is_infra)
        print("The response of OpenstackCloudCredentialApi->openstack_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenstackCloudCredentialApi->openstack_list: %s\n" % e)
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
 **is_infra** | **bool**|  | [optional] 

### Return type

[**OpenstackCredentialList**](OpenstackCredentialList.md)

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

# **openstack_networks**
> List[CommonStringBasedDropdownDto] openstack_networks(open_stack_network_list_query)

Openstack network list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_string_based_dropdown_dto import CommonStringBasedDropdownDto
from taikunpycore.models.open_stack_network_list_query import OpenStackNetworkListQuery
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
    api_instance = taikunpycore.OpenstackCloudCredentialApi(api_client)
    open_stack_network_list_query = taikunpycore.OpenStackNetworkListQuery() # OpenStackNetworkListQuery | 

    try:
        # Openstack network list
        api_response = api_instance.openstack_networks(open_stack_network_list_query)
        print("The response of OpenstackCloudCredentialApi->openstack_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenstackCloudCredentialApi->openstack_networks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_stack_network_list_query** | [**OpenStackNetworkListQuery**](OpenStackNetworkListQuery.md)|  | 

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

# **openstack_projects**
> List[CommonStringBasedDropdownDto] openstack_projects(open_stack_project_list_query)

Openstack project list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_string_based_dropdown_dto import CommonStringBasedDropdownDto
from taikunpycore.models.open_stack_project_list_query import OpenStackProjectListQuery
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
    api_instance = taikunpycore.OpenstackCloudCredentialApi(api_client)
    open_stack_project_list_query = taikunpycore.OpenStackProjectListQuery() # OpenStackProjectListQuery | 

    try:
        # Openstack project list
        api_response = api_instance.openstack_projects(open_stack_project_list_query)
        print("The response of OpenstackCloudCredentialApi->openstack_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenstackCloudCredentialApi->openstack_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_stack_project_list_query** | [**OpenStackProjectListQuery**](OpenStackProjectListQuery.md)|  | 

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

# **openstack_quotas**
> OpenstackQuotaList openstack_quotas(openstack_quotas_command)

Openstack quota list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.openstack_quota_list import OpenstackQuotaList
from taikunpycore.models.openstack_quotas_command import OpenstackQuotasCommand
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
    api_instance = taikunpycore.OpenstackCloudCredentialApi(api_client)
    openstack_quotas_command = taikunpycore.OpenstackQuotasCommand() # OpenstackQuotasCommand | 

    try:
        # Openstack quota list
        api_response = api_instance.openstack_quotas(openstack_quotas_command)
        print("The response of OpenstackCloudCredentialApi->openstack_quotas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenstackCloudCredentialApi->openstack_quotas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **openstack_quotas_command** | [**OpenstackQuotasCommand**](OpenstackQuotasCommand.md)|  | 

### Return type

[**OpenstackQuotaList**](OpenstackQuotaList.md)

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

# **openstack_region_list**
> List[str] openstack_region_list(open_stack_region_list_query)

Retrieve Openstack regions

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.open_stack_region_list_query import OpenStackRegionListQuery
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
    api_instance = taikunpycore.OpenstackCloudCredentialApi(api_client)
    open_stack_region_list_query = taikunpycore.OpenStackRegionListQuery() # OpenStackRegionListQuery | 

    try:
        # Retrieve Openstack regions
        api_response = api_instance.openstack_region_list(open_stack_region_list_query)
        print("The response of OpenstackCloudCredentialApi->openstack_region_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenstackCloudCredentialApi->openstack_region_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_stack_region_list_query** | [**OpenStackRegionListQuery**](OpenStackRegionListQuery.md)|  | 

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

# **openstack_subnet**
> List[Subnet] openstack_subnet(openstack_subnet_list_query)

Retrieve Openstack subnets

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.openstack_subnet_list_query import OpenstackSubnetListQuery
from taikunpycore.models.subnet import Subnet
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
    api_instance = taikunpycore.OpenstackCloudCredentialApi(api_client)
    openstack_subnet_list_query = taikunpycore.OpenstackSubnetListQuery() # OpenstackSubnetListQuery | 

    try:
        # Retrieve Openstack subnets
        api_response = api_instance.openstack_subnet(openstack_subnet_list_query)
        print("The response of OpenstackCloudCredentialApi->openstack_subnet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenstackCloudCredentialApi->openstack_subnet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **openstack_subnet_list_query** | [**OpenstackSubnetListQuery**](OpenstackSubnetListQuery.md)|  | 

### Return type

[**List[Subnet]**](Subnet.md)

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

# **openstack_update**
> object openstack_update(update_open_stack_command)

Update Openstack credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_open_stack_command import UpdateOpenStackCommand
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
    api_instance = taikunpycore.OpenstackCloudCredentialApi(api_client)
    update_open_stack_command = taikunpycore.UpdateOpenStackCommand() # UpdateOpenStackCommand | 

    try:
        # Update Openstack credentials
        api_response = api_instance.openstack_update(update_open_stack_command)
        print("The response of OpenstackCloudCredentialApi->openstack_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenstackCloudCredentialApi->openstack_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_open_stack_command** | [**UpdateOpenStackCommand**](UpdateOpenStackCommand.md)|  | 

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

# **openstack_volumes**
> List[str] openstack_volumes(openstack_volume_type_list_query)

Openstack volume list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.openstack_volume_type_list_query import OpenstackVolumeTypeListQuery
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
    api_instance = taikunpycore.OpenstackCloudCredentialApi(api_client)
    openstack_volume_type_list_query = taikunpycore.OpenstackVolumeTypeListQuery() # OpenstackVolumeTypeListQuery | 

    try:
        # Openstack volume list
        api_response = api_instance.openstack_volumes(openstack_volume_type_list_query)
        print("The response of OpenstackCloudCredentialApi->openstack_volumes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenstackCloudCredentialApi->openstack_volumes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **openstack_volume_type_list_query** | [**OpenstackVolumeTypeListQuery**](OpenstackVolumeTypeListQuery.md)|  | 

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

# **openstack_zones**
> List[str] openstack_zones(open_stack_zone_list_query)

Fetch Openstack zones

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.open_stack_zone_list_query import OpenStackZoneListQuery
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
    api_instance = taikunpycore.OpenstackCloudCredentialApi(api_client)
    open_stack_zone_list_query = taikunpycore.OpenStackZoneListQuery() # OpenStackZoneListQuery | 

    try:
        # Fetch Openstack zones
        api_response = api_instance.openstack_zones(open_stack_zone_list_query)
        print("The response of OpenstackCloudCredentialApi->openstack_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenstackCloudCredentialApi->openstack_zones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_stack_zone_list_query** | [**OpenStackZoneListQuery**](OpenStackZoneListQuery.md)|  | 

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

