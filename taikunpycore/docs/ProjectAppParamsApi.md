# taikunpycore.ProjectAppParamsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectappparam_edit**](ProjectAppParamsApi.md#projectappparam_edit) | **PUT** /api/v1/projectappparam/edit/{projectAppId} | Edit project app params


# **projectappparam_edit**
> object projectappparam_edit(project_app_id, edit_project_app_params_dto=edit_project_app_params_dto)

Edit project app params

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.edit_project_app_params_dto import EditProjectAppParamsDto
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
    api_instance = taikunpycore.ProjectAppParamsApi(api_client)
    project_app_id = 56 # int | 
    edit_project_app_params_dto = [taikunpycore.EditProjectAppParamsDto()] # List[EditProjectAppParamsDto] |  (optional)

    try:
        # Edit project app params
        api_response = api_instance.projectappparam_edit(project_app_id, edit_project_app_params_dto=edit_project_app_params_dto)
        print("The response of ProjectAppParamsApi->projectappparam_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAppParamsApi->projectappparam_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_app_id** | **int**|  | 
 **edit_project_app_params_dto** | [**List[EditProjectAppParamsDto]**](EditProjectAppParamsDto.md)|  | [optional] 

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

