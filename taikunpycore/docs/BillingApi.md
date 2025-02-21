# taikunpycore.BillingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_create**](BillingApi.md#billing_create) | **POST** /api/v1/billing/create | Add billing summary
[**billing_export_csv**](BillingApi.md#billing_export_csv) | **GET** /api/v1/billing/export | Export Csv
[**billing_grouped_list**](BillingApi.md#billing_grouped_list) | **POST** /api/v1/billing/grouped | Retrieve a grouped list of billing summaries
[**billing_list**](BillingApi.md#billing_list) | **GET** /api/v1/billing | Retrieve billing info


# **billing_create**
> object billing_create(create_billing_summary_command=create_billing_summary_command)

Add billing summary

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.create_billing_summary_command import CreateBillingSummaryCommand
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
    api_instance = taikunpycore.BillingApi(api_client)
    create_billing_summary_command = taikunpycore.CreateBillingSummaryCommand() # CreateBillingSummaryCommand |  (optional)

    try:
        # Add billing summary
        api_response = api_instance.billing_create(create_billing_summary_command=create_billing_summary_command)
        print("The response of BillingApi->billing_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->billing_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_billing_summary_command** | [**CreateBillingSummaryCommand**](CreateBillingSummaryCommand.md)|  | [optional] 

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

# **billing_export_csv**
> CsvExporter billing_export_csv(is_email_enabled, organization_id=organization_id, start_date=start_date, end_date=end_date, is_deleted=is_deleted)

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
    api_instance = taikunpycore.BillingApi(api_client)
    is_email_enabled = True # bool | 
    organization_id = 56 # int |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    is_deleted = True # bool |  (optional)

    try:
        # Export Csv
        api_response = api_instance.billing_export_csv(is_email_enabled, organization_id=organization_id, start_date=start_date, end_date=end_date, is_deleted=is_deleted)
        print("The response of BillingApi->billing_export_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->billing_export_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_email_enabled** | **bool**|  | 
 **organization_id** | **int**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **is_deleted** | **bool**|  | [optional] 

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

# **billing_grouped_list**
> List[GroupedBillingInfo] billing_grouped_list(grouped_billing_list_query)

Retrieve a grouped list of billing summaries

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.grouped_billing_info import GroupedBillingInfo
from taikunpycore.models.grouped_billing_list_query import GroupedBillingListQuery
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
    api_instance = taikunpycore.BillingApi(api_client)
    grouped_billing_list_query = taikunpycore.GroupedBillingListQuery() # GroupedBillingListQuery | 

    try:
        # Retrieve a grouped list of billing summaries
        api_response = api_instance.billing_grouped_list(grouped_billing_list_query)
        print("The response of BillingApi->billing_grouped_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->billing_grouped_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouped_billing_list_query** | [**GroupedBillingListQuery**](GroupedBillingListQuery.md)|  | 

### Return type

[**List[GroupedBillingInfo]**](GroupedBillingInfo.md)

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

# **billing_list**
> BillingInfo billing_list(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, start_date=start_date, end_date=end_date, organization_id=organization_id, is_deleted=is_deleted, project_id=project_id)

Retrieve billing info

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.billing_info import BillingInfo
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
    api_instance = taikunpycore.BillingApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    organization_id = 56 # int |  (optional)
    is_deleted = True # bool |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve billing info
        api_response = api_instance.billing_list(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, start_date=start_date, end_date=end_date, organization_id=organization_id, is_deleted=is_deleted, project_id=project_id)
        print("The response of BillingApi->billing_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->billing_list: %s\n" % e)
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
 **is_deleted** | **bool**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**BillingInfo**](BillingInfo.md)

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

