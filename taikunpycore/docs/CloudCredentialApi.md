# taikunpycore.CloudCredentialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudcredentials_all_flavors**](CloudCredentialApi.md#cloudcredentials_all_flavors) | **GET** /api/v1/cloudcredentials/flavors/{cloudId} | Retrieve all flavors
[**cloudcredentials_delete**](CloudCredentialApi.md#cloudcredentials_delete) | **DELETE** /api/v1/cloudcredentials/{cloudId} | Remove cloud credential by cloud Id
[**cloudcredentials_exceeded**](CloudCredentialApi.md#cloudcredentials_exceeded) | **GET** /api/v1/cloudcredentials/exceeded-quotas | Retrieve cloud credentials exceeded quotas
[**cloudcredentials_lock_manager**](CloudCredentialApi.md#cloudcredentials_lock_manager) | **POST** /api/v1/cloudcredentials/lockmanager | Lock/Unlock cloud credential
[**cloudcredentials_make_default**](CloudCredentialApi.md#cloudcredentials_make_default) | **POST** /api/v1/cloudcredentials/makedefault | Make cloud credentials default
[**cloudcredentials_org_list**](CloudCredentialApi.md#cloudcredentials_org_list) | **GET** /api/v1/cloudcredentials | Retrieve a list of cloud credentials by organization Id
[**cloudcredentials_update_ip_addresses**](CloudCredentialApi.md#cloudcredentials_update_ip_addresses) | **POST** /api/v1/cloudcredentials/network/ip-addresses | Update cloud credential&#39;s allocated ip addresses


# **cloudcredentials_all_flavors**
> AllFlavorsList cloudcredentials_all_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction)

Retrieve all flavors

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.all_flavors_list import AllFlavorsList
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
    api_instance = taikunpycore.CloudCredentialApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)

    try:
        # Retrieve all flavors
        api_response = api_instance.cloudcredentials_all_flavors(cloud_id, limit=limit, offset=offset, start_ram=start_ram, end_ram=end_ram, start_cpu=start_cpu, end_cpu=end_cpu, search=search, sort_by=sort_by, sort_direction=sort_direction)
        print("The response of CloudCredentialApi->cloudcredentials_all_flavors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCredentialApi->cloudcredentials_all_flavors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **start_ram** | **float**|  | [optional] 
 **end_ram** | **float**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 

### Return type

[**AllFlavorsList**](AllFlavorsList.md)

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

# **cloudcredentials_delete**
> cloudcredentials_delete(cloud_id)

Remove cloud credential by cloud Id

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
    api_instance = taikunpycore.CloudCredentialApi(api_client)
    cloud_id = 56 # int | 

    try:
        # Remove cloud credential by cloud Id
        api_instance.cloudcredentials_delete(cloud_id)
    except Exception as e:
        print("Exception when calling CloudCredentialApi->cloudcredentials_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 

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

# **cloudcredentials_exceeded**
> ExceededQuotaList cloudcredentials_exceeded(organization_id=organization_id)

Retrieve cloud credentials exceeded quotas

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.exceeded_quota_list import ExceededQuotaList
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
    api_instance = taikunpycore.CloudCredentialApi(api_client)
    organization_id = 56 # int |  (optional)

    try:
        # Retrieve cloud credentials exceeded quotas
        api_response = api_instance.cloudcredentials_exceeded(organization_id=organization_id)
        print("The response of CloudCredentialApi->cloudcredentials_exceeded:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCredentialApi->cloudcredentials_exceeded: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 

### Return type

[**ExceededQuotaList**](ExceededQuotaList.md)

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

# **cloudcredentials_lock_manager**
> object cloudcredentials_lock_manager(cloud_lock_manager_command)

Lock/Unlock cloud credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.cloud_lock_manager_command import CloudLockManagerCommand
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
    api_instance = taikunpycore.CloudCredentialApi(api_client)
    cloud_lock_manager_command = taikunpycore.CloudLockManagerCommand() # CloudLockManagerCommand | 

    try:
        # Lock/Unlock cloud credential
        api_response = api_instance.cloudcredentials_lock_manager(cloud_lock_manager_command)
        print("The response of CloudCredentialApi->cloudcredentials_lock_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCredentialApi->cloudcredentials_lock_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_lock_manager_command** | [**CloudLockManagerCommand**](CloudLockManagerCommand.md)|  | 

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

# **cloudcredentials_make_default**
> object cloudcredentials_make_default(credential_make_default_command)

Make cloud credentials default

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.credential_make_default_command import CredentialMakeDefaultCommand
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
    api_instance = taikunpycore.CloudCredentialApi(api_client)
    credential_make_default_command = taikunpycore.CredentialMakeDefaultCommand() # CredentialMakeDefaultCommand | 

    try:
        # Make cloud credentials default
        api_response = api_instance.cloudcredentials_make_default(credential_make_default_command)
        print("The response of CloudCredentialApi->cloudcredentials_make_default:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCredentialApi->cloudcredentials_make_default: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_make_default_command** | [**CredentialMakeDefaultCommand**](CredentialMakeDefaultCommand.md)|  | 

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

# **cloudcredentials_org_list**
> List[CloudCredentialsForOrganizationEntity] cloudcredentials_org_list(is_admin, organization_id=organization_id, search=search, is_infra=is_infra, id=id, cloud_type=cloud_type)

Retrieve a list of cloud credentials by organization Id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.cloud_credentials_for_organization_entity import CloudCredentialsForOrganizationEntity
from taikunpycore.models.cloud_type import CloudType
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
    api_instance = taikunpycore.CloudCredentialApi(api_client)
    is_admin = True # bool | 
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    is_infra = True # bool |  (optional)
    id = 56 # int |  (optional)
    cloud_type = taikunpycore.CloudType() # CloudType |  (optional)

    try:
        # Retrieve a list of cloud credentials by organization Id
        api_response = api_instance.cloudcredentials_org_list(is_admin, organization_id=organization_id, search=search, is_infra=is_infra, id=id, cloud_type=cloud_type)
        print("The response of CloudCredentialApi->cloudcredentials_org_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCredentialApi->cloudcredentials_org_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_admin** | **bool**|  | 
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **is_infra** | **bool**|  | [optional] 
 **id** | **int**|  | [optional] 
 **cloud_type** | [**CloudType**](.md)|  | [optional] 

### Return type

[**List[CloudCredentialsForOrganizationEntity]**](CloudCredentialsForOrganizationEntity.md)

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

# **cloudcredentials_update_ip_addresses**
> object cloudcredentials_update_ip_addresses(update_used_ip_addresses_command)

Update cloud credential's allocated ip addresses

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_used_ip_addresses_command import UpdateUsedIpAddressesCommand
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
    api_instance = taikunpycore.CloudCredentialApi(api_client)
    update_used_ip_addresses_command = taikunpycore.UpdateUsedIpAddressesCommand() # UpdateUsedIpAddressesCommand | 

    try:
        # Update cloud credential's allocated ip addresses
        api_response = api_instance.cloudcredentials_update_ip_addresses(update_used_ip_addresses_command)
        print("The response of CloudCredentialApi->cloudcredentials_update_ip_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCredentialApi->cloudcredentials_update_ip_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_used_ip_addresses_command** | [**UpdateUsedIpAddressesCommand**](UpdateUsedIpAddressesCommand.md)|  | 

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

