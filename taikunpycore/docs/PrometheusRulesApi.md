# taikunpycore.PrometheusRulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prometheusrules_add_organizations**](PrometheusRulesApi.md#prometheusrules_add_organizations) | **POST** /api/v1/prometheusrules/{id}/organizations | Add organizations to prometheus rule
[**prometheusrules_create**](PrometheusRulesApi.md#prometheusrules_create) | **POST** /api/v1/prometheusrules | Add prometheus rule
[**prometheusrules_delete**](PrometheusRulesApi.md#prometheusrules_delete) | **DELETE** /api/v1/prometheusrules/{id} | Remove prometheus rule
[**prometheusrules_delete_organizations**](PrometheusRulesApi.md#prometheusrules_delete_organizations) | **PUT** /api/v1/prometheusrules/{id}/organizations | Delete organizations from prometheus rule
[**prometheusrules_details**](PrometheusRulesApi.md#prometheusrules_details) | **GET** /api/v1/prometheusrules/details | Retrieve all prometheus rules with detailed info
[**prometheusrules_list**](PrometheusRulesApi.md#prometheusrules_list) | **GET** /api/v1/prometheusrules | Retrieve a list of prometheus rules
[**prometheusrules_update**](PrometheusRulesApi.md#prometheusrules_update) | **PUT** /api/v1/prometheusrules/edit/{id} | Edit prometheus rule


# **prometheusrules_add_organizations**
> object prometheusrules_add_organizations(id, add_organizations_to_rule_dto=add_organizations_to_rule_dto)

Add organizations to prometheus rule

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.add_organizations_to_rule_dto import AddOrganizationsToRuleDto
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
    api_instance = taikunpycore.PrometheusRulesApi(api_client)
    id = 56 # int | 
    add_organizations_to_rule_dto = [taikunpycore.AddOrganizationsToRuleDto()] # List[AddOrganizationsToRuleDto] |  (optional)

    try:
        # Add organizations to prometheus rule
        api_response = api_instance.prometheusrules_add_organizations(id, add_organizations_to_rule_dto=add_organizations_to_rule_dto)
        print("The response of PrometheusRulesApi->prometheusrules_add_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusRulesApi->prometheusrules_add_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **add_organizations_to_rule_dto** | [**List[AddOrganizationsToRuleDto]**](AddOrganizationsToRuleDto.md)|  | [optional] 

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

# **prometheusrules_create**
> ApiResponse prometheusrules_create(rule_create_command=rule_create_command)

Add prometheus rule

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.rule_create_command import RuleCreateCommand
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
    api_instance = taikunpycore.PrometheusRulesApi(api_client)
    rule_create_command = taikunpycore.RuleCreateCommand() # RuleCreateCommand |  (optional)

    try:
        # Add prometheus rule
        api_response = api_instance.prometheusrules_create(rule_create_command=rule_create_command)
        print("The response of PrometheusRulesApi->prometheusrules_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusRulesApi->prometheusrules_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_create_command** | [**RuleCreateCommand**](RuleCreateCommand.md)|  | [optional] 

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

# **prometheusrules_delete**
> prometheusrules_delete(id)

Remove prometheus rule

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
    api_instance = taikunpycore.PrometheusRulesApi(api_client)
    id = 56 # int | 

    try:
        # Remove prometheus rule
        api_instance.prometheusrules_delete(id)
    except Exception as e:
        print("Exception when calling PrometheusRulesApi->prometheusrules_delete: %s\n" % e)
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

# **prometheusrules_delete_organizations**
> object prometheusrules_delete_organizations(id, request_body=request_body)

Delete organizations from prometheus rule

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
    api_instance = taikunpycore.PrometheusRulesApi(api_client)
    id = 56 # int | 
    request_body = [56] # List[int] |  (optional)

    try:
        # Delete organizations from prometheus rule
        api_response = api_instance.prometheusrules_delete_organizations(id, request_body=request_body)
        print("The response of PrometheusRulesApi->prometheusrules_delete_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusRulesApi->prometheusrules_delete_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **request_body** | [**List[int]**](int.md)|  | [optional] 

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

# **prometheusrules_details**
> List[CommonDropdownIsBoundDto] prometheusrules_details(organization_id=organization_id)

Retrieve all prometheus rules with detailed info

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_dropdown_is_bound_dto import CommonDropdownIsBoundDto
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
    api_instance = taikunpycore.PrometheusRulesApi(api_client)
    organization_id = 56 # int |  (optional)

    try:
        # Retrieve all prometheus rules with detailed info
        api_response = api_instance.prometheusrules_details(organization_id=organization_id)
        print("The response of PrometheusRulesApi->prometheusrules_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusRulesApi->prometheusrules_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 

### Return type

[**List[CommonDropdownIsBoundDto]**](CommonDropdownIsBoundDto.md)

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

# **prometheusrules_list**
> PrometheusRulesList prometheusrules_list(limit=limit, offset=offset, partner_id=partner_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)

Retrieve a list of prometheus rules

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.prometheus_rules_list import PrometheusRulesList
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
    api_instance = taikunpycore.PrometheusRulesApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    partner_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve a list of prometheus rules
        api_response = api_instance.prometheusrules_list(limit=limit, offset=offset, partner_id=partner_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)
        print("The response of PrometheusRulesApi->prometheusrules_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusRulesApi->prometheusrules_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **partner_id** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 

### Return type

[**PrometheusRulesList**](PrometheusRulesList.md)

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

# **prometheusrules_update**
> object prometheusrules_update(id, rule_for_update_dto=rule_for_update_dto)

Edit prometheus rule

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.rule_for_update_dto import RuleForUpdateDto
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
    api_instance = taikunpycore.PrometheusRulesApi(api_client)
    id = 56 # int | 
    rule_for_update_dto = taikunpycore.RuleForUpdateDto() # RuleForUpdateDto |  (optional)

    try:
        # Edit prometheus rule
        api_response = api_instance.prometheusrules_update(id, rule_for_update_dto=rule_for_update_dto)
        print("The response of PrometheusRulesApi->prometheusrules_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusRulesApi->prometheusrules_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **rule_for_update_dto** | [**RuleForUpdateDto**](RuleForUpdateDto.md)|  | [optional] 

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

