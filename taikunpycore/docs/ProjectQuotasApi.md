# taikunpycore.ProjectQuotasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectquotas_list**](ProjectQuotasApi.md#projectquotas_list) | **GET** /api/v1/projectquotas | Retrieve all project quotas
[**projectquotas_update**](ProjectQuotasApi.md#projectquotas_update) | **POST** /api/v1/projectquotas/update | Edit project quota


# **projectquotas_list**
> ProjectQuotaList projectquotas_list(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, start_ram=start_ram, end_ram=end_ram, start_disk_size=start_disk_size, end_disk_size=end_disk_size, start_cpu=start_cpu, end_cpu=end_cpu, organization_id=organization_id, id=id)

Retrieve all project quotas

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_quota_list import ProjectQuotaList
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
    api_instance = taikunpycore.ProjectQuotasApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    start_ram = 3.4 # float |  (optional)
    end_ram = 3.4 # float |  (optional)
    start_disk_size = 56 # int |  (optional)
    end_disk_size = 56 # int |  (optional)
    start_cpu = 56 # int |  (optional)
    end_cpu = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve all project quotas
        api_response = api_instance.projectquotas_list(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, start_ram=start_ram, end_ram=end_ram, start_disk_size=start_disk_size, end_disk_size=end_disk_size, start_cpu=start_cpu, end_cpu=end_cpu, organization_id=organization_id, id=id)
        print("The response of ProjectQuotasApi->projectquotas_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectQuotasApi->projectquotas_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **start_ram** | **float**|  | [optional] 
 **end_ram** | **float**|  | [optional] 
 **start_disk_size** | **int**|  | [optional] 
 **end_disk_size** | **int**|  | [optional] 
 **start_cpu** | **int**|  | [optional] 
 **end_cpu** | **int**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **id** | **int**|  | [optional] 

### Return type

[**ProjectQuotaList**](ProjectQuotaList.md)

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

# **projectquotas_update**
> object projectquotas_update(update_quota_command=update_quota_command)

Edit project quota

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_quota_command import UpdateQuotaCommand
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
    api_instance = taikunpycore.ProjectQuotasApi(api_client)
    update_quota_command = taikunpycore.UpdateQuotaCommand() # UpdateQuotaCommand |  (optional)

    try:
        # Edit project quota
        api_response = api_instance.projectquotas_update(update_quota_command=update_quota_command)
        print("The response of ProjectQuotasApi->projectquotas_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectQuotasApi->projectquotas_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_quota_command** | [**UpdateQuotaCommand**](UpdateQuotaCommand.md)|  | [optional] 

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

