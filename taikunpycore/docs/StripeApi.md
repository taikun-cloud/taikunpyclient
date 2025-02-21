# taikunpycore.StripeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stripe_subscription_item_list**](StripeApi.md#stripe_subscription_item_list) | **GET** /api/v1/stripe/{subscriptionId} | Get subscription item list


# **stripe_subscription_item_list**
> List[StripeSubscriptionItemDto] stripe_subscription_item_list(subscription_id)

Get subscription item list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.stripe_subscription_item_dto import StripeSubscriptionItemDto
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
    api_instance = taikunpycore.StripeApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Get subscription item list
        api_response = api_instance.stripe_subscription_item_list(subscription_id)
        print("The response of StripeApi->stripe_subscription_item_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->stripe_subscription_item_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**List[StripeSubscriptionItemDto]**](StripeSubscriptionItemDto.md)

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

