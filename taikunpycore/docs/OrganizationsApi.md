# taikunpycore.OrganizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_accept_offer**](OrganizationsApi.md#organizations_accept_offer) | **POST** /api/v1/organizations/accept-offer | Accept discount offer
[**organizations_access_for_partner**](OrganizationsApi.md#organizations_access_for_partner) | **POST** /api/v1/organizations/access-for partner | Give access to partner
[**organizations_add_prometheusrules**](OrganizationsApi.md#organizations_add_prometheusrules) | **POST** /api/v1/organizations/{id}/prometheusrules | Add prometheus rule(s) to organization
[**organizations_create**](OrganizationsApi.md#organizations_create) | **POST** /api/v1/organizations | Add a new organization. Only available for admins.
[**organizations_delete**](OrganizationsApi.md#organizations_delete) | **DELETE** /api/v1/organizations/{id} | Delete the specified organization. Only available for admins.
[**organizations_delete_prometheusrules**](OrganizationsApi.md#organizations_delete_prometheusrules) | **PUT** /api/v1/organizations/{id}/prometheusrules | Delete prometheus rule(s) from organization
[**organizations_detawils**](OrganizationsApi.md#organizations_detawils) | **GET** /api/v1/organizations/details | Retrieve all data about current organization by Id
[**organizations_export_csv**](OrganizationsApi.md#organizations_export_csv) | **GET** /api/v1/organizations/export | Export Csv file
[**organizations_leave**](OrganizationsApi.md#organizations_leave) | **POST** /api/v1/organizations/leave | Leave taikun
[**organizations_list**](OrganizationsApi.md#organizations_list) | **GET** /api/v1/organizations | Retrieve all organizations
[**organizations_organization_list**](OrganizationsApi.md#organizations_organization_list) | **GET** /api/v1/organizations/list | Retrieve organizations
[**organizations_toggle**](OrganizationsApi.md#organizations_toggle) | **POST** /api/v1/organizations/toggle/keycloak | Toggle keycloak login option
[**organizations_update**](OrganizationsApi.md#organizations_update) | **POST** /api/v1/organizations/update | Update organization by Id
[**organizations_update_payment**](OrganizationsApi.md#organizations_update_payment) | **POST** /api/v1/organizations/updatepaymentmethod | Update organization payment Id


# **organizations_accept_offer**
> object organizations_accept_offer(body)

Accept discount offer

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
    api_instance = taikunpycore.OrganizationsApi(api_client)
    body = None # object | 

    try:
        # Accept discount offer
        api_response = api_instance.organizations_accept_offer(body)
        print("The response of OrganizationsApi->organizations_accept_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_accept_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

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

# **organizations_access_for_partner**
> object organizations_access_for_partner(give_access_to_partner_command)

Give access to partner

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.give_access_to_partner_command import GiveAccessToPartnerCommand
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
    api_instance = taikunpycore.OrganizationsApi(api_client)
    give_access_to_partner_command = taikunpycore.GiveAccessToPartnerCommand() # GiveAccessToPartnerCommand | 

    try:
        # Give access to partner
        api_response = api_instance.organizations_access_for_partner(give_access_to_partner_command)
        print("The response of OrganizationsApi->organizations_access_for_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_access_for_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **give_access_to_partner_command** | [**GiveAccessToPartnerCommand**](GiveAccessToPartnerCommand.md)|  | 

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

# **organizations_add_prometheusrules**
> object organizations_add_prometheusrules(id, add_prometheus_rules_to_organization_dto=add_prometheus_rules_to_organization_dto)

Add prometheus rule(s) to organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.add_prometheus_rules_to_organization_dto import AddPrometheusRulesToOrganizationDto
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
    api_instance = taikunpycore.OrganizationsApi(api_client)
    id = 56 # int | 
    add_prometheus_rules_to_organization_dto = [taikunpycore.AddPrometheusRulesToOrganizationDto()] # List[AddPrometheusRulesToOrganizationDto] |  (optional)

    try:
        # Add prometheus rule(s) to organization
        api_response = api_instance.organizations_add_prometheusrules(id, add_prometheus_rules_to_organization_dto=add_prometheus_rules_to_organization_dto)
        print("The response of OrganizationsApi->organizations_add_prometheusrules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_add_prometheusrules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **add_prometheus_rules_to_organization_dto** | [**List[AddPrometheusRulesToOrganizationDto]**](AddPrometheusRulesToOrganizationDto.md)|  | [optional] 

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

# **organizations_create**
> ApiResponse organizations_create(organization_create_command=organization_create_command)

Add a new organization. Only available for admins.

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.organization_create_command import OrganizationCreateCommand
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
    api_instance = taikunpycore.OrganizationsApi(api_client)
    organization_create_command = taikunpycore.OrganizationCreateCommand() # OrganizationCreateCommand |  (optional)

    try:
        # Add a new organization. Only available for admins.
        api_response = api_instance.organizations_create(organization_create_command=organization_create_command)
        print("The response of OrganizationsApi->organizations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_create_command** | [**OrganizationCreateCommand**](OrganizationCreateCommand.md)|  | [optional] 

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

# **organizations_delete**
> organizations_delete(id)

Delete the specified organization. Only available for admins.

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
    api_instance = taikunpycore.OrganizationsApi(api_client)
    id = 56 # int | 

    try:
        # Delete the specified organization. Only available for admins.
        api_instance.organizations_delete(id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_delete: %s\n" % e)
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

# **organizations_delete_prometheusrules**
> object organizations_delete_prometheusrules(id, request_body=request_body)

Delete prometheus rule(s) from organization

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
    api_instance = taikunpycore.OrganizationsApi(api_client)
    id = 56 # int | 
    request_body = [56] # List[int] |  (optional)

    try:
        # Delete prometheus rule(s) from organization
        api_response = api_instance.organizations_delete_prometheusrules(id, request_body=request_body)
        print("The response of OrganizationsApi->organizations_delete_prometheusrules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_delete_prometheusrules: %s\n" % e)
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

# **organizations_detawils**
> DashboardChart organizations_detawils(organization_id=organization_id)

Retrieve all data about current organization by Id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.dashboard_chart import DashboardChart
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
    api_instance = taikunpycore.OrganizationsApi(api_client)
    organization_id = 56 # int |  (optional)

    try:
        # Retrieve all data about current organization by Id
        api_response = api_instance.organizations_detawils(organization_id=organization_id)
        print("The response of OrganizationsApi->organizations_detawils:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_detawils: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 

### Return type

[**DashboardChart**](DashboardChart.md)

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

# **organizations_export_csv**
> CsvExporter organizations_export_csv()

Export Csv file

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.csv_exporter import CsvExporter
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
    api_instance = taikunpycore.OrganizationsApi(api_client)

    try:
        # Export Csv file
        api_response = api_instance.organizations_export_csv()
        print("The response of OrganizationsApi->organizations_export_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_export_csv: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CsvExporter**](CsvExporter.md)

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

# **organizations_leave**
> LeaveTaikunDto organizations_leave(leave_taikun_command)

Leave taikun

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.leave_taikun_command import LeaveTaikunCommand
from taikunpycore.models.leave_taikun_dto import LeaveTaikunDto
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
    api_instance = taikunpycore.OrganizationsApi(api_client)
    leave_taikun_command = taikunpycore.LeaveTaikunCommand() # LeaveTaikunCommand | 

    try:
        # Leave taikun
        api_response = api_instance.organizations_leave(leave_taikun_command)
        print("The response of OrganizationsApi->organizations_leave:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_leave: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leave_taikun_command** | [**LeaveTaikunCommand**](LeaveTaikunCommand.md)|  | 

### Return type

[**LeaveTaikunDto**](LeaveTaikunDto.md)

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

# **organizations_list**
> OrganizationsList organizations_list(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)

Retrieve all organizations

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.organizations_list import OrganizationsList
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
    api_instance = taikunpycore.OrganizationsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve all organizations
        api_response = api_instance.organizations_list(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)
        print("The response of OrganizationsApi->organizations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 

### Return type

[**OrganizationsList**](OrganizationsList.md)

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

# **organizations_organization_list**
> List[OrganizationDropdownDto] organizations_organization_list(partner_id=partner_id, search=search, is_infra=is_infra, prometheus_rule_id=prometheus_rule_id)

Retrieve organizations

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.organization_dropdown_dto import OrganizationDropdownDto
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
    api_instance = taikunpycore.OrganizationsApi(api_client)
    partner_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    is_infra = True # bool |  (optional)
    prometheus_rule_id = 56 # int |  (optional)

    try:
        # Retrieve organizations
        api_response = api_instance.organizations_organization_list(partner_id=partner_id, search=search, is_infra=is_infra, prometheus_rule_id=prometheus_rule_id)
        print("The response of OrganizationsApi->organizations_organization_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_organization_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **is_infra** | **bool**|  | [optional] 
 **prometheus_rule_id** | **int**|  | [optional] 

### Return type

[**List[OrganizationDropdownDto]**](OrganizationDropdownDto.md)

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

# **organizations_toggle**
> object organizations_toggle(toggle_keycloak_command)

Toggle keycloak login option

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.toggle_keycloak_command import ToggleKeycloakCommand
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
    api_instance = taikunpycore.OrganizationsApi(api_client)
    toggle_keycloak_command = taikunpycore.ToggleKeycloakCommand() # ToggleKeycloakCommand | 

    try:
        # Toggle keycloak login option
        api_response = api_instance.organizations_toggle(toggle_keycloak_command)
        print("The response of OrganizationsApi->organizations_toggle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_toggle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toggle_keycloak_command** | [**ToggleKeycloakCommand**](ToggleKeycloakCommand.md)|  | 

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

# **organizations_update**
> object organizations_update(update_organization_command=update_organization_command)

Update organization by Id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_organization_command import UpdateOrganizationCommand
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
    api_instance = taikunpycore.OrganizationsApi(api_client)
    update_organization_command = taikunpycore.UpdateOrganizationCommand() # UpdateOrganizationCommand |  (optional)

    try:
        # Update organization by Id
        api_response = api_instance.organizations_update(update_organization_command=update_organization_command)
        print("The response of OrganizationsApi->organizations_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_organization_command** | [**UpdateOrganizationCommand**](UpdateOrganizationCommand.md)|  | [optional] 

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

# **organizations_update_payment**
> object organizations_update_payment(update_payment_id_command)

Update organization payment Id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_payment_id_command import UpdatePaymentIdCommand
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
    api_instance = taikunpycore.OrganizationsApi(api_client)
    update_payment_id_command = taikunpycore.UpdatePaymentIdCommand() # UpdatePaymentIdCommand | 

    try:
        # Update organization payment Id
        api_response = api_instance.organizations_update_payment(update_payment_id_command)
        print("The response of OrganizationsApi->organizations_update_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_update_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_payment_id_command** | [**UpdatePaymentIdCommand**](UpdatePaymentIdCommand.md)|  | 

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

