# taikunpycore.AWSCloudCredentialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aws_create**](AWSCloudCredentialApi.md#aws_create) | **POST** /api/v1/aws/create | Add Aws credentials
[**aws_eks_clusters**](AWSCloudCredentialApi.md#aws_eks_clusters) | **GET** /api/v1/aws/eks-clusters/{cloudId} | Retrieve eks clusters list
[**aws_eks_node_groups**](AWSCloudCredentialApi.md#aws_eks_node_groups) | **GET** /api/v1/aws/eks-node-groups/{projectId} | Retrieve eks node group list
[**aws_list**](AWSCloudCredentialApi.md#aws_list) | **GET** /api/v1/aws/list | Retrieve list of aws cloud credentials
[**aws_owners**](AWSCloudCredentialApi.md#aws_owners) | **GET** /api/v1/aws/owners | Retrieve aws verified owner list
[**aws_regionlist**](AWSCloudCredentialApi.md#aws_regionlist) | **POST** /api/v1/aws/regions | Retrieve aws regions list
[**aws_update**](AWSCloudCredentialApi.md#aws_update) | **POST** /api/v1/aws/update | Update AWS credentials
[**aws_validate_owners**](AWSCloudCredentialApi.md#aws_validate_owners) | **POST** /api/v1/aws/validate-owners | Aws validate owners
[**aws_zones**](AWSCloudCredentialApi.md#aws_zones) | **POST** /api/v1/aws/zones | Fetch Aws zones


# **aws_create**
> ApiResponse aws_create(create_aws_cloud_command=create_aws_cloud_command)

Add Aws credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_aws_cloud_command import CreateAwsCloudCommand
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
    api_instance = taikunpycore.AWSCloudCredentialApi(api_client)
    create_aws_cloud_command = {"name":"taikun","awsSecretAccessKey":"rd98DUXrLkcxI5rqcimJD2BkrsRUZmbqBSwcAcIm","awsAccessKeyId":"X9BZGP8TSTB7D4K6N9U8","azCount":1,"awsRegion":"ap-south-1","organizationId":1} # CreateAwsCloudCommand |  (optional)

    try:
        # Add Aws credentials
        api_response = api_instance.aws_create(create_aws_cloud_command=create_aws_cloud_command)
        print("The response of AWSCloudCredentialApi->aws_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AWSCloudCredentialApi->aws_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_aws_cloud_command** | [**CreateAwsCloudCommand**](CreateAwsCloudCommand.md)|  | [optional] 

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

# **aws_eks_clusters**
> List[str] aws_eks_clusters(cloud_id, region=region)

Retrieve eks clusters list

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
    api_instance = taikunpycore.AWSCloudCredentialApi(api_client)
    cloud_id = 56 # int | 
    region = 'region_example' # str |  (optional)

    try:
        # Retrieve eks clusters list
        api_response = api_instance.aws_eks_clusters(cloud_id, region=region)
        print("The response of AWSCloudCredentialApi->aws_eks_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AWSCloudCredentialApi->aws_eks_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **region** | **str**|  | [optional] 

### Return type

**List[str]**

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

# **aws_eks_node_groups**
> List[AwsEksNodeGroupDto] aws_eks_node_groups(project_id)

Retrieve eks node group list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.aws_eks_node_group_dto import AwsEksNodeGroupDto
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
    api_instance = taikunpycore.AWSCloudCredentialApi(api_client)
    project_id = 56 # int | 

    try:
        # Retrieve eks node group list
        api_response = api_instance.aws_eks_node_groups(project_id)
        print("The response of AWSCloudCredentialApi->aws_eks_node_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AWSCloudCredentialApi->aws_eks_node_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**List[AwsEksNodeGroupDto]**](AwsEksNodeGroupDto.md)

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

# **aws_list**
> AwsCredentialList aws_list(organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id, limit=limit, offset=offset)

Retrieve list of aws cloud credentials

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>SortBy</b> - Options: <i>amazonRegion</i>, <i>organizationName</i>, <i>createdAt</i><li><b>SortDirection</b> - Options: <i>asc</i>, <i>desc</i><li><b>Search</b> - Options: <i>name</i>, <i>organizationName</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.aws_credential_list import AwsCredentialList
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
    api_instance = taikunpycore.AWSCloudCredentialApi(api_client)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Retrieve list of aws cloud credentials
        api_response = api_instance.aws_list(organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id, limit=limit, offset=offset)
        print("The response of AWSCloudCredentialApi->aws_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AWSCloudCredentialApi->aws_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**AwsCredentialList**](AwsCredentialList.md)

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

# **aws_owners**
> List[CommonStringBasedDropdownDto] aws_owners()

Retrieve aws verified owner list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_string_based_dropdown_dto import CommonStringBasedDropdownDto
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
    api_instance = taikunpycore.AWSCloudCredentialApi(api_client)

    try:
        # Retrieve aws verified owner list
        api_response = api_instance.aws_owners()
        print("The response of AWSCloudCredentialApi->aws_owners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AWSCloudCredentialApi->aws_owners: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CommonStringBasedDropdownDto]**](CommonStringBasedDropdownDto.md)

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

# **aws_regionlist**
> List[AwsRegionDto] aws_regionlist(region_list_command=region_list_command)

Retrieve aws regions list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.aws_region_dto import AwsRegionDto
from taikunpycore.models.region_list_command import RegionListCommand
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
    api_instance = taikunpycore.AWSCloudCredentialApi(api_client)
    region_list_command = {"awsAccessKeyId":"X9BZGP8TSTB7D4K6N9U8","awsSecretAccessKey":"rd98DUXrLkcxI5rqcimJD2BkrsRUZmbqBSwcAcIm","cloudId":1} # RegionListCommand |  (optional)

    try:
        # Retrieve aws regions list
        api_response = api_instance.aws_regionlist(region_list_command=region_list_command)
        print("The response of AWSCloudCredentialApi->aws_regionlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AWSCloudCredentialApi->aws_regionlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_list_command** | [**RegionListCommand**](RegionListCommand.md)|  | [optional] 

### Return type

[**List[AwsRegionDto]**](AwsRegionDto.md)

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

# **aws_update**
> object aws_update(update_aws_command=update_aws_command)

Update AWS credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_aws_command import UpdateAwsCommand
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
    api_instance = taikunpycore.AWSCloudCredentialApi(api_client)
    update_aws_command = {"id":1,"name":"taikun","awsSecretAccessKey":"rd98DUXrLkcxI5rqcimJD2BkrsRUZmbqBSwcAcIm","awsAccessKeyId":"X9BZGP8TSTB7D4K6N9U8"} # UpdateAwsCommand |  (optional)

    try:
        # Update AWS credentials
        api_response = api_instance.aws_update(update_aws_command=update_aws_command)
        print("The response of AWSCloudCredentialApi->aws_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AWSCloudCredentialApi->aws_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_aws_command** | [**UpdateAwsCommand**](UpdateAwsCommand.md)|  | [optional] 

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

# **aws_validate_owners**
> object aws_validate_owners(aws_validate_owner_command=aws_validate_owner_command)

Aws validate owners

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.aws_validate_owner_command import AwsValidateOwnerCommand
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
    api_instance = taikunpycore.AWSCloudCredentialApi(api_client)
    aws_validate_owner_command = {"cloudId":1,"owners":["amazon"]} # AwsValidateOwnerCommand |  (optional)

    try:
        # Aws validate owners
        api_response = api_instance.aws_validate_owners(aws_validate_owner_command=aws_validate_owner_command)
        print("The response of AWSCloudCredentialApi->aws_validate_owners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AWSCloudCredentialApi->aws_validate_owners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_validate_owner_command** | [**AwsValidateOwnerCommand**](AwsValidateOwnerCommand.md)|  | [optional] 

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

# **aws_zones**
> AzResult aws_zones(amazon_availability_zones_command=amazon_availability_zones_command)

Fetch Aws zones

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.amazon_availability_zones_command import AmazonAvailabilityZonesCommand
from taikunpycore.models.az_result import AzResult
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
    api_instance = taikunpycore.AWSCloudCredentialApi(api_client)
    amazon_availability_zones_command = {"region":"ap-south-1","awsAccessKeyId":"X9BZGP8TSTB7D4K6N9U8","awsSecretAccessKey":"rd98DUXrLkcxI5rqcimJD2BkrsRUZmbqBSwcAcIm","cloudId":1} # AmazonAvailabilityZonesCommand |  (optional)

    try:
        # Fetch Aws zones
        api_response = api_instance.aws_zones(amazon_availability_zones_command=amazon_availability_zones_command)
        print("The response of AWSCloudCredentialApi->aws_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AWSCloudCredentialApi->aws_zones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_availability_zones_command** | [**AmazonAvailabilityZonesCommand**](AmazonAvailabilityZonesCommand.md)|  | [optional] 

### Return type

[**AzResult**](AzResult.md)

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

