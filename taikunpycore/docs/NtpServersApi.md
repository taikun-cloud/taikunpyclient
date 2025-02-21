# taikunpycore.NtpServersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ntpservers_create**](NtpServersApi.md#ntpservers_create) | **POST** /api/v1/ntpservers/create | Create access profile ntp server
[**ntpservers_delete**](NtpServersApi.md#ntpservers_delete) | **DELETE** /api/v1/ntpservers/{id} | Delete access profile ntp server
[**ntpservers_edit**](NtpServersApi.md#ntpservers_edit) | **PUT** /api/v1/ntpservers/edit/{id} | Edit access profile ntp server
[**ntpservers_list**](NtpServersApi.md#ntpservers_list) | **GET** /api/v1/ntpservers/list/{accessProfileId} | List ntp server by access profile id


# **ntpservers_create**
> ApiResponse ntpservers_create(create_ntp_server_command=create_ntp_server_command)

Create access profile ntp server

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_ntp_server_command import CreateNtpServerCommand
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
    api_instance = taikunpycore.NtpServersApi(api_client)
    create_ntp_server_command = {"address":"8.8.8.8","accessProfileId":1} # CreateNtpServerCommand |  (optional)

    try:
        # Create access profile ntp server
        api_response = api_instance.ntpservers_create(create_ntp_server_command=create_ntp_server_command)
        print("The response of NtpServersApi->ntpservers_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NtpServersApi->ntpservers_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ntp_server_command** | [**CreateNtpServerCommand**](CreateNtpServerCommand.md)|  | [optional] 

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

# **ntpservers_delete**
> ntpservers_delete(id)

Delete access profile ntp server

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
    api_instance = taikunpycore.NtpServersApi(api_client)
    id = 56 # int | 

    try:
        # Delete access profile ntp server
        api_instance.ntpservers_delete(id)
    except Exception as e:
        print("Exception when calling NtpServersApi->ntpservers_delete: %s\n" % e)
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

# **ntpservers_edit**
> ntpservers_edit(id, dns_ntp_address_edit_dto=dns_ntp_address_edit_dto)

Edit access profile ntp server

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
    api_instance = taikunpycore.NtpServersApi(api_client)
    id = 56 # int | 
    dns_ntp_address_edit_dto = {"address":"8.8.8.8"} # DnsNtpAddressEditDto |  (optional)

    try:
        # Edit access profile ntp server
        api_instance.ntpservers_edit(id, dns_ntp_address_edit_dto=dns_ntp_address_edit_dto)
    except Exception as e:
        print("Exception when calling NtpServersApi->ntpservers_edit: %s\n" % e)
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

# **ntpservers_list**
> List[NtpServersListDto] ntpservers_list(access_profile_id, search=search)

List ntp server by access profile id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.ntp_servers_list_dto import NtpServersListDto
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
    api_instance = taikunpycore.NtpServersApi(api_client)
    access_profile_id = 56 # int | 
    search = 'search_example' # str |  (optional)

    try:
        # List ntp server by access profile id
        api_response = api_instance.ntpservers_list(access_profile_id, search=search)
        print("The response of NtpServersApi->ntpservers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NtpServersApi->ntpservers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_profile_id** | **int**|  | 
 **search** | **str**|  | [optional] 

### Return type

[**List[NtpServersListDto]**](NtpServersListDto.md)

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

