# taikunpycore.InvoicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoices_create**](InvoicesApi.md#invoices_create) | **POST** /api/v1/invoices/create | Create invoice
[**invoices_download**](InvoicesApi.md#invoices_download) | **POST** /api/v1/invoices/download | Download invoice
[**invoices_list**](InvoicesApi.md#invoices_list) | **GET** /api/v1/invoices/list | Invoices list
[**invoices_update**](InvoicesApi.md#invoices_update) | **PUT** /api/v1/invoices/update/{invoiceId} | Update invoice


# **invoices_create**
> int invoices_create(create_invoice_command=create_invoice_command)

Create invoice

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.create_invoice_command import CreateInvoiceCommand
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
    api_instance = taikunpycore.InvoicesApi(api_client)
    create_invoice_command = taikunpycore.CreateInvoiceCommand() # CreateInvoiceCommand |  (optional)

    try:
        # Create invoice
        api_response = api_instance.invoices_create(create_invoice_command=create_invoice_command)
        print("The response of InvoicesApi->invoices_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_invoice_command** | [**CreateInvoiceCommand**](CreateInvoiceCommand.md)|  | [optional] 

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

# **invoices_download**
> CsvExporter invoices_download(download_invoice_command)

Download invoice

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.csv_exporter import CsvExporter
from taikunpycore.models.download_invoice_command import DownloadInvoiceCommand
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
    api_instance = taikunpycore.InvoicesApi(api_client)
    download_invoice_command = taikunpycore.DownloadInvoiceCommand() # DownloadInvoiceCommand | 

    try:
        # Download invoice
        api_response = api_instance.invoices_download(download_invoice_command)
        print("The response of InvoicesApi->invoices_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_invoice_command** | [**DownloadInvoiceCommand**](DownloadInvoiceCommand.md)|  | 

### Return type

[**CsvExporter**](CsvExporter.md)

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

# **invoices_list**
> Invoices invoices_list(offset=offset, limit=limit, start_date=start_date, end_date=end_date, search=search, filter_by=filter_by, sort_by=sort_by, sort_direction=sort_direction, organization_id=organization_id, partner_id=partner_id)

Invoices list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.invoices import Invoices
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
    api_instance = taikunpycore.InvoicesApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    search = 'search_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    organization_id = 56 # int |  (optional)
    partner_id = 56 # int |  (optional)

    try:
        # Invoices list
        api_response = api_instance.invoices_list(offset=offset, limit=limit, start_date=start_date, end_date=end_date, search=search, filter_by=filter_by, sort_by=sort_by, sort_direction=sort_direction, organization_id=organization_id, partner_id=partner_id)
        print("The response of InvoicesApi->invoices_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **search** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **partner_id** | **int**|  | [optional] 

### Return type

[**Invoices**](Invoices.md)

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

# **invoices_update**
> object invoices_update(invoice_id, update_invoice_dto=update_invoice_dto)

Update invoice

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_invoice_dto import UpdateInvoiceDto
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
    api_instance = taikunpycore.InvoicesApi(api_client)
    invoice_id = 56 # int | 
    update_invoice_dto = taikunpycore.UpdateInvoiceDto() # UpdateInvoiceDto |  (optional)

    try:
        # Update invoice
        api_response = api_instance.invoices_update(invoice_id, update_invoice_dto=update_invoice_dto)
        print("The response of InvoicesApi->invoices_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**|  | 
 **update_invoice_dto** | [**UpdateInvoiceDto**](UpdateInvoiceDto.md)|  | [optional] 

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

