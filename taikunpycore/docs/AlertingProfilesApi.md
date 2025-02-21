# taikunpycore.AlertingProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertingprofiles_assign_email**](AlertingProfilesApi.md#alertingprofiles_assign_email) | **PUT** /api/v1/alertingprofiles/assignemails/{id} | Assign Alerting emails
[**alertingprofiles_assign_webhooks**](AlertingProfilesApi.md#alertingprofiles_assign_webhooks) | **PUT** /api/v1/alertingprofiles/assignwebhooks/{id} | Assign Alerting webhooks
[**alertingprofiles_attach**](AlertingProfilesApi.md#alertingprofiles_attach) | **POST** /api/v1/alertingprofiles/attach | Attach alerting profile to project
[**alertingprofiles_create**](AlertingProfilesApi.md#alertingprofiles_create) | **POST** /api/v1/alertingprofiles/create | Add Alerting profile
[**alertingprofiles_delete**](AlertingProfilesApi.md#alertingprofiles_delete) | **DELETE** /api/v1/alertingprofiles/{id} | Remove Alerting profiles by Id
[**alertingprofiles_detach**](AlertingProfilesApi.md#alertingprofiles_detach) | **POST** /api/v1/alertingprofiles/detach | Detach alerting profile from project
[**alertingprofiles_dropdown**](AlertingProfilesApi.md#alertingprofiles_dropdown) | **GET** /api/v1/alertingprofiles/list | Retrieve all Alerting profiles for organization
[**alertingprofiles_edit**](AlertingProfilesApi.md#alertingprofiles_edit) | **POST** /api/v1/alertingprofiles/edit | Update Alerting profile
[**alertingprofiles_list**](AlertingProfilesApi.md#alertingprofiles_list) | **GET** /api/v1/alertingprofiles | Retrieve all Alerting profiles
[**alertingprofiles_lock_manager**](AlertingProfilesApi.md#alertingprofiles_lock_manager) | **POST** /api/v1/alertingprofiles/lockmanager | Lock/Unlock Alerting profiles
[**alertingprofiles_verify**](AlertingProfilesApi.md#alertingprofiles_verify) | **POST** /api/v1/alertingprofiles/verifywebhook | Verify webhook endpoint


# **alertingprofiles_assign_email**
> object alertingprofiles_assign_email(id, alerting_email_dto=alerting_email_dto)

Assign Alerting emails

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.alerting_email_dto import AlertingEmailDto
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
    api_instance = taikunpycore.AlertingProfilesApi(api_client)
    id = 56 # int | 
    alerting_email_dto = [{"email":"taikun@taikun.cloud"}] # List[AlertingEmailDto] |  (optional)

    try:
        # Assign Alerting emails
        api_response = api_instance.alertingprofiles_assign_email(id, alerting_email_dto=alerting_email_dto)
        print("The response of AlertingProfilesApi->alertingprofiles_assign_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingProfilesApi->alertingprofiles_assign_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **alerting_email_dto** | [**List[AlertingEmailDto]**](AlertingEmailDto.md)|  | [optional] 

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

# **alertingprofiles_assign_webhooks**
> object alertingprofiles_assign_webhooks(id, alerting_webhook_dto=alerting_webhook_dto)

Assign Alerting webhooks

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.alerting_webhook_dto import AlertingWebhookDto
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
    api_instance = taikunpycore.AlertingProfilesApi(api_client)
    id = 56 # int | 
    alerting_webhook_dto = [{"id":1,"url":"https://www.google.com","headers":[{"id":1,"key":"taikun","value":"taikun"}]}] # List[AlertingWebhookDto] |  (optional)

    try:
        # Assign Alerting webhooks
        api_response = api_instance.alertingprofiles_assign_webhooks(id, alerting_webhook_dto=alerting_webhook_dto)
        print("The response of AlertingProfilesApi->alertingprofiles_assign_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingProfilesApi->alertingprofiles_assign_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **alerting_webhook_dto** | [**List[AlertingWebhookDto]**](AlertingWebhookDto.md)|  | [optional] 

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

# **alertingprofiles_attach**
> object alertingprofiles_attach(attach_detach_alerting_profile_command)

Attach alerting profile to project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.attach_detach_alerting_profile_command import AttachDetachAlertingProfileCommand
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
    api_instance = taikunpycore.AlertingProfilesApi(api_client)
    attach_detach_alerting_profile_command = taikunpycore.AttachDetachAlertingProfileCommand() # AttachDetachAlertingProfileCommand | 

    try:
        # Attach alerting profile to project
        api_response = api_instance.alertingprofiles_attach(attach_detach_alerting_profile_command)
        print("The response of AlertingProfilesApi->alertingprofiles_attach:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingProfilesApi->alertingprofiles_attach: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attach_detach_alerting_profile_command** | [**AttachDetachAlertingProfileCommand**](AttachDetachAlertingProfileCommand.md)|  | 

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

# **alertingprofiles_create**
> ApiResponse alertingprofiles_create(create_alerting_profile_command=create_alerting_profile_command)

Add Alerting profile

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_alerting_profile_command import CreateAlertingProfileCommand
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
    api_instance = taikunpycore.AlertingProfilesApi(api_client)
    create_alerting_profile_command = {"name":"taikun","slackConfigurationId":null,"organizationId":null,"emails":[{"email":"taikun@taikun.cloud"}],"webhooks":[{"id":1,"url":"https://www.google.com","headers":[{"id":1,"key":"taikun","value":"taikun"}]}],"alertingIntegrations":[{"url":"https://www.google.com","token":"Only if no microsoft teams type","alertingIntegrationType":"Opsgenie"}],"reminder":"Daily"} # CreateAlertingProfileCommand |  (optional)

    try:
        # Add Alerting profile
        api_response = api_instance.alertingprofiles_create(create_alerting_profile_command=create_alerting_profile_command)
        print("The response of AlertingProfilesApi->alertingprofiles_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingProfilesApi->alertingprofiles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_alerting_profile_command** | [**CreateAlertingProfileCommand**](CreateAlertingProfileCommand.md)|  | [optional] 

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

# **alertingprofiles_delete**
> alertingprofiles_delete(id)

Remove Alerting profiles by Id

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
    api_instance = taikunpycore.AlertingProfilesApi(api_client)
    id = 56 # int | 

    try:
        # Remove Alerting profiles by Id
        api_instance.alertingprofiles_delete(id)
    except Exception as e:
        print("Exception when calling AlertingProfilesApi->alertingprofiles_delete: %s\n" % e)
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

# **alertingprofiles_detach**
> object alertingprofiles_detach(attach_detach_alerting_profile_command)

Detach alerting profile from project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.attach_detach_alerting_profile_command import AttachDetachAlertingProfileCommand
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
    api_instance = taikunpycore.AlertingProfilesApi(api_client)
    attach_detach_alerting_profile_command = taikunpycore.AttachDetachAlertingProfileCommand() # AttachDetachAlertingProfileCommand | 

    try:
        # Detach alerting profile from project
        api_response = api_instance.alertingprofiles_detach(attach_detach_alerting_profile_command)
        print("The response of AlertingProfilesApi->alertingprofiles_detach:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingProfilesApi->alertingprofiles_detach: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attach_detach_alerting_profile_command** | [**AttachDetachAlertingProfileCommand**](AttachDetachAlertingProfileCommand.md)|  | 

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

# **alertingprofiles_dropdown**
> List[CommonDropdownDto] alertingprofiles_dropdown(organization_id=organization_id, search=search)

Retrieve all Alerting profiles for organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_dropdown_dto import CommonDropdownDto
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
    api_instance = taikunpycore.AlertingProfilesApi(api_client)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Retrieve all Alerting profiles for organization
        api_response = api_instance.alertingprofiles_dropdown(organization_id=organization_id, search=search)
        print("The response of AlertingProfilesApi->alertingprofiles_dropdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingProfilesApi->alertingprofiles_dropdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**List[CommonDropdownDto]**](CommonDropdownDto.md)

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

# **alertingprofiles_edit**
> ApiResponse alertingprofiles_edit(update_alerting_profile_command=update_alerting_profile_command)

Update Alerting profile

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.update_alerting_profile_command import UpdateAlertingProfileCommand
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
    api_instance = taikunpycore.AlertingProfilesApi(api_client)
    update_alerting_profile_command = {"id":1,"name":"taikun","slackConfigurationId":null,"organizationId":null,"reminder":"Daily"} # UpdateAlertingProfileCommand |  (optional)

    try:
        # Update Alerting profile
        api_response = api_instance.alertingprofiles_edit(update_alerting_profile_command=update_alerting_profile_command)
        print("The response of AlertingProfilesApi->alertingprofiles_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingProfilesApi->alertingprofiles_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_alerting_profile_command** | [**UpdateAlertingProfileCommand**](UpdateAlertingProfileCommand.md)|  | [optional] 

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

# **alertingprofiles_list**
> AlertingProfilesList alertingprofiles_list(organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id, search_id=search_id, limit=limit, offset=offset)

Retrieve all Alerting profiles

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>SortBy</b> - Options: <i>createdAt</i>, <i>name</i>, <i>organizationName</i></li><li><b>SortDirection</b> - Options: <i>asc</i>, <i>desc</i></li><li><b>Search</b> - Options: <i>name</i>, <i>organizationName</i></li></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.alerting_profiles_list import AlertingProfilesList
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
    api_instance = taikunpycore.AlertingProfilesApi(api_client)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    id = 56 # int |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Retrieve all Alerting profiles
        api_response = api_instance.alertingprofiles_list(organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id, search_id=search_id, limit=limit, offset=offset)
        print("The response of AlertingProfilesApi->alertingprofiles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingProfilesApi->alertingprofiles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**AlertingProfilesList**](AlertingProfilesList.md)

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

# **alertingprofiles_lock_manager**
> object alertingprofiles_lock_manager(alerting_profiles_lock_manager_command=alerting_profiles_lock_manager_command)

Lock/Unlock Alerting profiles

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.alerting_profiles_lock_manager_command import AlertingProfilesLockManagerCommand
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
    api_instance = taikunpycore.AlertingProfilesApi(api_client)
    alerting_profiles_lock_manager_command = {"id":1,"mode":"lock|unlock"} # AlertingProfilesLockManagerCommand |  (optional)

    try:
        # Lock/Unlock Alerting profiles
        api_response = api_instance.alertingprofiles_lock_manager(alerting_profiles_lock_manager_command=alerting_profiles_lock_manager_command)
        print("The response of AlertingProfilesApi->alertingprofiles_lock_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingProfilesApi->alertingprofiles_lock_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alerting_profiles_lock_manager_command** | [**AlertingProfilesLockManagerCommand**](AlertingProfilesLockManagerCommand.md)|  | [optional] 

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

# **alertingprofiles_verify**
> object alertingprofiles_verify(verify_webhook_command=verify_webhook_command)

Verify webhook endpoint

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.verify_webhook_command import VerifyWebhookCommand
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
    api_instance = taikunpycore.AlertingProfilesApi(api_client)
    verify_webhook_command = {"url":"https://www.google.com"} # VerifyWebhookCommand |  (optional)

    try:
        # Verify webhook endpoint
        api_response = api_instance.alertingprofiles_verify(verify_webhook_command=verify_webhook_command)
        print("The response of AlertingProfilesApi->alertingprofiles_verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertingProfilesApi->alertingprofiles_verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_webhook_command** | [**VerifyWebhookCommand**](VerifyWebhookCommand.md)|  | [optional] 

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

