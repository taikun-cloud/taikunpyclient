# taikunpycore.SecurityGroupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**securitygroup_create**](SecurityGroupApi.md#securitygroup_create) | **POST** /api/v1/securitygroup/create | Create standalonealone profile security group
[**securitygroup_delete**](SecurityGroupApi.md#securitygroup_delete) | **DELETE** /api/v1/securitygroup/{id} | Delete standalone profile security group
[**securitygroup_edit**](SecurityGroupApi.md#securitygroup_edit) | **PUT** /api/v1/securitygroup/edit | Edit standalone profile security group
[**securitygroup_list**](SecurityGroupApi.md#securitygroup_list) | **GET** /api/v1/securitygroup/list/{standAloneProfileId} | List stand alone security group by profile id


# **securitygroup_create**
> ApiResponse securitygroup_create(create_security_group_command=create_security_group_command)

Create standalonealone profile security group

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_security_group_command import CreateSecurityGroupCommand
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
    api_instance = taikunpycore.SecurityGroupApi(api_client)
    create_security_group_command = taikunpycore.CreateSecurityGroupCommand() # CreateSecurityGroupCommand |  (optional)

    try:
        # Create standalonealone profile security group
        api_response = api_instance.securitygroup_create(create_security_group_command=create_security_group_command)
        print("The response of SecurityGroupApi->securitygroup_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupApi->securitygroup_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_security_group_command** | [**CreateSecurityGroupCommand**](CreateSecurityGroupCommand.md)|  | [optional] 

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

# **securitygroup_delete**
> securitygroup_delete(id)

Delete standalone profile security group

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
    api_instance = taikunpycore.SecurityGroupApi(api_client)
    id = 56 # int | 

    try:
        # Delete standalone profile security group
        api_instance.securitygroup_delete(id)
    except Exception as e:
        print("Exception when calling SecurityGroupApi->securitygroup_delete: %s\n" % e)
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

# **securitygroup_edit**
> object securitygroup_edit(edit_security_group_command=edit_security_group_command)

Edit standalone profile security group

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.edit_security_group_command import EditSecurityGroupCommand
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
    api_instance = taikunpycore.SecurityGroupApi(api_client)
    edit_security_group_command = taikunpycore.EditSecurityGroupCommand() # EditSecurityGroupCommand |  (optional)

    try:
        # Edit standalone profile security group
        api_response = api_instance.securitygroup_edit(edit_security_group_command=edit_security_group_command)
        print("The response of SecurityGroupApi->securitygroup_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupApi->securitygroup_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_security_group_command** | [**EditSecurityGroupCommand**](EditSecurityGroupCommand.md)|  | [optional] 

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

# **securitygroup_list**
> List[SecurityGroupListDto] securitygroup_list(stand_alone_profile_id)

List stand alone security group by profile id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.security_group_list_dto import SecurityGroupListDto
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
    api_instance = taikunpycore.SecurityGroupApi(api_client)
    stand_alone_profile_id = 56 # int | 

    try:
        # List stand alone security group by profile id
        api_response = api_instance.securitygroup_list(stand_alone_profile_id)
        print("The response of SecurityGroupApi->securitygroup_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupApi->securitygroup_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stand_alone_profile_id** | **int**|  | 

### Return type

[**List[SecurityGroupListDto]**](SecurityGroupListDto.md)

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

