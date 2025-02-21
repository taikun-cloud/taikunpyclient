# taikunpycore.PrometheusBillingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prometheusbillings_create**](PrometheusBillingsApi.md#prometheusbillings_create) | **POST** /api/v1/prometheusbillings | Add prometheus billing
[**prometheusbillings_export_csv**](PrometheusBillingsApi.md#prometheusbillings_export_csv) | **GET** /api/v1/prometheusbillings/export | Export Csv
[**prometheusbillings_grouped_list**](PrometheusBillingsApi.md#prometheusbillings_grouped_list) | **POST** /api/v1/prometheusbillings/grouped | Retrieve a list of grouped prometheus billing
[**prometheusbillings_list**](PrometheusBillingsApi.md#prometheusbillings_list) | **GET** /api/v1/prometheusbillings | Retrieve all prometheus billing


# **prometheusbillings_create**
> object prometheusbillings_create(prometheus_billing_create_command)

Add prometheus billing

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.prometheus_billing_create_command import PrometheusBillingCreateCommand
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
    api_instance = taikunpycore.PrometheusBillingsApi(api_client)
    prometheus_billing_create_command = taikunpycore.PrometheusBillingCreateCommand() # PrometheusBillingCreateCommand | 

    try:
        # Add prometheus billing
        api_response = api_instance.prometheusbillings_create(prometheus_billing_create_command)
        print("The response of PrometheusBillingsApi->prometheusbillings_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusBillingsApi->prometheusbillings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prometheus_billing_create_command** | [**PrometheusBillingCreateCommand**](PrometheusBillingCreateCommand.md)|  | 

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

# **prometheusbillings_export_csv**
> CsvExporter prometheusbillings_export_csv(is_email_enabled, organization_id=organization_id, start_date=start_date, end_date=end_date)

Export Csv

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
    api_instance = taikunpycore.PrometheusBillingsApi(api_client)
    is_email_enabled = True # bool | 
    organization_id = 56 # int |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Export Csv
        api_response = api_instance.prometheusbillings_export_csv(is_email_enabled, organization_id=organization_id, start_date=start_date, end_date=end_date)
        print("The response of PrometheusBillingsApi->prometheusbillings_export_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusBillingsApi->prometheusbillings_export_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_email_enabled** | **bool**|  | 
 **organization_id** | **int**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

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

# **prometheusbillings_grouped_list**
> object prometheusbillings_grouped_list(grouped_prometheus_billing_list_query)

Retrieve a list of grouped prometheus billing

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.grouped_prometheus_billing_list_query import GroupedPrometheusBillingListQuery
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
    api_instance = taikunpycore.PrometheusBillingsApi(api_client)
    grouped_prometheus_billing_list_query = taikunpycore.GroupedPrometheusBillingListQuery() # GroupedPrometheusBillingListQuery | 

    try:
        # Retrieve a list of grouped prometheus billing
        api_response = api_instance.prometheusbillings_grouped_list(grouped_prometheus_billing_list_query)
        print("The response of PrometheusBillingsApi->prometheusbillings_grouped_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusBillingsApi->prometheusbillings_grouped_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouped_prometheus_billing_list_query** | [**GroupedPrometheusBillingListQuery**](GroupedPrometheusBillingListQuery.md)|  | 

### Return type

**object**

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

# **prometheusbillings_list**
> PrometheusBillingInfo prometheusbillings_list(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, start_date=start_date, end_date=end_date, organization_id=organization_id)

Retrieve all prometheus billing

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.prometheus_billing_info import PrometheusBillingInfo
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
    api_instance = taikunpycore.PrometheusBillingsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    organization_id = 56 # int |  (optional)

    try:
        # Retrieve all prometheus billing
        api_response = api_instance.prometheusbillings_list(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, start_date=start_date, end_date=end_date, organization_id=organization_id)
        print("The response of PrometheusBillingsApi->prometheusbillings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusBillingsApi->prometheusbillings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **organization_id** | **int**|  | [optional] 

### Return type

[**PrometheusBillingInfo**](PrometheusBillingInfo.md)

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

