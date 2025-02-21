# taikunpycore.PartnersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**partner_add_organizations**](PartnersApi.md#partner_add_organizations) | **POST** /api/v1/partner/{id}/organizations | Add organizations to a partner
[**partner_add_whitelist_domain**](PartnersApi.md#partner_add_whitelist_domain) | **POST** /api/v1/partner/add/whitelist/domain | Add white list domain
[**partner_become_a_partner**](PartnersApi.md#partner_become_a_partner) | **POST** /api/v1/partner/become-a-partner | Become a partner
[**partner_contact_us**](PartnersApi.md#partner_contact_us) | **POST** /api/v1/partner/contact-us | Contact with us
[**partner_create**](PartnersApi.md#partner_create) | **POST** /api/v1/partner/create | Add a partner
[**partner_delete_organizations**](PartnersApi.md#partner_delete_organizations) | **PUT** /api/v1/partner/{id}/organizations | Delete organizations from a partner
[**partner_delete_whitelist_domain**](PartnersApi.md#partner_delete_whitelist_domain) | **POST** /api/v1/partner/delete/whitelist/domain | Delete white list domain
[**partner_details**](PartnersApi.md#partner_details) | **GET** /api/v1/partner/details | Details of partners
[**partner_dropdown**](PartnersApi.md#partner_dropdown) | **GET** /api/v1/partner/list | Get partners dropdown
[**partner_info**](PartnersApi.md#partner_info) | **GET** /api/v1/partner/info | Get partner&#39;s registration info
[**partner_list**](PartnersApi.md#partner_list) | **GET** /api/v1/partner | Get partners
[**partner_update**](PartnersApi.md#partner_update) | **PUT** /api/v1/partner/update | Edit partner&#39;s data by Id


# **partner_add_organizations**
> object partner_add_organizations(id, request_body=request_body)

Add organizations to a partner

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
    api_instance = taikunpycore.PartnersApi(api_client)
    id = 56 # int | 
    request_body = [56] # List[int] |  (optional)

    try:
        # Add organizations to a partner
        api_response = api_instance.partner_add_organizations(id, request_body=request_body)
        print("The response of PartnersApi->partner_add_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnersApi->partner_add_organizations: %s\n" % e)
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

# **partner_add_whitelist_domain**
> object partner_add_whitelist_domain(white_list_domain_create_command=white_list_domain_create_command)

Add white list domain

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.white_list_domain_create_command import WhiteListDomainCreateCommand
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
    api_instance = taikunpycore.PartnersApi(api_client)
    white_list_domain_create_command = taikunpycore.WhiteListDomainCreateCommand() # WhiteListDomainCreateCommand |  (optional)

    try:
        # Add white list domain
        api_response = api_instance.partner_add_whitelist_domain(white_list_domain_create_command=white_list_domain_create_command)
        print("The response of PartnersApi->partner_add_whitelist_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnersApi->partner_add_whitelist_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **white_list_domain_create_command** | [**WhiteListDomainCreateCommand**](WhiteListDomainCreateCommand.md)|  | [optional] 

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

# **partner_become_a_partner**
> object partner_become_a_partner(become_partner_command=become_partner_command)

Become a partner

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.become_partner_command import BecomePartnerCommand
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
    api_instance = taikunpycore.PartnersApi(api_client)
    become_partner_command = taikunpycore.BecomePartnerCommand() # BecomePartnerCommand |  (optional)

    try:
        # Become a partner
        api_response = api_instance.partner_become_a_partner(become_partner_command=become_partner_command)
        print("The response of PartnersApi->partner_become_a_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnersApi->partner_become_a_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **become_partner_command** | [**BecomePartnerCommand**](BecomePartnerCommand.md)|  | [optional] 

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

# **partner_contact_us**
> object partner_contact_us(contact_us_command=contact_us_command)

Contact with us

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.contact_us_command import ContactUsCommand
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
    api_instance = taikunpycore.PartnersApi(api_client)
    contact_us_command = taikunpycore.ContactUsCommand() # ContactUsCommand |  (optional)

    try:
        # Contact with us
        api_response = api_instance.partner_contact_us(contact_us_command=contact_us_command)
        print("The response of PartnersApi->partner_contact_us:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnersApi->partner_contact_us: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_us_command** | [**ContactUsCommand**](ContactUsCommand.md)|  | [optional] 

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

# **partner_create**
> object partner_create(logo=logo, background_image=background_image, allow_registration=allow_registration, required_user_approval=required_user_approval, payment_enabled=payment_enabled, name=name, domain=domain, link=link, phone=phone, email=email, country=country, city=city, vat_number=vat_number, address=address, bg=bg, bg_collapsed_sub_item=bg_collapsed_sub_item, item_text=item_text, item_bg=item_bg, item_bg_hover=item_bg_hover, item_text_active=item_text_active, item_bg_active=item_bg_active, item_bg_active_hover=item_bg_active_hover, expanded=expanded, collapsed=collapsed)

Add a partner

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
    api_instance = taikunpycore.PartnersApi(api_client)
    logo = None # bytearray |  (optional)
    background_image = None # bytearray |  (optional)
    allow_registration = True # bool |  (optional)
    required_user_approval = True # bool |  (optional)
    payment_enabled = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    domain = 'domain_example' # str |  (optional)
    link = 'link_example' # str |  (optional)
    phone = 'phone_example' # str |  (optional)
    email = 'email_example' # str |  (optional)
    country = 'country_example' # str |  (optional)
    city = 'city_example' # str |  (optional)
    vat_number = 'vat_number_example' # str |  (optional)
    address = 'address_example' # str |  (optional)
    bg = 'bg_example' # str |  (optional)
    bg_collapsed_sub_item = 'bg_collapsed_sub_item_example' # str |  (optional)
    item_text = 'item_text_example' # str |  (optional)
    item_bg = 'item_bg_example' # str |  (optional)
    item_bg_hover = 'item_bg_hover_example' # str |  (optional)
    item_text_active = 'item_text_active_example' # str |  (optional)
    item_bg_active = 'item_bg_active_example' # str |  (optional)
    item_bg_active_hover = 'item_bg_active_hover_example' # str |  (optional)
    expanded = None # bytearray |  (optional)
    collapsed = None # bytearray |  (optional)

    try:
        # Add a partner
        api_response = api_instance.partner_create(logo=logo, background_image=background_image, allow_registration=allow_registration, required_user_approval=required_user_approval, payment_enabled=payment_enabled, name=name, domain=domain, link=link, phone=phone, email=email, country=country, city=city, vat_number=vat_number, address=address, bg=bg, bg_collapsed_sub_item=bg_collapsed_sub_item, item_text=item_text, item_bg=item_bg, item_bg_hover=item_bg_hover, item_text_active=item_text_active, item_bg_active=item_bg_active, item_bg_active_hover=item_bg_active_hover, expanded=expanded, collapsed=collapsed)
        print("The response of PartnersApi->partner_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnersApi->partner_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logo** | **bytearray**|  | [optional] 
 **background_image** | **bytearray**|  | [optional] 
 **allow_registration** | **bool**|  | [optional] 
 **required_user_approval** | **bool**|  | [optional] 
 **payment_enabled** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **domain** | **str**|  | [optional] 
 **link** | **str**|  | [optional] 
 **phone** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 
 **country** | **str**|  | [optional] 
 **city** | **str**|  | [optional] 
 **vat_number** | **str**|  | [optional] 
 **address** | **str**|  | [optional] 
 **bg** | **str**|  | [optional] 
 **bg_collapsed_sub_item** | **str**|  | [optional] 
 **item_text** | **str**|  | [optional] 
 **item_bg** | **str**|  | [optional] 
 **item_bg_hover** | **str**|  | [optional] 
 **item_text_active** | **str**|  | [optional] 
 **item_bg_active** | **str**|  | [optional] 
 **item_bg_active_hover** | **str**|  | [optional] 
 **expanded** | **bytearray**|  | [optional] 
 **collapsed** | **bytearray**|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **partner_delete_organizations**
> object partner_delete_organizations(id, request_body=request_body)

Delete organizations from a partner

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
    api_instance = taikunpycore.PartnersApi(api_client)
    id = 56 # int | 
    request_body = [56] # List[int] |  (optional)

    try:
        # Delete organizations from a partner
        api_response = api_instance.partner_delete_organizations(id, request_body=request_body)
        print("The response of PartnersApi->partner_delete_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnersApi->partner_delete_organizations: %s\n" % e)
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

# **partner_delete_whitelist_domain**
> object partner_delete_whitelist_domain(white_list_domain_delete_command=white_list_domain_delete_command)

Delete white list domain

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.white_list_domain_delete_command import WhiteListDomainDeleteCommand
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
    api_instance = taikunpycore.PartnersApi(api_client)
    white_list_domain_delete_command = taikunpycore.WhiteListDomainDeleteCommand() # WhiteListDomainDeleteCommand |  (optional)

    try:
        # Delete white list domain
        api_response = api_instance.partner_delete_whitelist_domain(white_list_domain_delete_command=white_list_domain_delete_command)
        print("The response of PartnersApi->partner_delete_whitelist_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnersApi->partner_delete_whitelist_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **white_list_domain_delete_command** | [**WhiteListDomainDeleteCommand**](WhiteListDomainDeleteCommand.md)|  | [optional] 

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

# **partner_details**
> PartnerDetailsDto partner_details()

Details of partners

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.partner_details_dto import PartnerDetailsDto
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
    api_instance = taikunpycore.PartnersApi(api_client)

    try:
        # Details of partners
        api_response = api_instance.partner_details()
        print("The response of PartnersApi->partner_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnersApi->partner_details: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PartnerDetailsDto**](PartnerDetailsDto.md)

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

# **partner_dropdown**
> List[PartnerEntity] partner_dropdown(search=search)

Get partners dropdown

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.partner_entity import PartnerEntity
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
    api_instance = taikunpycore.PartnersApi(api_client)
    search = 'search_example' # str |  (optional)

    try:
        # Get partners dropdown
        api_response = api_instance.partner_dropdown(search=search)
        print("The response of PartnersApi->partner_dropdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnersApi->partner_dropdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 

### Return type

[**List[PartnerEntity]**](PartnerEntity.md)

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

# **partner_info**
> PartnerRecordDto partner_info(domain=domain)

Get partner's registration info

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.partner_record_dto import PartnerRecordDto
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
    api_instance = taikunpycore.PartnersApi(api_client)
    domain = 'domain_example' # str |  (optional)

    try:
        # Get partner's registration info
        api_response = api_instance.partner_info(domain=domain)
        print("The response of PartnersApi->partner_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnersApi->partner_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | [optional] 

### Return type

[**PartnerRecordDto**](PartnerRecordDto.md)

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

# **partner_list**
> PartnersList partner_list(offset=offset, limit=limit, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id)

Get partners

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.partners_list import PartnersList
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
    api_instance = taikunpycore.PartnersApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)

    try:
        # Get partners
        api_response = api_instance.partner_list(offset=offset, limit=limit, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id)
        print("The response of PartnersApi->partner_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnersApi->partner_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 

### Return type

[**PartnersList**](PartnersList.md)

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

# **partner_update**
> object partner_update(id=id, logo=logo, background_image=background_image, name=name, domain=domain, link=link, phone=phone, email=email, country=country, city=city, vat_number=vat_number, address=address, allow_registration=allow_registration, required_user_approval=required_user_approval, payment_enabled=payment_enabled, bg=bg, bg_collapsed_sub_item=bg_collapsed_sub_item, item_text=item_text, item_bg=item_bg, item_bg_hover=item_bg_hover, item_text_active=item_text_active, item_bg_active=item_bg_active, item_bg_active_hover=item_bg_active_hover, expanded=expanded, collapsed=collapsed)

Edit partner's data by Id

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
    api_instance = taikunpycore.PartnersApi(api_client)
    id = 56 # int |  (optional)
    logo = None # bytearray |  (optional)
    background_image = None # bytearray |  (optional)
    name = 'name_example' # str |  (optional)
    domain = 'domain_example' # str |  (optional)
    link = 'link_example' # str |  (optional)
    phone = 'phone_example' # str |  (optional)
    email = 'email_example' # str |  (optional)
    country = 'country_example' # str |  (optional)
    city = 'city_example' # str |  (optional)
    vat_number = 'vat_number_example' # str |  (optional)
    address = 'address_example' # str |  (optional)
    allow_registration = True # bool |  (optional)
    required_user_approval = True # bool |  (optional)
    payment_enabled = True # bool |  (optional)
    bg = 'bg_example' # str |  (optional)
    bg_collapsed_sub_item = 'bg_collapsed_sub_item_example' # str |  (optional)
    item_text = 'item_text_example' # str |  (optional)
    item_bg = 'item_bg_example' # str |  (optional)
    item_bg_hover = 'item_bg_hover_example' # str |  (optional)
    item_text_active = 'item_text_active_example' # str |  (optional)
    item_bg_active = 'item_bg_active_example' # str |  (optional)
    item_bg_active_hover = 'item_bg_active_hover_example' # str |  (optional)
    expanded = None # bytearray |  (optional)
    collapsed = None # bytearray |  (optional)

    try:
        # Edit partner's data by Id
        api_response = api_instance.partner_update(id=id, logo=logo, background_image=background_image, name=name, domain=domain, link=link, phone=phone, email=email, country=country, city=city, vat_number=vat_number, address=address, allow_registration=allow_registration, required_user_approval=required_user_approval, payment_enabled=payment_enabled, bg=bg, bg_collapsed_sub_item=bg_collapsed_sub_item, item_text=item_text, item_bg=item_bg, item_bg_hover=item_bg_hover, item_text_active=item_text_active, item_bg_active=item_bg_active, item_bg_active_hover=item_bg_active_hover, expanded=expanded, collapsed=collapsed)
        print("The response of PartnersApi->partner_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnersApi->partner_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 
 **logo** | **bytearray**|  | [optional] 
 **background_image** | **bytearray**|  | [optional] 
 **name** | **str**|  | [optional] 
 **domain** | **str**|  | [optional] 
 **link** | **str**|  | [optional] 
 **phone** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 
 **country** | **str**|  | [optional] 
 **city** | **str**|  | [optional] 
 **vat_number** | **str**|  | [optional] 
 **address** | **str**|  | [optional] 
 **allow_registration** | **bool**|  | [optional] 
 **required_user_approval** | **bool**|  | [optional] 
 **payment_enabled** | **bool**|  | [optional] 
 **bg** | **str**|  | [optional] 
 **bg_collapsed_sub_item** | **str**|  | [optional] 
 **item_text** | **str**|  | [optional] 
 **item_bg** | **str**|  | [optional] 
 **item_bg_hover** | **str**|  | [optional] 
 **item_text_active** | **str**|  | [optional] 
 **item_bg_active** | **str**|  | [optional] 
 **item_bg_active_hover** | **str**|  | [optional] 
 **expanded** | **bytearray**|  | [optional] 
 **collapsed** | **bytearray**|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

