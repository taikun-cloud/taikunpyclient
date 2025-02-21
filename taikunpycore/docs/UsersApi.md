# taikunpycore.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_add_user_projects**](UsersApi.md#users_add_user_projects) | **POST** /api/v1/users/{id}/projects | Add projects to user
[**users_change_password**](UsersApi.md#users_change_password) | **POST** /api/v1/users/changepassword | Change user password
[**users_confirm_email**](UsersApi.md#users_confirm_email) | **POST** /api/v1/users/confirmemail | Confirm user email
[**users_create**](UsersApi.md#users_create) | **POST** /api/v1/users/create | Create user
[**users_delete**](UsersApi.md#users_delete) | **DELETE** /api/v1/users/{id} | Delete user
[**users_delete_my_account**](UsersApi.md#users_delete_my_account) | **POST** /api/v1/users/delete | Delete my account
[**users_delete_user_projects**](UsersApi.md#users_delete_user_projects) | **PUT** /api/v1/users/{id}/projects | Delete projects from user
[**users_disable**](UsersApi.md#users_disable) | **POST** /api/v1/users/disable | Disable user
[**users_dropdown**](UsersApi.md#users_dropdown) | **GET** /api/v1/users/list | Retrieve users as dropdown
[**users_export_csv**](UsersApi.md#users_export_csv) | **GET** /api/v1/users/export | Export Csv
[**users_force_to_reset_password**](UsersApi.md#users_force_to_reset_password) | **POST** /api/v1/users/force-to-reset | Force to reset password
[**users_list**](UsersApi.md#users_list) | **GET** /api/v1/users | Retrieve all users
[**users_toggle2fa_mode**](UsersApi.md#users_toggle2fa_mode) | **POST** /api/v1/users/toggle-2fa | Toggle 2FA mode
[**users_toggle_maintenance_mode**](UsersApi.md#users_toggle_maintenance_mode) | **POST** /api/v1/users/togglemaintenancemode | Toggle maintenance mode
[**users_toggle_notification_mode**](UsersApi.md#users_toggle_notification_mode) | **POST** /api/v1/users/togglenotificationmode | Toggle notification mode
[**users_update_user**](UsersApi.md#users_update_user) | **POST** /api/v1/users/update | Update user
[**users_user_info**](UsersApi.md#users_user_info) | **GET** /api/v1/users/userinfo | Retrieve user info
[**users_verify_email**](UsersApi.md#users_verify_email) | **POST** /api/v1/users/verifyemail | Verify user email


# **users_add_user_projects**
> users_add_user_projects(id, request_body=request_body)

Add projects to user

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
    api_instance = taikunpycore.UsersApi(api_client)
    id = 'id_example' # str | 
    request_body = [56] # List[int] |  (optional)

    try:
        # Add projects to user
        api_instance.users_add_user_projects(id, request_body=request_body)
    except Exception as e:
        print("Exception when calling UsersApi->users_add_user_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**List[int]**](int.md)|  | [optional] 

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

# **users_change_password**
> object users_change_password(change_password_command=change_password_command)

Change user password

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.change_password_command import ChangePasswordCommand
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
    api_instance = taikunpycore.UsersApi(api_client)
    change_password_command = taikunpycore.ChangePasswordCommand() # ChangePasswordCommand |  (optional)

    try:
        # Change user password
        api_response = api_instance.users_change_password(change_password_command=change_password_command)
        print("The response of UsersApi->users_change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password_command** | [**ChangePasswordCommand**](ChangePasswordCommand.md)|  | [optional] 

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

# **users_confirm_email**
> object users_confirm_email(confirm_email_command=confirm_email_command)

Confirm user email

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.confirm_email_command import ConfirmEmailCommand
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
    api_instance = taikunpycore.UsersApi(api_client)
    confirm_email_command = taikunpycore.ConfirmEmailCommand() # ConfirmEmailCommand |  (optional)

    try:
        # Confirm user email
        api_response = api_instance.users_confirm_email(confirm_email_command=confirm_email_command)
        print("The response of UsersApi->users_confirm_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_confirm_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirm_email_command** | [**ConfirmEmailCommand**](ConfirmEmailCommand.md)|  | [optional] 

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

# **users_create**
> ApiResponse users_create(create_user_command=create_user_command)

Create user

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_user_command import CreateUserCommand
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
    api_instance = taikunpycore.UsersApi(api_client)
    create_user_command = taikunpycore.CreateUserCommand() # CreateUserCommand |  (optional)

    try:
        # Create user
        api_response = api_instance.users_create(create_user_command=create_user_command)
        print("The response of UsersApi->users_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_command** | [**CreateUserCommand**](CreateUserCommand.md)|  | [optional] 

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

# **users_delete**
> users_delete(id)

Delete user

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
    api_instance = taikunpycore.UsersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete user
        api_instance.users_delete(id)
    except Exception as e:
        print("Exception when calling UsersApi->users_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **users_delete_my_account**
> object users_delete_my_account(body)

Delete my account

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
    api_instance = taikunpycore.UsersApi(api_client)
    body = None # object | 

    try:
        # Delete my account
        api_response = api_instance.users_delete_my_account(body)
        print("The response of UsersApi->users_delete_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_delete_my_account: %s\n" % e)
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

# **users_delete_user_projects**
> users_delete_user_projects(id, request_body=request_body)

Delete projects from user

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
    api_instance = taikunpycore.UsersApi(api_client)
    id = 'id_example' # str | 
    request_body = [56] # List[int] |  (optional)

    try:
        # Delete projects from user
        api_instance.users_delete_user_projects(id, request_body=request_body)
    except Exception as e:
        print("Exception when calling UsersApi->users_delete_user_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**List[int]**](int.md)|  | [optional] 

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

# **users_disable**
> object users_disable(disable_user_command)

Disable user

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.disable_user_command import DisableUserCommand
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
    api_instance = taikunpycore.UsersApi(api_client)
    disable_user_command = taikunpycore.DisableUserCommand() # DisableUserCommand | 

    try:
        # Disable user
        api_response = api_instance.users_disable(disable_user_command)
        print("The response of UsersApi->users_disable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_disable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_user_command** | [**DisableUserCommand**](DisableUserCommand.md)|  | 

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

# **users_dropdown**
> List[CommonStringDropdownIsBoundDto] users_dropdown(organization_id=organization_id, search=search, project_id=project_id)

Retrieve users as dropdown

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_string_dropdown_is_bound_dto import CommonStringDropdownIsBoundDto
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
    api_instance = taikunpycore.UsersApi(api_client)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve users as dropdown
        api_response = api_instance.users_dropdown(organization_id=organization_id, search=search, project_id=project_id)
        print("The response of UsersApi->users_dropdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_dropdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**List[CommonStringDropdownIsBoundDto]**](CommonStringDropdownIsBoundDto.md)

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

# **users_export_csv**
> CsvExporter users_export_csv()

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
    api_instance = taikunpycore.UsersApi(api_client)

    try:
        # Export Csv
        api_response = api_instance.users_export_csv()
        print("The response of UsersApi->users_export_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_export_csv: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **users_force_to_reset_password**
> object users_force_to_reset_password(force_to_reset_password_command)

Force to reset password

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.force_to_reset_password_command import ForceToResetPasswordCommand
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
    api_instance = taikunpycore.UsersApi(api_client)
    force_to_reset_password_command = taikunpycore.ForceToResetPasswordCommand() # ForceToResetPasswordCommand | 

    try:
        # Force to reset password
        api_response = api_instance.users_force_to_reset_password(force_to_reset_password_command)
        print("The response of UsersApi->users_force_to_reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_force_to_reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force_to_reset_password_command** | [**ForceToResetPasswordCommand**](ForceToResetPasswordCommand.md)|  | 

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

# **users_list**
> UsersList users_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id, filter_by=filter_by)

Retrieve all users

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.users_list import UsersList
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
    api_instance = taikunpycore.UsersApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve all users
        api_response = api_instance.users_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id, filter_by=filter_by)
        print("The response of UsersApi->users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**UsersList**](UsersList.md)

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

# **users_toggle2fa_mode**
> object users_toggle2fa_mode(toggle_two_factor_authentication_command)

Toggle 2FA mode

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.toggle_two_factor_authentication_command import ToggleTwoFactorAuthenticationCommand
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
    api_instance = taikunpycore.UsersApi(api_client)
    toggle_two_factor_authentication_command = taikunpycore.ToggleTwoFactorAuthenticationCommand() # ToggleTwoFactorAuthenticationCommand | 

    try:
        # Toggle 2FA mode
        api_response = api_instance.users_toggle2fa_mode(toggle_two_factor_authentication_command)
        print("The response of UsersApi->users_toggle2fa_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_toggle2fa_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toggle_two_factor_authentication_command** | [**ToggleTwoFactorAuthenticationCommand**](ToggleTwoFactorAuthenticationCommand.md)|  | 

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

# **users_toggle_maintenance_mode**
> object users_toggle_maintenance_mode(toggle_maintenance_mode_command)

Toggle maintenance mode

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.toggle_maintenance_mode_command import ToggleMaintenanceModeCommand
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
    api_instance = taikunpycore.UsersApi(api_client)
    toggle_maintenance_mode_command = taikunpycore.ToggleMaintenanceModeCommand() # ToggleMaintenanceModeCommand | 

    try:
        # Toggle maintenance mode
        api_response = api_instance.users_toggle_maintenance_mode(toggle_maintenance_mode_command)
        print("The response of UsersApi->users_toggle_maintenance_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_toggle_maintenance_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toggle_maintenance_mode_command** | [**ToggleMaintenanceModeCommand**](ToggleMaintenanceModeCommand.md)|  | 

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

# **users_toggle_notification_mode**
> object users_toggle_notification_mode(toggle_notification_mode_command)

Toggle notification mode

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.toggle_notification_mode_command import ToggleNotificationModeCommand
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
    api_instance = taikunpycore.UsersApi(api_client)
    toggle_notification_mode_command = taikunpycore.ToggleNotificationModeCommand() # ToggleNotificationModeCommand | 

    try:
        # Toggle notification mode
        api_response = api_instance.users_toggle_notification_mode(toggle_notification_mode_command)
        print("The response of UsersApi->users_toggle_notification_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_toggle_notification_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toggle_notification_mode_command** | [**ToggleNotificationModeCommand**](ToggleNotificationModeCommand.md)|  | 

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

# **users_update_user**
> object users_update_user(update_user_command=update_user_command)

Update user

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_user_command import UpdateUserCommand
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
    api_instance = taikunpycore.UsersApi(api_client)
    update_user_command = taikunpycore.UpdateUserCommand() # UpdateUserCommand |  (optional)

    try:
        # Update user
        api_response = api_instance.users_update_user(update_user_command=update_user_command)
        print("The response of UsersApi->users_update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_command** | [**UpdateUserCommand**](UpdateUserCommand.md)|  | [optional] 

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

# **users_user_info**
> UserDetails users_user_info()

Retrieve user info

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.user_details import UserDetails
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
    api_instance = taikunpycore.UsersApi(api_client)

    try:
        # Retrieve user info
        api_response = api_instance.users_user_info()
        print("The response of UsersApi->users_user_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_user_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserDetails**](UserDetails.md)

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

# **users_verify_email**
> object users_verify_email(verify_email_command)

Verify user email

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.verify_email_command import VerifyEmailCommand
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
    api_instance = taikunpycore.UsersApi(api_client)
    verify_email_command = taikunpycore.VerifyEmailCommand() # VerifyEmailCommand | 

    try:
        # Verify user email
        api_response = api_instance.users_verify_email(verify_email_command)
        print("The response of UsersApi->users_verify_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_verify_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_email_command** | [**VerifyEmailCommand**](VerifyEmailCommand.md)|  | 

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

