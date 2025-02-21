# taikunpycore.ProxmoxCloudCredentialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proxmox_bridge_list**](ProxmoxCloudCredentialApi.md#proxmox_bridge_list) | **POST** /api/v1/proxmox/bridge-list | Fetch proxmox bridge list
[**proxmox_create**](ProxmoxCloudCredentialApi.md#proxmox_create) | **POST** /api/v1/proxmox/create | Add Proxmox credentials
[**proxmox_hypervisor_list**](ProxmoxCloudCredentialApi.md#proxmox_hypervisor_list) | **POST** /api/v1/proxmox/hypervisor-list | Fetch proxmox hypervisor list
[**proxmox_list**](ProxmoxCloudCredentialApi.md#proxmox_list) | **GET** /api/v1/proxmox/list | Retrieve list of proxmox cloud credentials
[**proxmox_storage_list**](ProxmoxCloudCredentialApi.md#proxmox_storage_list) | **POST** /api/v1/proxmox/storage-list | Fetch proxmox storage list
[**proxmox_update**](ProxmoxCloudCredentialApi.md#proxmox_update) | **POST** /api/v1/proxmox/update | Update proxmox credentials
[**proxmox_update_hypervisors**](ProxmoxCloudCredentialApi.md#proxmox_update_hypervisors) | **POST** /api/v1/proxmox/update/hypervisors | Update proxmox credentials
[**proxmox_update_ip_addresses**](ProxmoxCloudCredentialApi.md#proxmox_update_ip_addresses) | **POST** /api/v1/proxmox/update/ip-addresses | Update proxmox network used ip addresses
[**proxmox_vm_template_list**](ProxmoxCloudCredentialApi.md#proxmox_vm_template_list) | **POST** /api/v1/proxmox/vm-template-list | Fetch proxmox vm template list


# **proxmox_bridge_list**
> List[str] proxmox_bridge_list(bridge_list_command)

Fetch proxmox bridge list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.bridge_list_command import BridgeListCommand
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
    api_instance = taikunpycore.ProxmoxCloudCredentialApi(api_client)
    bridge_list_command = taikunpycore.BridgeListCommand() # BridgeListCommand | 

    try:
        # Fetch proxmox bridge list
        api_response = api_instance.proxmox_bridge_list(bridge_list_command)
        print("The response of ProxmoxCloudCredentialApi->proxmox_bridge_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProxmoxCloudCredentialApi->proxmox_bridge_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_list_command** | [**BridgeListCommand**](BridgeListCommand.md)|  | 

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

# **proxmox_create**
> ApiResponse proxmox_create(create_proxmox_command=create_proxmox_command)

Add Proxmox credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_proxmox_command import CreateProxmoxCommand
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
    api_instance = taikunpycore.ProxmoxCloudCredentialApi(api_client)
    create_proxmox_command = taikunpycore.CreateProxmoxCommand() # CreateProxmoxCommand |  (optional)

    try:
        # Add Proxmox credentials
        api_response = api_instance.proxmox_create(create_proxmox_command=create_proxmox_command)
        print("The response of ProxmoxCloudCredentialApi->proxmox_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProxmoxCloudCredentialApi->proxmox_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_proxmox_command** | [**CreateProxmoxCommand**](CreateProxmoxCommand.md)|  | [optional] 

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

# **proxmox_hypervisor_list**
> List[ProxmoxHypervisorDto] proxmox_hypervisor_list(hypervisor_list_command)

Fetch proxmox hypervisor list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.hypervisor_list_command import HypervisorListCommand
from taikunpycore.models.proxmox_hypervisor_dto import ProxmoxHypervisorDto
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
    api_instance = taikunpycore.ProxmoxCloudCredentialApi(api_client)
    hypervisor_list_command = taikunpycore.HypervisorListCommand() # HypervisorListCommand | 

    try:
        # Fetch proxmox hypervisor list
        api_response = api_instance.proxmox_hypervisor_list(hypervisor_list_command)
        print("The response of ProxmoxCloudCredentialApi->proxmox_hypervisor_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProxmoxCloudCredentialApi->proxmox_hypervisor_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hypervisor_list_command** | [**HypervisorListCommand**](HypervisorListCommand.md)|  | 

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

# **proxmox_list**
> ProxmoxList proxmox_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)

Retrieve list of proxmox cloud credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.proxmox_list import ProxmoxList
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
    api_instance = taikunpycore.ProxmoxCloudCredentialApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve list of proxmox cloud credentials
        api_response = api_instance.proxmox_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)
        print("The response of ProxmoxCloudCredentialApi->proxmox_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProxmoxCloudCredentialApi->proxmox_list: %s\n" % e)
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

[**ProxmoxList**](ProxmoxList.md)

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

# **proxmox_storage_list**
> List[str] proxmox_storage_list(storage_list_command)

Fetch proxmox storage list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.storage_list_command import StorageListCommand
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
    api_instance = taikunpycore.ProxmoxCloudCredentialApi(api_client)
    storage_list_command = taikunpycore.StorageListCommand() # StorageListCommand | 

    try:
        # Fetch proxmox storage list
        api_response = api_instance.proxmox_storage_list(storage_list_command)
        print("The response of ProxmoxCloudCredentialApi->proxmox_storage_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProxmoxCloudCredentialApi->proxmox_storage_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_list_command** | [**StorageListCommand**](StorageListCommand.md)|  | 

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

# **proxmox_update**
> object proxmox_update(update_proxmox_command=update_proxmox_command)

Update proxmox credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_proxmox_command import UpdateProxmoxCommand
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
    api_instance = taikunpycore.ProxmoxCloudCredentialApi(api_client)
    update_proxmox_command = taikunpycore.UpdateProxmoxCommand() # UpdateProxmoxCommand |  (optional)

    try:
        # Update proxmox credentials
        api_response = api_instance.proxmox_update(update_proxmox_command=update_proxmox_command)
        print("The response of ProxmoxCloudCredentialApi->proxmox_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProxmoxCloudCredentialApi->proxmox_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_proxmox_command** | [**UpdateProxmoxCommand**](UpdateProxmoxCommand.md)|  | [optional] 

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

# **proxmox_update_hypervisors**
> object proxmox_update_hypervisors(update_hypervisors_command=update_hypervisors_command)

Update proxmox credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_hypervisors_command import UpdateHypervisorsCommand
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
    api_instance = taikunpycore.ProxmoxCloudCredentialApi(api_client)
    update_hypervisors_command = taikunpycore.UpdateHypervisorsCommand() # UpdateHypervisorsCommand |  (optional)

    try:
        # Update proxmox credentials
        api_response = api_instance.proxmox_update_hypervisors(update_hypervisors_command=update_hypervisors_command)
        print("The response of ProxmoxCloudCredentialApi->proxmox_update_hypervisors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProxmoxCloudCredentialApi->proxmox_update_hypervisors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_hypervisors_command** | [**UpdateHypervisorsCommand**](UpdateHypervisorsCommand.md)|  | [optional] 

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

# **proxmox_update_ip_addresses**
> object proxmox_update_ip_addresses(update_used_ip_addresses_command)

Update proxmox network used ip addresses

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_used_ip_addresses_command import UpdateUsedIpAddressesCommand
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
    api_instance = taikunpycore.ProxmoxCloudCredentialApi(api_client)
    update_used_ip_addresses_command = taikunpycore.UpdateUsedIpAddressesCommand() # UpdateUsedIpAddressesCommand | 

    try:
        # Update proxmox network used ip addresses
        api_response = api_instance.proxmox_update_ip_addresses(update_used_ip_addresses_command)
        print("The response of ProxmoxCloudCredentialApi->proxmox_update_ip_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProxmoxCloudCredentialApi->proxmox_update_ip_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_used_ip_addresses_command** | [**UpdateUsedIpAddressesCommand**](UpdateUsedIpAddressesCommand.md)|  | 

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

# **proxmox_vm_template_list**
> List[CommonDropdownDto] proxmox_vm_template_list(vm_template_list_command)

Fetch proxmox vm template list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_dropdown_dto import CommonDropdownDto
from taikunpycore.models.vm_template_list_command import VmTemplateListCommand
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
    api_instance = taikunpycore.ProxmoxCloudCredentialApi(api_client)
    vm_template_list_command = taikunpycore.VmTemplateListCommand() # VmTemplateListCommand | 

    try:
        # Fetch proxmox vm template list
        api_response = api_instance.proxmox_vm_template_list(vm_template_list_command)
        print("The response of ProxmoxCloudCredentialApi->proxmox_vm_template_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProxmoxCloudCredentialApi->proxmox_vm_template_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_template_list_command** | [**VmTemplateListCommand**](VmTemplateListCommand.md)|  | 

### Return type

[**List[CommonDropdownDto]**](CommonDropdownDto.md)

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

