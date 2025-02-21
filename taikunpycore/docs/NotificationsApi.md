# taikunpycore.NotificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifications_create**](NotificationsApi.md#notifications_create) | **POST** /api/v1/notifications/add | Create notification
[**notifications_export_csv**](NotificationsApi.md#notifications_export_csv) | **GET** /api/v1/notifications/download | Export Csv
[**notifications_list**](NotificationsApi.md#notifications_list) | **GET** /api/v1/notifications/list | Retrieve all notifications
[**notifications_notify_owner**](NotificationsApi.md#notifications_notify_owner) | **POST** /api/v1/notifications/notifyowner | Notify owner
[**notifications_operation_messages**](NotificationsApi.md#notifications_operation_messages) | **POST** /api/v1/notifications/operations | Get project operations


# **notifications_create**
> object notifications_create(notification_send_command=notification_send_command)

Create notification

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.notification_send_command import NotificationSendCommand
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
    api_instance = taikunpycore.NotificationsApi(api_client)
    notification_send_command = taikunpycore.NotificationSendCommand() # NotificationSendCommand |  (optional)

    try:
        # Create notification
        api_response = api_instance.notifications_create(notification_send_command=notification_send_command)
        print("The response of NotificationsApi->notifications_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->notifications_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_send_command** | [**NotificationSendCommand**](NotificationSendCommand.md)|  | [optional] 

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

# **notifications_export_csv**
> CsvExporter notifications_export_csv(is_email_enabled, sort_by=sort_by, sort_direction=sort_direction, start_date=start_date, end_date=end_date, organization_id=organization_id, filter_by=filter_by, project_id=project_id, user_id=user_id, is_deleted=is_deleted)

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
    api_instance = taikunpycore.NotificationsApi(api_client)
    is_email_enabled = True # bool | 
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    organization_id = 56 # int |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    is_deleted = True # bool |  (optional)

    try:
        # Export Csv
        api_response = api_instance.notifications_export_csv(is_email_enabled, sort_by=sort_by, sort_direction=sort_direction, start_date=start_date, end_date=end_date, organization_id=organization_id, filter_by=filter_by, project_id=project_id, user_id=user_id, is_deleted=is_deleted)
        print("The response of NotificationsApi->notifications_export_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->notifications_export_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_email_enabled** | **bool**|  | 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **filter_by** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 
 **user_id** | **str**|  | [optional] 
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

# **notifications_list**
> NotificationHistory notifications_list(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, start_date=start_date, end_date=end_date, organization_id=organization_id, filter_by=filter_by, project_id=project_id, user_id=user_id, is_deleted=is_deleted, search=search)

Retrieve all notifications

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.notification_history import NotificationHistory
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
    api_instance = taikunpycore.NotificationsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    organization_id = 56 # int |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    is_deleted = True # bool |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Retrieve all notifications
        api_response = api_instance.notifications_list(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, start_date=start_date, end_date=end_date, organization_id=organization_id, filter_by=filter_by, project_id=project_id, user_id=user_id, is_deleted=is_deleted, search=search)
        print("The response of NotificationsApi->notifications_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->notifications_list: %s\n" % e)
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
 **filter_by** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **is_deleted** | **bool**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**NotificationHistory**](NotificationHistory.md)

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

# **notifications_notify_owner**
> object notifications_notify_owner(notify_owners_command)

Notify owner

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.notify_owners_command import NotifyOwnersCommand
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
    api_instance = taikunpycore.NotificationsApi(api_client)
    notify_owners_command = taikunpycore.NotifyOwnersCommand() # NotifyOwnersCommand | 

    try:
        # Notify owner
        api_response = api_instance.notifications_notify_owner(notify_owners_command)
        print("The response of NotificationsApi->notifications_notify_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->notifications_notify_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notify_owners_command** | [**NotifyOwnersCommand**](NotifyOwnersCommand.md)|  | 

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

# **notifications_operation_messages**
> OperationDto notifications_operation_messages(get_project_operation_command)

Get project operations

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.get_project_operation_command import GetProjectOperationCommand
from taikunpycore.models.operation_dto import OperationDto
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
    api_instance = taikunpycore.NotificationsApi(api_client)
    get_project_operation_command = taikunpycore.GetProjectOperationCommand() # GetProjectOperationCommand | 

    try:
        # Get project operations
        api_response = api_instance.notifications_operation_messages(get_project_operation_command)
        print("The response of NotificationsApi->notifications_operation_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->notifications_operation_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_project_operation_command** | [**GetProjectOperationCommand**](GetProjectOperationCommand.md)|  | 

### Return type

[**OperationDto**](OperationDto.md)

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

