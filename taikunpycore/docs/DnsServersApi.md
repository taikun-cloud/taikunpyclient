# taikunpycore.DnsServersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dnsservers_create**](DnsServersApi.md#dnsservers_create) | **POST** /api/v1/dnsservers/create | Create dns servers for access profile
[**dnsservers_delete**](DnsServersApi.md#dnsservers_delete) | **DELETE** /api/v1/dnsservers/{id} | Delete DNS server
[**dnsservers_edit**](DnsServersApi.md#dnsservers_edit) | **PUT** /api/v1/dnsservers/edit/{id} | Edit dns server
[**dnsservers_list**](DnsServersApi.md#dnsservers_list) | **GET** /api/v1/dnsservers/{accessProfileId} | List dns servers by profile id


# **dnsservers_create**
> ApiResponse dnsservers_create(create_dns_server_command=create_dns_server_command)

Create dns servers for access profile

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_dns_server_command import CreateDnsServerCommand
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
    api_instance = taikunpycore.DnsServersApi(api_client)
    create_dns_server_command = {"address":"8.8.8.8","accessProfileId":1} # CreateDnsServerCommand |  (optional)

    try:
        # Create dns servers for access profile
        api_response = api_instance.dnsservers_create(create_dns_server_command=create_dns_server_command)
        print("The response of DnsServersApi->dnsservers_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DnsServersApi->dnsservers_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dns_server_command** | [**CreateDnsServerCommand**](CreateDnsServerCommand.md)|  | [optional] 

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

# **dnsservers_delete**
> dnsservers_delete(id)

Delete DNS server

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
    api_instance = taikunpycore.DnsServersApi(api_client)
    id = 56 # int | 

    try:
        # Delete DNS server
        api_instance.dnsservers_delete(id)
    except Exception as e:
        print("Exception when calling DnsServersApi->dnsservers_delete: %s\n" % e)
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

# **dnsservers_edit**
> dnsservers_edit(id, dns_ntp_address_edit_dto=dns_ntp_address_edit_dto)

Edit dns server

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.dns_ntp_address_edit_dto import DnsNtpAddressEditDto
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
    api_instance = taikunpycore.DnsServersApi(api_client)
    id = 56 # int | 
    dns_ntp_address_edit_dto = {"address":"8.8.8.8"} # DnsNtpAddressEditDto |  (optional)

    try:
        # Edit dns server
        api_instance.dnsservers_edit(id, dns_ntp_address_edit_dto=dns_ntp_address_edit_dto)
    except Exception as e:
        print("Exception when calling DnsServersApi->dnsservers_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **dns_ntp_address_edit_dto** | [**DnsNtpAddressEditDto**](DnsNtpAddressEditDto.md)|  | [optional] 

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

# **dnsservers_list**
> List[DnsServersListDto] dnsservers_list(access_profile_id, search=search)

List dns servers by profile id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.dns_servers_list_dto import DnsServersListDto
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
    api_instance = taikunpycore.DnsServersApi(api_client)
    access_profile_id = 56 # int | 
    search = 'search_example' # str |  (optional)

    try:
        # List dns servers by profile id
        api_response = api_instance.dnsservers_list(access_profile_id, search=search)
        print("The response of DnsServersApi->dnsservers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DnsServersApi->dnsservers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_profile_id** | **int**|  | 
 **search** | **str**|  | [optional] 

### Return type

[**List[DnsServersListDto]**](DnsServersListDto.md)

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

