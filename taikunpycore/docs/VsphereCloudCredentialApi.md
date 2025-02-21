# taikunpycore.VsphereCloudCredentialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vsphere_create**](VsphereCloudCredentialApi.md#vsphere_create) | **POST** /api/v1/vsphere/create | Add Vsphere credentials
[**vsphere_datacenter_list**](VsphereCloudCredentialApi.md#vsphere_datacenter_list) | **POST** /api/v1/vsphere/datacenter-list | Fetch Vsphere datacenter list
[**vsphere_datastore_list**](VsphereCloudCredentialApi.md#vsphere_datastore_list) | **POST** /api/v1/vsphere/datastore-list | Fetch Vsphere datastore list
[**vsphere_hypervisor_list**](VsphereCloudCredentialApi.md#vsphere_hypervisor_list) | **POST** /api/v1/vsphere/hypervisor-list | Fetch Vsphere hypervisor list
[**vsphere_list**](VsphereCloudCredentialApi.md#vsphere_list) | **GET** /api/v1/vsphere/list | Retrieve list of vsphere cloud credentials
[**vsphere_network_list**](VsphereCloudCredentialApi.md#vsphere_network_list) | **POST** /api/v1/vsphere/network-list | Fetch Vsphere network list
[**vsphere_resource_pool_list**](VsphereCloudCredentialApi.md#vsphere_resource_pool_list) | **POST** /api/v1/vsphere/resource-pool-list | Fetch Vsphere resource pool list
[**vsphere_update**](VsphereCloudCredentialApi.md#vsphere_update) | **POST** /api/v1/vsphere/update | Update Vsphere credentials
[**vsphere_update_vsphere_hypervisors**](VsphereCloudCredentialApi.md#vsphere_update_vsphere_hypervisors) | **POST** /api/v1/vsphere/update/hypervisors | Update Vsphere credentials
[**vsphere_validate**](VsphereCloudCredentialApi.md#vsphere_validate) | **POST** /api/v1/vsphere/validate | Validate Vsphere credentials
[**vsphere_vm_template_list**](VsphereCloudCredentialApi.md#vsphere_vm_template_list) | **POST** /api/v1/vsphere/vm-template-list | Fetch Vsphere vm template list


# **vsphere_create**
> ApiResponse vsphere_create(create_vsphere_command=create_vsphere_command)

Add Vsphere credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_vsphere_command import CreateVsphereCommand
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
    api_instance = taikunpycore.VsphereCloudCredentialApi(api_client)
    create_vsphere_command = taikunpycore.CreateVsphereCommand() # CreateVsphereCommand |  (optional)

    try:
        # Add Vsphere credentials
        api_response = api_instance.vsphere_create(create_vsphere_command=create_vsphere_command)
        print("The response of VsphereCloudCredentialApi->vsphere_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsphereCloudCredentialApi->vsphere_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_vsphere_command** | [**CreateVsphereCommand**](CreateVsphereCommand.md)|  | [optional] 

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

# **vsphere_datacenter_list**
> List[DatacenterSummary] vsphere_datacenter_list(datacenter_list_command)

Fetch Vsphere datacenter list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.datacenter_list_command import DatacenterListCommand
from taikunpycore.models.datacenter_summary import DatacenterSummary
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
    api_instance = taikunpycore.VsphereCloudCredentialApi(api_client)
    datacenter_list_command = taikunpycore.DatacenterListCommand() # DatacenterListCommand | 

    try:
        # Fetch Vsphere datacenter list
        api_response = api_instance.vsphere_datacenter_list(datacenter_list_command)
        print("The response of VsphereCloudCredentialApi->vsphere_datacenter_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsphereCloudCredentialApi->vsphere_datacenter_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_list_command** | [**DatacenterListCommand**](DatacenterListCommand.md)|  | 

### Return type

[**List[DatacenterSummary]**](DatacenterSummary.md)

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

# **vsphere_datastore_list**
> List[DatastoreSummary] vsphere_datastore_list(datastore_list_command)

Fetch Vsphere datastore list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.datastore_list_command import DatastoreListCommand
from taikunpycore.models.datastore_summary import DatastoreSummary
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
    api_instance = taikunpycore.VsphereCloudCredentialApi(api_client)
    datastore_list_command = taikunpycore.DatastoreListCommand() # DatastoreListCommand | 

    try:
        # Fetch Vsphere datastore list
        api_response = api_instance.vsphere_datastore_list(datastore_list_command)
        print("The response of VsphereCloudCredentialApi->vsphere_datastore_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsphereCloudCredentialApi->vsphere_datastore_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datastore_list_command** | [**DatastoreListCommand**](DatastoreListCommand.md)|  | 

### Return type

[**List[DatastoreSummary]**](DatastoreSummary.md)

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

# **vsphere_hypervisor_list**
> List[ProxmoxHypervisorDto] vsphere_hypervisor_list(vsphere_hypervisor_list_command)

Fetch Vsphere hypervisor list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.proxmox_hypervisor_dto import ProxmoxHypervisorDto
from taikunpycore.models.vsphere_hypervisor_list_command import VsphereHypervisorListCommand
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
    api_instance = taikunpycore.VsphereCloudCredentialApi(api_client)
    vsphere_hypervisor_list_command = taikunpycore.VsphereHypervisorListCommand() # VsphereHypervisorListCommand | 

    try:
        # Fetch Vsphere hypervisor list
        api_response = api_instance.vsphere_hypervisor_list(vsphere_hypervisor_list_command)
        print("The response of VsphereCloudCredentialApi->vsphere_hypervisor_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsphereCloudCredentialApi->vsphere_hypervisor_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vsphere_hypervisor_list_command** | [**VsphereHypervisorListCommand**](VsphereHypervisorListCommand.md)|  | 

### Return type

[**List[ProxmoxHypervisorDto]**](ProxmoxHypervisorDto.md)

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

# **vsphere_list**
> VsphereList vsphere_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)

Retrieve list of vsphere cloud credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.vsphere_list import VsphereList
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
    api_instance = taikunpycore.VsphereCloudCredentialApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve list of vsphere cloud credentials
        api_response = api_instance.vsphere_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)
        print("The response of VsphereCloudCredentialApi->vsphere_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsphereCloudCredentialApi->vsphere_list: %s\n" % e)
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

[**VsphereList**](VsphereList.md)

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

# **vsphere_network_list**
> List[NetworkSummary] vsphere_network_list(network_list_command)

Fetch Vsphere network list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.network_list_command import NetworkListCommand
from taikunpycore.models.network_summary import NetworkSummary
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
    api_instance = taikunpycore.VsphereCloudCredentialApi(api_client)
    network_list_command = taikunpycore.NetworkListCommand() # NetworkListCommand | 

    try:
        # Fetch Vsphere network list
        api_response = api_instance.vsphere_network_list(network_list_command)
        print("The response of VsphereCloudCredentialApi->vsphere_network_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsphereCloudCredentialApi->vsphere_network_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_list_command** | [**NetworkListCommand**](NetworkListCommand.md)|  | 

### Return type

[**List[NetworkSummary]**](NetworkSummary.md)

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

# **vsphere_resource_pool_list**
> List[ResourcePoolSummary] vsphere_resource_pool_list(resource_pool_list_command)

Fetch Vsphere resource pool list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.resource_pool_list_command import ResourcePoolListCommand
from taikunpycore.models.resource_pool_summary import ResourcePoolSummary
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
    api_instance = taikunpycore.VsphereCloudCredentialApi(api_client)
    resource_pool_list_command = taikunpycore.ResourcePoolListCommand() # ResourcePoolListCommand | 

    try:
        # Fetch Vsphere resource pool list
        api_response = api_instance.vsphere_resource_pool_list(resource_pool_list_command)
        print("The response of VsphereCloudCredentialApi->vsphere_resource_pool_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsphereCloudCredentialApi->vsphere_resource_pool_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_pool_list_command** | [**ResourcePoolListCommand**](ResourcePoolListCommand.md)|  | 

### Return type

[**List[ResourcePoolSummary]**](ResourcePoolSummary.md)

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

# **vsphere_update**
> object vsphere_update(update_vsphere_command=update_vsphere_command)

Update Vsphere credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_vsphere_command import UpdateVsphereCommand
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
    api_instance = taikunpycore.VsphereCloudCredentialApi(api_client)
    update_vsphere_command = taikunpycore.UpdateVsphereCommand() # UpdateVsphereCommand |  (optional)

    try:
        # Update Vsphere credentials
        api_response = api_instance.vsphere_update(update_vsphere_command=update_vsphere_command)
        print("The response of VsphereCloudCredentialApi->vsphere_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsphereCloudCredentialApi->vsphere_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_vsphere_command** | [**UpdateVsphereCommand**](UpdateVsphereCommand.md)|  | [optional] 

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

# **vsphere_update_vsphere_hypervisors**
> object vsphere_update_vsphere_hypervisors(update_vsphere_hypervisors_command)

Update Vsphere credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_vsphere_hypervisors_command import UpdateVsphereHypervisorsCommand
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
    api_instance = taikunpycore.VsphereCloudCredentialApi(api_client)
    update_vsphere_hypervisors_command = taikunpycore.UpdateVsphereHypervisorsCommand() # UpdateVsphereHypervisorsCommand | 

    try:
        # Update Vsphere credentials
        api_response = api_instance.vsphere_update_vsphere_hypervisors(update_vsphere_hypervisors_command)
        print("The response of VsphereCloudCredentialApi->vsphere_update_vsphere_hypervisors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsphereCloudCredentialApi->vsphere_update_vsphere_hypervisors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_vsphere_hypervisors_command** | [**UpdateVsphereHypervisorsCommand**](UpdateVsphereHypervisorsCommand.md)|  | 

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

# **vsphere_validate**
> object vsphere_validate(validate_vsphere_command)

Validate Vsphere credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.validate_vsphere_command import ValidateVsphereCommand
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
    api_instance = taikunpycore.VsphereCloudCredentialApi(api_client)
    validate_vsphere_command = taikunpycore.ValidateVsphereCommand() # ValidateVsphereCommand | 

    try:
        # Validate Vsphere credentials
        api_response = api_instance.vsphere_validate(validate_vsphere_command)
        print("The response of VsphereCloudCredentialApi->vsphere_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsphereCloudCredentialApi->vsphere_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_vsphere_command** | [**ValidateVsphereCommand**](ValidateVsphereCommand.md)|  | 

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

# **vsphere_vm_template_list**
> List[VsphereVmTemplateData] vsphere_vm_template_list(vsphere_vm_template_list_command)

Fetch Vsphere vm template list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.vsphere_vm_template_data import VsphereVmTemplateData
from taikunpycore.models.vsphere_vm_template_list_command import VsphereVmTemplateListCommand
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
    api_instance = taikunpycore.VsphereCloudCredentialApi(api_client)
    vsphere_vm_template_list_command = taikunpycore.VsphereVmTemplateListCommand() # VsphereVmTemplateListCommand | 

    try:
        # Fetch Vsphere vm template list
        api_response = api_instance.vsphere_vm_template_list(vsphere_vm_template_list_command)
        print("The response of VsphereCloudCredentialApi->vsphere_vm_template_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsphereCloudCredentialApi->vsphere_vm_template_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vsphere_vm_template_list_command** | [**VsphereVmTemplateListCommand**](VsphereVmTemplateListCommand.md)|  | 

### Return type

[**List[VsphereVmTemplateData]**](VsphereVmTemplateData.md)

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

