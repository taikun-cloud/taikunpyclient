# taikunpycore.ImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**images_aws_common_images**](ImagesApi.md#images_aws_common_images) | **GET** /api/v1/images/aws/common/{cloudId} | Commonly used aws images
[**images_aws_images_list**](ImagesApi.md#images_aws_images_list) | **POST** /api/v1/images/aws | Retrieve aws images
[**images_aws_personal_images**](ImagesApi.md#images_aws_personal_images) | **GET** /api/v1/images/aws/personal/{cloudId} | Aws personal images
[**images_azure_common_images**](ImagesApi.md#images_azure_common_images) | **GET** /api/v1/images/azure/common/{cloudId} | Commonly used azure images
[**images_azure_images**](ImagesApi.md#images_azure_images) | **GET** /api/v1/images/azure/{cloudId}/{publisherName}/{offer}/{sku} | Retrieve azure images
[**images_azure_personal_images**](ImagesApi.md#images_azure_personal_images) | **GET** /api/v1/images/azure/personal/{cloudId} | Azure personal images
[**images_bind_images_to_project**](ImagesApi.md#images_bind_images_to_project) | **POST** /api/v1/images/bind | Bind images to project
[**images_common_google_images**](ImagesApi.md#images_common_google_images) | **GET** /api/v1/images/google/common/{cloudId} | Commonly used google images
[**images_google_images**](ImagesApi.md#images_google_images) | **GET** /api/v1/images/google/{cloudId}/{type} | Retrieve google images
[**images_image_details**](ImagesApi.md#images_image_details) | **POST** /api/v1/images/details | Get image details
[**images_openshift_images**](ImagesApi.md#images_openshift_images) | **GET** /api/v1/images/openshift/{cloudId} | Retrieve openshift images
[**images_openstack_images**](ImagesApi.md#images_openstack_images) | **GET** /api/v1/images/openstack/{cloudId} | Retrieve openstack images
[**images_proxmox_images**](ImagesApi.md#images_proxmox_images) | **GET** /api/v1/images/proxmox/{cloudId} | Retrieve proxmox images
[**images_selected_images_for_project**](ImagesApi.md#images_selected_images_for_project) | **GET** /api/v1/images/projects/list | Retrieve selected images for projects
[**images_tanzu_images**](ImagesApi.md#images_tanzu_images) | **GET** /api/v1/images/tanzu/{cloudId} | Retrieve tanzu images
[**images_unbind_images_from_project**](ImagesApi.md#images_unbind_images_from_project) | **POST** /api/v1/images/unbind | Unbind images from project
[**images_vsphere_images**](ImagesApi.md#images_vsphere_images) | **GET** /api/v1/images/vsphere/{cloudId} | Retrieve vsphere images
[**images_zadara_images_list**](ImagesApi.md#images_zadara_images_list) | **POST** /api/v1/images/zadara/{cloudId} | Retrieve zadara images
[**images_zadara_personal_images**](ImagesApi.md#images_zadara_personal_images) | **GET** /api/v1/images/zadara/personal/{cloudId} | Zadara personal images


# **images_aws_common_images**
> List[CommonStringBasedDropdownDto] images_aws_common_images(cloud_id, project_id=project_id)

Commonly used aws images

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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    project_id = 56 # int |  (optional)

    try:
        # Commonly used aws images
        api_response = api_instance.images_aws_common_images(cloud_id, project_id=project_id)
        print("The response of ImagesApi->images_aws_common_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_aws_common_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **project_id** | **int**|  | [optional] 

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

# **images_aws_images_list**
> PublicImageList images_aws_images_list(aws_images_post_list_command)

Retrieve aws images

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.aws_images_post_list_command import AwsImagesPostListCommand
from taikunpycore.models.public_image_list import PublicImageList
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
    api_instance = taikunpycore.ImagesApi(api_client)
    aws_images_post_list_command = taikunpycore.AwsImagesPostListCommand() # AwsImagesPostListCommand | 

    try:
        # Retrieve aws images
        api_response = api_instance.images_aws_images_list(aws_images_post_list_command)
        print("The response of ImagesApi->images_aws_images_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_aws_images_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_images_post_list_command** | [**AwsImagesPostListCommand**](AwsImagesPostListCommand.md)|  | 

### Return type

[**PublicImageList**](PublicImageList.md)

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

# **images_aws_personal_images**
> List[CommonStringBasedDropdownDto] images_aws_personal_images(cloud_id, search=search, project_id=project_id)

Aws personal images

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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    search = 'search_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Aws personal images
        api_response = api_instance.images_aws_personal_images(cloud_id, search=search, project_id=project_id)
        print("The response of ImagesApi->images_aws_personal_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_aws_personal_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **search** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

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

# **images_azure_common_images**
> List[CommonStringBasedDropdownDto] images_azure_common_images(cloud_id, project_id=project_id)

Commonly used azure images

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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    project_id = 56 # int |  (optional)

    try:
        # Commonly used azure images
        api_response = api_instance.images_azure_common_images(cloud_id, project_id=project_id)
        print("The response of ImagesApi->images_azure_common_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_azure_common_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **project_id** | **int**|  | [optional] 

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

# **images_azure_images**
> PublicImageList images_azure_images(cloud_id, publisher_name, offer, sku, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id, latest=latest)

Retrieve azure images

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.public_image_list import PublicImageList
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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    publisher_name = 'publisher_name_example' # str | 
    offer = 'offer_example' # str | 
    sku = 'sku_example' # str | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    latest = False # bool |  (optional) (default to False)

    try:
        # Retrieve azure images
        api_response = api_instance.images_azure_images(cloud_id, publisher_name, offer, sku, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id, latest=latest)
        print("The response of ImagesApi->images_azure_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_azure_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **publisher_name** | **str**|  | 
 **offer** | **str**|  | 
 **sku** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 
 **latest** | **bool**|  | [optional] [default to False]

### Return type

[**PublicImageList**](PublicImageList.md)

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

# **images_azure_personal_images**
> List[CommonStringBasedDropdownDto] images_azure_personal_images(cloud_id, project_id=project_id)

Azure personal images

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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    project_id = 56 # int |  (optional)

    try:
        # Azure personal images
        api_response = api_instance.images_azure_personal_images(cloud_id, project_id=project_id)
        print("The response of ImagesApi->images_azure_personal_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_azure_personal_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **project_id** | **int**|  | [optional] 

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

# **images_bind_images_to_project**
> object images_bind_images_to_project(bind_image_to_project_command=bind_image_to_project_command)

Bind images to project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.bind_image_to_project_command import BindImageToProjectCommand
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
    api_instance = taikunpycore.ImagesApi(api_client)
    bind_image_to_project_command = taikunpycore.BindImageToProjectCommand() # BindImageToProjectCommand |  (optional)

    try:
        # Bind images to project
        api_response = api_instance.images_bind_images_to_project(bind_image_to_project_command=bind_image_to_project_command)
        print("The response of ImagesApi->images_bind_images_to_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_bind_images_to_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bind_image_to_project_command** | [**BindImageToProjectCommand**](BindImageToProjectCommand.md)|  | [optional] 

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

# **images_common_google_images**
> List[CommonStringBasedDropdownDto] images_common_google_images(cloud_id, project_id=project_id)

Commonly used google images

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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    project_id = 56 # int |  (optional)

    try:
        # Commonly used google images
        api_response = api_instance.images_common_google_images(cloud_id, project_id=project_id)
        print("The response of ImagesApi->images_common_google_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_common_google_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **project_id** | **int**|  | [optional] 

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

# **images_google_images**
> PublicImageList images_google_images(cloud_id, type, latest, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id)

Retrieve google images

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.public_image_list import PublicImageList
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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    type = 'type_example' # str | 
    latest = True # bool | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve google images
        api_response = api_instance.images_google_images(cloud_id, type, latest, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id)
        print("The response of ImagesApi->images_google_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_google_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **type** | **str**|  | 
 **latest** | **bool**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**PublicImageList**](PublicImageList.md)

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

# **images_image_details**
> str images_image_details(image_by_id_command)

Get image details

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.image_by_id_command import ImageByIdCommand
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
    api_instance = taikunpycore.ImagesApi(api_client)
    image_by_id_command = taikunpycore.ImageByIdCommand() # ImageByIdCommand | 

    try:
        # Get image details
        api_response = api_instance.images_image_details(image_by_id_command)
        print("The response of ImagesApi->images_image_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_image_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_by_id_command** | [**ImageByIdCommand**](ImageByIdCommand.md)|  | 

### Return type

**str**

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

# **images_openshift_images**
> PublicImageList images_openshift_images(cloud_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id)

Retrieve openshift images

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.public_image_list import PublicImageList
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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve openshift images
        api_response = api_instance.images_openshift_images(cloud_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id)
        print("The response of ImagesApi->images_openshift_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_openshift_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**PublicImageList**](PublicImageList.md)

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

# **images_openstack_images**
> PublicImageList images_openstack_images(cloud_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id, personal=personal)

Retrieve openstack images

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.public_image_list import PublicImageList
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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    personal = False # bool |  (optional) (default to False)

    try:
        # Retrieve openstack images
        api_response = api_instance.images_openstack_images(cloud_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id, personal=personal)
        print("The response of ImagesApi->images_openstack_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_openstack_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 
 **personal** | **bool**|  | [optional] [default to False]

### Return type

[**PublicImageList**](PublicImageList.md)

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

# **images_proxmox_images**
> PublicImageList images_proxmox_images(cloud_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id)

Retrieve proxmox images

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.public_image_list import PublicImageList
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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve proxmox images
        api_response = api_instance.images_proxmox_images(cloud_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id)
        print("The response of ImagesApi->images_proxmox_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_proxmox_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**PublicImageList**](PublicImageList.md)

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

# **images_selected_images_for_project**
> BoundImagesForProjectsList images_selected_images_for_project(limit=limit, offset=offset, project_id=project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, filter_by=filter_by, organization_id=organization_id)

Retrieve selected images for projects

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.bound_images_for_projects_list import BoundImagesForProjectsList
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
    api_instance = taikunpycore.ImagesApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    project_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)
    organization_id = 56 # int |  (optional)

    try:
        # Retrieve selected images for projects
        api_response = api_instance.images_selected_images_for_project(limit=limit, offset=offset, project_id=project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, filter_by=filter_by, organization_id=organization_id)
        print("The response of ImagesApi->images_selected_images_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_selected_images_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **project_id** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 
 **organization_id** | **int**|  | [optional] 

### Return type

[**BoundImagesForProjectsList**](BoundImagesForProjectsList.md)

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

# **images_tanzu_images**
> PublicImageList images_tanzu_images(cloud_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id)

Retrieve tanzu images

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.public_image_list import PublicImageList
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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve tanzu images
        api_response = api_instance.images_tanzu_images(cloud_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id)
        print("The response of ImagesApi->images_tanzu_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_tanzu_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**PublicImageList**](PublicImageList.md)

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

# **images_unbind_images_from_project**
> object images_unbind_images_from_project(delete_image_from_project_command)

Unbind images from project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_image_from_project_command import DeleteImageFromProjectCommand
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
    api_instance = taikunpycore.ImagesApi(api_client)
    delete_image_from_project_command = taikunpycore.DeleteImageFromProjectCommand() # DeleteImageFromProjectCommand | 

    try:
        # Unbind images from project
        api_response = api_instance.images_unbind_images_from_project(delete_image_from_project_command)
        print("The response of ImagesApi->images_unbind_images_from_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_unbind_images_from_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_image_from_project_command** | [**DeleteImageFromProjectCommand**](DeleteImageFromProjectCommand.md)|  | 

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

# **images_vsphere_images**
> PublicImageList images_vsphere_images(cloud_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id)

Retrieve vsphere images

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.public_image_list import PublicImageList
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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve vsphere images
        api_response = api_instance.images_vsphere_images(cloud_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id)
        print("The response of ImagesApi->images_vsphere_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_vsphere_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**PublicImageList**](PublicImageList.md)

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

# **images_zadara_images_list**
> PublicImageList images_zadara_images_list(cloud_id, latest, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id)

Retrieve zadara images

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.public_image_list import PublicImageList
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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    latest = True # bool | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Retrieve zadara images
        api_response = api_instance.images_zadara_images_list(cloud_id, latest, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, project_id=project_id)
        print("The response of ImagesApi->images_zadara_images_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_zadara_images_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **latest** | **bool**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

### Return type

[**PublicImageList**](PublicImageList.md)

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

# **images_zadara_personal_images**
> List[CommonStringBasedDropdownDto] images_zadara_personal_images(cloud_id, search=search, project_id=project_id)

Zadara personal images

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
    api_instance = taikunpycore.ImagesApi(api_client)
    cloud_id = 56 # int | 
    search = 'search_example' # str |  (optional)
    project_id = 56 # int |  (optional)

    try:
        # Zadara personal images
        api_response = api_instance.images_zadara_personal_images(cloud_id, search=search, project_id=project_id)
        print("The response of ImagesApi->images_zadara_personal_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_zadara_personal_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_id** | **int**|  | 
 **search** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 

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

