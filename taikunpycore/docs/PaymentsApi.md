# taikunpycore.PaymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_billing_info**](PaymentsApi.md#payment_billing_info) | **GET** /api/v1/payment/billing-info | Get billing info for organization
[**payment_cardinfo**](PaymentsApi.md#payment_cardinfo) | **GET** /api/v1/payment/cardinfo | Get card information
[**payment_clear**](PaymentsApi.md#payment_clear) | **POST** /api/v1/payment/clear | Clear payment
[**payment_create_customer**](PaymentsApi.md#payment_create_customer) | **POST** /api/v1/payment/createcustomer | Create customer
[**payment_final_price**](PaymentsApi.md#payment_final_price) | **POST** /api/v1/payment/finalprice | Fetch final price
[**payment_get_stripe_invoices**](PaymentsApi.md#payment_get_stripe_invoices) | **GET** /api/v1/payment/stripeinvoices/{subscriptionId} | Get required stripe invoices by stripe subscription id
[**payment_pay**](PaymentsApi.md#payment_pay) | **POST** /api/v1/payment/pay | Pay invoice
[**payment_update_card**](PaymentsApi.md#payment_update_card) | **POST** /api/v1/payment/updatecard | Update payment card
[**payment_webhook**](PaymentsApi.md#payment_webhook) | **POST** /api/v1/payment/webhook | Listen to payment webhook


# **payment_billing_info**
> BillingInfoDto payment_billing_info()

Get billing info for organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.billing_info_dto import BillingInfoDto
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
    api_instance = taikunpycore.PaymentsApi(api_client)

    try:
        # Get billing info for organization
        api_response = api_instance.payment_billing_info()
        print("The response of PaymentsApi->payment_billing_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payment_billing_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BillingInfoDto**](BillingInfoDto.md)

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

# **payment_cardinfo**
> CardInformationDto payment_cardinfo(organization_id=organization_id)

Get card information

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.card_information_dto import CardInformationDto
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
    api_instance = taikunpycore.PaymentsApi(api_client)
    organization_id = 56 # int |  (optional)

    try:
        # Get card information
        api_response = api_instance.payment_cardinfo(organization_id=organization_id)
        print("The response of PaymentsApi->payment_cardinfo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payment_cardinfo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 

### Return type

[**CardInformationDto**](CardInformationDto.md)

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

# **payment_clear**
> object payment_clear(body)

Clear payment

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
    api_instance = taikunpycore.PaymentsApi(api_client)
    body = None # object | 

    try:
        # Clear payment
        api_response = api_instance.payment_clear(body)
        print("The response of PaymentsApi->payment_clear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payment_clear: %s\n" % e)
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

# **payment_create_customer**
> object payment_create_customer(create_stripe_customer_command=create_stripe_customer_command)

Create customer

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.create_stripe_customer_command import CreateStripeCustomerCommand
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
    api_instance = taikunpycore.PaymentsApi(api_client)
    create_stripe_customer_command = taikunpycore.CreateStripeCustomerCommand() # CreateStripeCustomerCommand |  (optional)

    try:
        # Create customer
        api_response = api_instance.payment_create_customer(create_stripe_customer_command=create_stripe_customer_command)
        print("The response of PaymentsApi->payment_create_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payment_create_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_stripe_customer_command** | [**CreateStripeCustomerCommand**](CreateStripeCustomerCommand.md)|  | [optional] 

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

# **payment_final_price**
> FinalPriceDto payment_final_price(final_price_command)

Fetch final price

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.final_price_command import FinalPriceCommand
from taikunpycore.models.final_price_dto import FinalPriceDto
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
    api_instance = taikunpycore.PaymentsApi(api_client)
    final_price_command = taikunpycore.FinalPriceCommand() # FinalPriceCommand | 

    try:
        # Fetch final price
        api_response = api_instance.payment_final_price(final_price_command)
        print("The response of PaymentsApi->payment_final_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payment_final_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **final_price_command** | [**FinalPriceCommand**](FinalPriceCommand.md)|  | 

### Return type

[**FinalPriceDto**](FinalPriceDto.md)

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

# **payment_get_stripe_invoices**
> StripeInvoices payment_get_stripe_invoices(subscription_id)

Get required stripe invoices by stripe subscription id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.stripe_invoices import StripeInvoices
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
    api_instance = taikunpycore.PaymentsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Get required stripe invoices by stripe subscription id
        api_response = api_instance.payment_get_stripe_invoices(subscription_id)
        print("The response of PaymentsApi->payment_get_stripe_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payment_get_stripe_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**StripeInvoices**](StripeInvoices.md)

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

# **payment_pay**
> payment_pay(pay_invoice_command)

Pay invoice

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.pay_invoice_command import PayInvoiceCommand
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
    api_instance = taikunpycore.PaymentsApi(api_client)
    pay_invoice_command = taikunpycore.PayInvoiceCommand() # PayInvoiceCommand | 

    try:
        # Pay invoice
        api_instance.payment_pay(pay_invoice_command)
    except Exception as e:
        print("Exception when calling PaymentsApi->payment_pay: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_invoice_command** | [**PayInvoiceCommand**](PayInvoiceCommand.md)|  | 

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

# **payment_update_card**
> object payment_update_card(change_card_command)

Update payment card

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.change_card_command import ChangeCardCommand
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
    api_instance = taikunpycore.PaymentsApi(api_client)
    change_card_command = taikunpycore.ChangeCardCommand() # ChangeCardCommand | 

    try:
        # Update payment card
        api_response = api_instance.payment_update_card(change_card_command)
        print("The response of PaymentsApi->payment_update_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payment_update_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_card_command** | [**ChangeCardCommand**](ChangeCardCommand.md)|  | 

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

# **payment_webhook**
> object payment_webhook(body)

Listen to payment webhook

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
    api_instance = taikunpycore.PaymentsApi(api_client)
    body = None # object | 

    try:
        # Listen to payment webhook
        api_response = api_instance.payment_webhook(body)
        print("The response of PaymentsApi->payment_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payment_webhook: %s\n" % e)
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

