# taikunpycore.TicketApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ticket_archive**](TicketApi.md#ticket_archive) | **POST** /api/v1/ticket/archive | Archive ticket
[**ticket_close**](TicketApi.md#ticket_close) | **POST** /api/v1/ticket/close | Close ticket
[**ticket_create**](TicketApi.md#ticket_create) | **POST** /api/v1/ticket/create | Create ticket
[**ticket_delete**](TicketApi.md#ticket_delete) | **DELETE** /api/v1/ticket/delete/{ticketId} | Delete ticket
[**ticket_delete_message**](TicketApi.md#ticket_delete_message) | **DELETE** /api/v1/ticket/delete/message/{messageId} | Delete ticket message
[**ticket_edit**](TicketApi.md#ticket_edit) | **POST** /api/v1/ticket/edit | Edit ticket
[**ticket_edit_message**](TicketApi.md#ticket_edit_message) | **POST** /api/v1/ticket/edit/message | Edit ticket message
[**ticket_list**](TicketApi.md#ticket_list) | **GET** /api/v1/ticket/list | Retrieve list of tickets
[**ticket_messages**](TicketApi.md#ticket_messages) | **GET** /api/v1/ticket/{ticketId}/messages | Retrieve articles of ticket
[**ticket_open**](TicketApi.md#ticket_open) | **POST** /api/v1/ticket/open | Open ticket
[**ticket_reply**](TicketApi.md#ticket_reply) | **POST** /api/v1/ticket/reply | Reply message
[**ticket_set_priority**](TicketApi.md#ticket_set_priority) | **POST** /api/v1/ticket/set-priority | Set priority
[**ticket_transfer**](TicketApi.md#ticket_transfer) | **POST** /api/v1/ticket/transfer | Transfer ticket
[**ticket_transfer_list**](TicketApi.md#ticket_transfer_list) | **GET** /api/v1/ticket/transfer/list | Retrieve organization managers


# **ticket_archive**
> object ticket_archive(archive_ticket_command)

Archive ticket

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.archive_ticket_command import ArchiveTicketCommand
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
    api_instance = taikunpycore.TicketApi(api_client)
    archive_ticket_command = taikunpycore.ArchiveTicketCommand() # ArchiveTicketCommand | 

    try:
        # Archive ticket
        api_response = api_instance.ticket_archive(archive_ticket_command)
        print("The response of TicketApi->ticket_archive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_archive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_ticket_command** | [**ArchiveTicketCommand**](ArchiveTicketCommand.md)|  | 

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

# **ticket_close**
> object ticket_close(close_ticket_command)

Close ticket

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.close_ticket_command import CloseTicketCommand
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
    api_instance = taikunpycore.TicketApi(api_client)
    close_ticket_command = taikunpycore.CloseTicketCommand() # CloseTicketCommand | 

    try:
        # Close ticket
        api_response = api_instance.ticket_close(close_ticket_command)
        print("The response of TicketApi->ticket_close:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_close: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **close_ticket_command** | [**CloseTicketCommand**](CloseTicketCommand.md)|  | 

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

# **ticket_create**
> object ticket_create(create_ticket_command)

Create ticket

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.create_ticket_command import CreateTicketCommand
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
    api_instance = taikunpycore.TicketApi(api_client)
    create_ticket_command = taikunpycore.CreateTicketCommand() # CreateTicketCommand | 

    try:
        # Create ticket
        api_response = api_instance.ticket_create(create_ticket_command)
        print("The response of TicketApi->ticket_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ticket_command** | [**CreateTicketCommand**](CreateTicketCommand.md)|  | 

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

# **ticket_delete**
> ticket_delete(ticket_id)

Delete ticket

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
    api_instance = taikunpycore.TicketApi(api_client)
    ticket_id = 'ticket_id_example' # str | 

    try:
        # Delete ticket
        api_instance.ticket_delete(ticket_id)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_delete_message**
> ticket_delete_message(message_id)

Delete ticket message

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
    api_instance = taikunpycore.TicketApi(api_client)
    message_id = 'message_id_example' # str | 

    try:
        # Delete ticket message
        api_instance.ticket_delete_message(message_id)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_delete_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**|  | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_edit**
> object ticket_edit(edit_ticket_command)

Edit ticket

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.edit_ticket_command import EditTicketCommand
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
    api_instance = taikunpycore.TicketApi(api_client)
    edit_ticket_command = taikunpycore.EditTicketCommand() # EditTicketCommand | 

    try:
        # Edit ticket
        api_response = api_instance.ticket_edit(edit_ticket_command)
        print("The response of TicketApi->ticket_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_ticket_command** | [**EditTicketCommand**](EditTicketCommand.md)|  | 

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

# **ticket_edit_message**
> object ticket_edit_message(edit_article_command)

Edit ticket message

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.edit_article_command import EditArticleCommand
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
    api_instance = taikunpycore.TicketApi(api_client)
    edit_article_command = taikunpycore.EditArticleCommand() # EditArticleCommand | 

    try:
        # Edit ticket message
        api_response = api_instance.ticket_edit_message(edit_article_command)
        print("The response of TicketApi->ticket_edit_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_edit_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_article_command** | [**EditArticleCommand**](EditArticleCommand.md)|  | 

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

# **ticket_list**
> AllTicketsList ticket_list(limit=limit, offset=offset, organization_id=organization_id, search=search, start_date=start_date, end_date=end_date, ticket_id=ticket_id)

Retrieve list of tickets

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.all_tickets_list import AllTicketsList
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
    api_instance = taikunpycore.TicketApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    ticket_id = 'ticket_id_example' # str |  (optional)

    try:
        # Retrieve list of tickets
        api_response = api_instance.ticket_list(limit=limit, offset=offset, organization_id=organization_id, search=search, start_date=start_date, end_date=end_date, ticket_id=ticket_id)
        print("The response of TicketApi->ticket_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **ticket_id** | **str**|  | [optional] 

### Return type

[**AllTicketsList**](AllTicketsList.md)

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

# **ticket_messages**
> ArticleList ticket_messages(ticket_id, limit=limit, offset=offset)

Retrieve articles of ticket

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.article_list import ArticleList
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
    api_instance = taikunpycore.TicketApi(api_client)
    ticket_id = 'ticket_id_example' # str | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)

    try:
        # Retrieve articles of ticket
        api_response = api_instance.ticket_messages(ticket_id, limit=limit, offset=offset)
        print("The response of TicketApi->ticket_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**ArticleList**](ArticleList.md)

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

# **ticket_open**
> object ticket_open(open_ticket_command)

Open ticket

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.open_ticket_command import OpenTicketCommand
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
    api_instance = taikunpycore.TicketApi(api_client)
    open_ticket_command = taikunpycore.OpenTicketCommand() # OpenTicketCommand | 

    try:
        # Open ticket
        api_response = api_instance.ticket_open(open_ticket_command)
        print("The response of TicketApi->ticket_open:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_open: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_ticket_command** | [**OpenTicketCommand**](OpenTicketCommand.md)|  | 

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

# **ticket_reply**
> object ticket_reply(reply_ticket_command)

Reply message

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.reply_ticket_command import ReplyTicketCommand
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
    api_instance = taikunpycore.TicketApi(api_client)
    reply_ticket_command = taikunpycore.ReplyTicketCommand() # ReplyTicketCommand | 

    try:
        # Reply message
        api_response = api_instance.ticket_reply(reply_ticket_command)
        print("The response of TicketApi->ticket_reply:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_reply: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reply_ticket_command** | [**ReplyTicketCommand**](ReplyTicketCommand.md)|  | 

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

# **ticket_set_priority**
> object ticket_set_priority(set_ticket_priority_command)

Set priority

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.set_ticket_priority_command import SetTicketPriorityCommand
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
    api_instance = taikunpycore.TicketApi(api_client)
    set_ticket_priority_command = taikunpycore.SetTicketPriorityCommand() # SetTicketPriorityCommand | 

    try:
        # Set priority
        api_response = api_instance.ticket_set_priority(set_ticket_priority_command)
        print("The response of TicketApi->ticket_set_priority:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_set_priority: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_ticket_priority_command** | [**SetTicketPriorityCommand**](SetTicketPriorityCommand.md)|  | 

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

# **ticket_transfer**
> object ticket_transfer(transfer_ticket_command)

Transfer ticket

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.transfer_ticket_command import TransferTicketCommand
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
    api_instance = taikunpycore.TicketApi(api_client)
    transfer_ticket_command = taikunpycore.TransferTicketCommand() # TransferTicketCommand | 

    try:
        # Transfer ticket
        api_response = api_instance.ticket_transfer(transfer_ticket_command)
        print("The response of TicketApi->ticket_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_ticket_command** | [**TransferTicketCommand**](TransferTicketCommand.md)|  | 

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

# **ticket_transfer_list**
> List[TransferList] ticket_transfer_list(organization_id=organization_id)

Retrieve organization managers

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.transfer_list import TransferList
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
    api_instance = taikunpycore.TicketApi(api_client)
    organization_id = 56 # int |  (optional)

    try:
        # Retrieve organization managers
        api_response = api_instance.ticket_transfer_list(organization_id=organization_id)
        print("The response of TicketApi->ticket_transfer_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_transfer_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 

### Return type

[**List[TransferList]**](TransferList.md)

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

