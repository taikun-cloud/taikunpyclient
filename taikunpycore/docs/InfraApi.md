# taikunpycore.InfraApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**infra_create**](InfraApi.md#infra_create) | **POST** /api/v1/infra/create | Create infra product
[**infra_details**](InfraApi.md#infra_details) | **GET** /api/v1/infra/details | Retrieve infra details
[**infra_organizations_list**](InfraApi.md#infra_organizations_list) | **GET** /api/v1/infra/organizations-list | Retrieve infra products list
[**infra_product_list**](InfraApi.md#infra_product_list) | **GET** /api/v1/infra/list | Retrieve infra products list


# **infra_create**
> object infra_create(create_infra_product_command)

Create infra product

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.create_infra_product_command import CreateInfraProductCommand
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
    api_instance = taikunpycore.InfraApi(api_client)
    create_infra_product_command = taikunpycore.CreateInfraProductCommand() # CreateInfraProductCommand | 

    try:
        # Create infra product
        api_response = api_instance.infra_create(create_infra_product_command)
        print("The response of InfraApi->infra_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraApi->infra_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_infra_product_command** | [**CreateInfraProductCommand**](CreateInfraProductCommand.md)|  | 

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

# **infra_details**
> OpenstackQuotaList infra_details(organization_id=organization_id)

Retrieve infra details

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.openstack_quota_list import OpenstackQuotaList
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
    api_instance = taikunpycore.InfraApi(api_client)
    organization_id = 56 # int |  (optional)

    try:
        # Retrieve infra details
        api_response = api_instance.infra_details(organization_id=organization_id)
        print("The response of InfraApi->infra_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraApi->infra_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 

### Return type

[**OpenstackQuotaList**](OpenstackQuotaList.md)

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

# **infra_organizations_list**
> List[InfraOrganizationsListDto] infra_organizations_list()

Retrieve infra products list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.infra_organizations_list_dto import InfraOrganizationsListDto
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
    api_instance = taikunpycore.InfraApi(api_client)

    try:
        # Retrieve infra products list
        api_response = api_instance.infra_organizations_list()
        print("The response of InfraApi->infra_organizations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraApi->infra_organizations_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[InfraOrganizationsListDto]**](InfraOrganizationsListDto.md)

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

# **infra_product_list**
> List[InfraProductDto] infra_product_list()

Retrieve infra products list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.infra_product_dto import InfraProductDto
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
    api_instance = taikunpycore.InfraApi(api_client)

    try:
        # Retrieve infra products list
        api_response = api_instance.infra_product_list()
        print("The response of InfraApi->infra_product_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraApi->infra_product_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[InfraProductDto]**](InfraProductDto.md)

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

