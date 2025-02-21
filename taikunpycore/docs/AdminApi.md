# taikunpycore.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_add_balance**](AdminApi.md#admin_add_balance) | **POST** /api/v1/admin/organizations/add/balance | Add balance for organization
[**admin_billing_operations**](AdminApi.md#admin_billing_operations) | **POST** /api/v1/admin/cloudcredentials/billing | Billing operations: enable/disable billing 
[**admin_create_user**](AdminApi.md#admin_create_user) | **POST** /api/v1/admin/users/create | User creation for admin
[**admin_delete_org**](AdminApi.md#admin_delete_org) | **POST** /api/v1/admin/organizations/delete | Delete organization
[**admin_extend_trial_period**](AdminApi.md#admin_extend_trial_period) | **POST** /api/v1/admin/organizations/extend/trial | Extend trial period
[**admin_keycloak_list**](AdminApi.md#admin_keycloak_list) | **GET** /api/v1/admin/keycloak/list | Keycloak list for admin
[**admin_make_csm**](AdminApi.md#admin_make_csm) | **POST** /api/v1/admin/users/make/csm | User csm update for admin
[**admin_make_owner**](AdminApi.md#admin_make_owner) | **POST** /api/v1/admin/users/make/owner | Make owner
[**admin_organizations**](AdminApi.md#admin_organizations) | **GET** /api/v1/admin/organizations/list |  Organizations for admin
[**admin_project_list**](AdminApi.md#admin_project_list) | **GET** /api/v1/admin/projects/list | Projects for admin
[**admin_remove_owner**](AdminApi.md#admin_remove_owner) | **POST** /api/v1/admin/users/remove/owner | Remove owner
[**admin_update_project**](AdminApi.md#admin_update_project) | **POST** /api/v1/admin/projects/update/version | Projects update for admin
[**admin_update_project_kube**](AdminApi.md#admin_update_project_kube) | **POST** /api/v1/admin/projects/update/kubeconfig | Projects update kube for admin
[**admin_update_user**](AdminApi.md#admin_update_user) | **POST** /api/v1/admin/users/update/password | User password update for admin
[**admin_update_user_kube**](AdminApi.md#admin_update_user_kube) | **POST** /api/v1/admin/projects/update/userkube | Projects update kube for admin
[**admin_update_users**](AdminApi.md#admin_update_users) | **POST** /api/v1/admin/users/update/email | User email update for admin
[**admin_users_list**](AdminApi.md#admin_users_list) | **GET** /api/v1/admin/users/list | Users for admin


# **admin_add_balance**
> object admin_add_balance(admin_add_balance_command)

Add balance for organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.admin_add_balance_command import AdminAddBalanceCommand
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
    api_instance = taikunpycore.AdminApi(api_client)
    admin_add_balance_command = taikunpycore.AdminAddBalanceCommand() # AdminAddBalanceCommand | 

    try:
        # Add balance for organization
        api_response = api_instance.admin_add_balance(admin_add_balance_command)
        print("The response of AdminApi->admin_add_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_add_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_add_balance_command** | [**AdminAddBalanceCommand**](AdminAddBalanceCommand.md)|  | 

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

# **admin_billing_operations**
> object admin_billing_operations(admin_billing_operation_command)

Billing operations: enable/disable billing 

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.admin_billing_operation_command import AdminBillingOperationCommand
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
    api_instance = taikunpycore.AdminApi(api_client)
    admin_billing_operation_command = taikunpycore.AdminBillingOperationCommand() # AdminBillingOperationCommand | 

    try:
        # Billing operations: enable/disable billing 
        api_response = api_instance.admin_billing_operations(admin_billing_operation_command)
        print("The response of AdminApi->admin_billing_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_billing_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_billing_operation_command** | [**AdminBillingOperationCommand**](AdminBillingOperationCommand.md)|  | 

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

# **admin_create_user**
> object admin_create_user(admin_user_create_command=admin_user_create_command)

User creation for admin

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.admin_user_create_command import AdminUserCreateCommand
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
    api_instance = taikunpycore.AdminApi(api_client)
    admin_user_create_command = taikunpycore.AdminUserCreateCommand() # AdminUserCreateCommand |  (optional)

    try:
        # User creation for admin
        api_response = api_instance.admin_create_user(admin_user_create_command=admin_user_create_command)
        print("The response of AdminApi->admin_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_user_create_command** | [**AdminUserCreateCommand**](AdminUserCreateCommand.md)|  | [optional] 

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

# **admin_delete_org**
> object admin_delete_org(admin_organizations_delete_command)

Delete organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.admin_organizations_delete_command import AdminOrganizationsDeleteCommand
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
    api_instance = taikunpycore.AdminApi(api_client)
    admin_organizations_delete_command = taikunpycore.AdminOrganizationsDeleteCommand() # AdminOrganizationsDeleteCommand | 

    try:
        # Delete organization
        api_response = api_instance.admin_delete_org(admin_organizations_delete_command)
        print("The response of AdminApi->admin_delete_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_delete_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_organizations_delete_command** | [**AdminOrganizationsDeleteCommand**](AdminOrganizationsDeleteCommand.md)|  | 

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

# **admin_extend_trial_period**
> object admin_extend_trial_period(extend_trial_period_command)

Extend trial period

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.extend_trial_period_command import ExtendTrialPeriodCommand
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
    api_instance = taikunpycore.AdminApi(api_client)
    extend_trial_period_command = taikunpycore.ExtendTrialPeriodCommand() # ExtendTrialPeriodCommand | 

    try:
        # Extend trial period
        api_response = api_instance.admin_extend_trial_period(extend_trial_period_command)
        print("The response of AdminApi->admin_extend_trial_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_extend_trial_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extend_trial_period_command** | [**ExtendTrialPeriodCommand**](ExtendTrialPeriodCommand.md)|  | 

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

# **admin_keycloak_list**
> AdminProjectsList admin_keycloak_list(limit=limit, offset=offset)

Keycloak list for admin

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.admin_projects_list import AdminProjectsList
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
    api_instance = taikunpycore.AdminApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)

    try:
        # Keycloak list for admin
        api_response = api_instance.admin_keycloak_list(limit=limit, offset=offset)
        print("The response of AdminApi->admin_keycloak_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_keycloak_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**AdminProjectsList**](AdminProjectsList.md)

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

# **admin_make_csm**
> object admin_make_csm(make_csm_command)

User csm update for admin

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.make_csm_command import MakeCsmCommand
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
    api_instance = taikunpycore.AdminApi(api_client)
    make_csm_command = taikunpycore.MakeCsmCommand() # MakeCsmCommand | 

    try:
        # User csm update for admin
        api_response = api_instance.admin_make_csm(make_csm_command)
        print("The response of AdminApi->admin_make_csm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_make_csm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **make_csm_command** | [**MakeCsmCommand**](MakeCsmCommand.md)|  | 

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

# **admin_make_owner**
> object admin_make_owner(make_owner_command)

Make owner

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.make_owner_command import MakeOwnerCommand
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
    api_instance = taikunpycore.AdminApi(api_client)
    make_owner_command = taikunpycore.MakeOwnerCommand() # MakeOwnerCommand | 

    try:
        # Make owner
        api_response = api_instance.admin_make_owner(make_owner_command)
        print("The response of AdminApi->admin_make_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_make_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **make_owner_command** | [**MakeOwnerCommand**](MakeOwnerCommand.md)|  | 

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

# **admin_organizations**
> AdminOrganizationsList admin_organizations(limit=limit, offset=offset, partner_id=partner_id, search=search)

 Organizations for admin

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.admin_organizations_list import AdminOrganizationsList
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
    api_instance = taikunpycore.AdminApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    partner_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        #  Organizations for admin
        api_response = api_instance.admin_organizations(limit=limit, offset=offset, partner_id=partner_id, search=search)
        print("The response of AdminApi->admin_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **partner_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**AdminOrganizationsList**](AdminOrganizationsList.md)

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

# **admin_project_list**
> AdminProjectsList admin_project_list(limit=limit, offset=offset, organization_id=organization_id, search=search)

Projects for admin

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.admin_projects_list import AdminProjectsList
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
    api_instance = taikunpycore.AdminApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Projects for admin
        api_response = api_instance.admin_project_list(limit=limit, offset=offset, organization_id=organization_id, search=search)
        print("The response of AdminApi->admin_project_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_project_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**AdminProjectsList**](AdminProjectsList.md)

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

# **admin_remove_owner**
> object admin_remove_owner(remove_owner_command)

Remove owner

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.remove_owner_command import RemoveOwnerCommand
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
    api_instance = taikunpycore.AdminApi(api_client)
    remove_owner_command = taikunpycore.RemoveOwnerCommand() # RemoveOwnerCommand | 

    try:
        # Remove owner
        api_response = api_instance.admin_remove_owner(remove_owner_command)
        print("The response of AdminApi->admin_remove_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_remove_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_owner_command** | [**RemoveOwnerCommand**](RemoveOwnerCommand.md)|  | 

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

# **admin_update_project**
> object admin_update_project(admin_project_update_command)

Projects update for admin

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.admin_project_update_command import AdminProjectUpdateCommand
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
    api_instance = taikunpycore.AdminApi(api_client)
    admin_project_update_command = taikunpycore.AdminProjectUpdateCommand() # AdminProjectUpdateCommand | 

    try:
        # Projects update for admin
        api_response = api_instance.admin_update_project(admin_project_update_command)
        print("The response of AdminApi->admin_update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_project_update_command** | [**AdminProjectUpdateCommand**](AdminProjectUpdateCommand.md)|  | 

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

# **admin_update_project_kube**
> object admin_update_project_kube(admin_update_project_kube_config_command)

Projects update kube for admin

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.admin_update_project_kube_config_command import AdminUpdateProjectKubeConfigCommand
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
    api_instance = taikunpycore.AdminApi(api_client)
    admin_update_project_kube_config_command = taikunpycore.AdminUpdateProjectKubeConfigCommand() # AdminUpdateProjectKubeConfigCommand | 

    try:
        # Projects update kube for admin
        api_response = api_instance.admin_update_project_kube(admin_update_project_kube_config_command)
        print("The response of AdminApi->admin_update_project_kube:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_update_project_kube: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_update_project_kube_config_command** | [**AdminUpdateProjectKubeConfigCommand**](AdminUpdateProjectKubeConfigCommand.md)|  | 

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

# **admin_update_user**
> object admin_update_user(admin_users_update_password_command=admin_users_update_password_command)

User password update for admin

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.admin_users_update_password_command import AdminUsersUpdatePasswordCommand
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
    api_instance = taikunpycore.AdminApi(api_client)
    admin_users_update_password_command = taikunpycore.AdminUsersUpdatePasswordCommand() # AdminUsersUpdatePasswordCommand |  (optional)

    try:
        # User password update for admin
        api_response = api_instance.admin_update_user(admin_users_update_password_command=admin_users_update_password_command)
        print("The response of AdminApi->admin_update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_users_update_password_command** | [**AdminUsersUpdatePasswordCommand**](AdminUsersUpdatePasswordCommand.md)|  | [optional] 

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

# **admin_update_user_kube**
> object admin_update_user_kube(admin_update_user_kube_config_command)

Projects update kube for admin

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.admin_update_user_kube_config_command import AdminUpdateUserKubeConfigCommand
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
    api_instance = taikunpycore.AdminApi(api_client)
    admin_update_user_kube_config_command = taikunpycore.AdminUpdateUserKubeConfigCommand() # AdminUpdateUserKubeConfigCommand | 

    try:
        # Projects update kube for admin
        api_response = api_instance.admin_update_user_kube(admin_update_user_kube_config_command)
        print("The response of AdminApi->admin_update_user_kube:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_update_user_kube: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_update_user_kube_config_command** | [**AdminUpdateUserKubeConfigCommand**](AdminUpdateUserKubeConfigCommand.md)|  | 

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

# **admin_update_users**
> object admin_update_users(admin_users_update_email_command)

User email update for admin

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.admin_users_update_email_command import AdminUsersUpdateEmailCommand
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
    api_instance = taikunpycore.AdminApi(api_client)
    admin_users_update_email_command = taikunpycore.AdminUsersUpdateEmailCommand() # AdminUsersUpdateEmailCommand | 

    try:
        # User email update for admin
        api_response = api_instance.admin_update_users(admin_users_update_email_command)
        print("The response of AdminApi->admin_update_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_update_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_users_update_email_command** | [**AdminUsersUpdateEmailCommand**](AdminUsersUpdateEmailCommand.md)|  | 

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

# **admin_users_list**
> AdminUsersList admin_users_list(limit=limit, offset=offset, organization_id=organization_id, search=search)

Users for admin

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.admin_users_list import AdminUsersList
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
    api_instance = taikunpycore.AdminApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Users for admin
        api_response = api_instance.admin_users_list(limit=limit, offset=offset, organization_id=organization_id, search=search)
        print("The response of AdminApi->admin_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**AdminUsersList**](AdminUsersList.md)

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

