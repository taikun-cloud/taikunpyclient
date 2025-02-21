# taikunpycore.CommonApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**common_countries**](CommonApi.md#common_countries) | **GET** /api/v1/common/countries | Retrieve country list
[**common_enum_values**](CommonApi.md#common_enum_values) | **GET** /api/v1/common/enumvalues | Retrieve enum values
[**common_ip_range_count**](CommonApi.md#common_ip_range_count) | **POST** /api/v1/common/ip-range-count | Retrieve ip address range count
[**common_ip_range_list**](CommonApi.md#common_ip_range_list) | **POST** /api/v1/common/ip-range-list | Retrieve ip address range list
[**common_sorting_elements**](CommonApi.md#common_sorting_elements) | **GET** /api/v1/common/sorting-elements/{type} | Retrieve sorting values


# **common_countries**
> List[CountryListDto] common_countries(search=search)

Retrieve country list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.country_list_dto import CountryListDto
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
    api_instance = taikunpycore.CommonApi(api_client)
    search = 'search_example' # str |  (optional)

    try:
        # Retrieve country list
        api_response = api_instance.common_countries(search=search)
        print("The response of CommonApi->common_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonApi->common_countries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 

### Return type

[**List[CountryListDto]**](CountryListDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_enum_values**
> EnumList common_enum_values()

Retrieve enum values

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.enum_list import EnumList
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
    api_instance = taikunpycore.CommonApi(api_client)

    try:
        # Retrieve enum values
        api_response = api_instance.common_enum_values()
        print("The response of CommonApi->common_enum_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonApi->common_enum_values: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EnumList**](EnumList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_ip_range_count**
> int common_ip_range_count(ip_address_range_count_command)

Retrieve ip address range count

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.ip_address_range_count_command import IpAddressRangeCountCommand
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
    api_instance = taikunpycore.CommonApi(api_client)
    ip_address_range_count_command = taikunpycore.IpAddressRangeCountCommand() # IpAddressRangeCountCommand | 

    try:
        # Retrieve ip address range count
        api_response = api_instance.common_ip_range_count(ip_address_range_count_command)
        print("The response of CommonApi->common_ip_range_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonApi->common_ip_range_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address_range_count_command** | [**IpAddressRangeCountCommand**](IpAddressRangeCountCommand.md)|  | 

### Return type

**int**

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

# **common_ip_range_list**
> List[str] common_ip_range_list(ip_address_range_list_command)

Retrieve ip address range list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.ip_address_range_list_command import IpAddressRangeListCommand
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
    api_instance = taikunpycore.CommonApi(api_client)
    ip_address_range_list_command = taikunpycore.IpAddressRangeListCommand() # IpAddressRangeListCommand | 

    try:
        # Retrieve ip address range list
        api_response = api_instance.common_ip_range_list(ip_address_range_list_command)
        print("The response of CommonApi->common_ip_range_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonApi->common_ip_range_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address_range_list_command** | [**IpAddressRangeListCommand**](IpAddressRangeListCommand.md)|  | 

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

# **common_sorting_elements**
> List[str] common_sorting_elements(type)

Retrieve sorting values

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
    api_instance = taikunpycore.CommonApi(api_client)
    type = 'type_example' # str | 

    try:
        # Retrieve sorting values
        api_response = api_instance.common_sorting_elements(type)
        print("The response of CommonApi->common_sorting_elements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonApi->common_sorting_elements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

**List[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

