# taikunpycore.InfraBillingSummaryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**infra_billing_summary_create**](InfraBillingSummaryApi.md#infra_billing_summary_create) | **POST** /api/v1/infra-billing-summary/create | Add infra billing summary
[**infra_billing_summary_list**](InfraBillingSummaryApi.md#infra_billing_summary_list) | **POST** /api/v1/infra-billing-summary/list | Retrieve infra billing info


# **infra_billing_summary_create**
> object infra_billing_summary_create(infra_billing_summaries_create_command=infra_billing_summaries_create_command)

Add infra billing summary

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.infra_billing_summaries_create_command import InfraBillingSummariesCreateCommand
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
    api_instance = taikunpycore.InfraBillingSummaryApi(api_client)
    infra_billing_summaries_create_command = taikunpycore.InfraBillingSummariesCreateCommand() # InfraBillingSummariesCreateCommand |  (optional)

    try:
        # Add infra billing summary
        api_response = api_instance.infra_billing_summary_create(infra_billing_summaries_create_command=infra_billing_summaries_create_command)
        print("The response of InfraBillingSummaryApi->infra_billing_summary_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingSummaryApi->infra_billing_summary_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_billing_summaries_create_command** | [**InfraBillingSummariesCreateCommand**](InfraBillingSummariesCreateCommand.md)|  | [optional] 

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

# **infra_billing_summary_list**
> List[InfraBillingSummaryDto] infra_billing_summary_list(infra_billing_list_command)

Retrieve infra billing info

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.infra_billing_list_command import InfraBillingListCommand
from taikunpycore.models.infra_billing_summary_dto import InfraBillingSummaryDto
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
    api_instance = taikunpycore.InfraBillingSummaryApi(api_client)
    infra_billing_list_command = taikunpycore.InfraBillingListCommand() # InfraBillingListCommand | 

    try:
        # Retrieve infra billing info
        api_response = api_instance.infra_billing_summary_list(infra_billing_list_command)
        print("The response of InfraBillingSummaryApi->infra_billing_summary_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingSummaryApi->infra_billing_summary_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_billing_list_command** | [**InfraBillingListCommand**](InfraBillingListCommand.md)|  | 

### Return type

[**List[InfraBillingSummaryDto]**](InfraBillingSummaryDto.md)

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

