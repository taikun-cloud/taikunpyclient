# taikunpycore.CheckerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checker_artifact**](CheckerApi.md#checker_artifact) | **POST** /api/v1/checker/artifact | Check artifact url
[**checker_aws**](CheckerApi.md#checker_aws) | **POST** /api/v1/checker/aws | Check aws credential
[**checker_azure**](CheckerApi.md#checker_azure) | **POST** /api/v1/checker/azure | Check azure credentials
[**checker_azure_quota**](CheckerApi.md#checker_azure_quota) | **POST** /api/v1/checker/azure/quota/cpu | Check azure cpu quota
[**checker_cidr**](CheckerApi.md#checker_cidr) | **POST** /api/v1/checker/cidr | Check valid cidr format
[**checker_cron**](CheckerApi.md#checker_cron) | **POST** /api/v1/checker/cron | Check valid cron job format
[**checker_dns**](CheckerApi.md#checker_dns) | **POST** /api/v1/checker/dns | Check valid dns format
[**checker_duplicate_name**](CheckerApi.md#checker_duplicate_name) | **POST** /api/v1/checker/duplicate | Duplicate name
[**checker_google**](CheckerApi.md#checker_google) | **POST** /api/v1/checker/google | Check google credentials
[**checker_helm**](CheckerApi.md#checker_helm) | **POST** /api/v1/checker/helm | Check helm credential
[**checker_import_cluster_kube_config**](CheckerApi.md#checker_import_cluster_kube_config) | **POST** /api/v1/checker/import-cluster-kube-config | Check kube config
[**checker_keycloak**](CheckerApi.md#checker_keycloak) | **POST** /api/v1/checker/keycloak | Check keycloak credential
[**checker_kube_config**](CheckerApi.md#checker_kube_config) | **POST** /api/v1/checker/kube-config | Check kube config
[**checker_node**](CheckerApi.md#checker_node) | **POST** /api/v1/checker/node | Duplicate server name checker
[**checker_ntp**](CheckerApi.md#checker_ntp) | **POST** /api/v1/checker/ntp | Check valid ntp format
[**checker_open_ai**](CheckerApi.md#checker_open_ai) | **POST** /api/v1/checker/openai | Check open-ai token
[**checker_openstack**](CheckerApi.md#checker_openstack) | **POST** /api/v1/checker/openstack | Check openstack credential
[**checker_openstack_taikun_image**](CheckerApi.md#checker_openstack_taikun_image) | **POST** /api/v1/checker/openstack-image/{id} | Check openstack taikun image
[**checker_openstack_taikun_lb_image**](CheckerApi.md#checker_openstack_taikun_lb_image) | **POST** /api/v1/checker/taikun-lb-image/{id} | Check openstack taikun lb image
[**checker_organization**](CheckerApi.md#checker_organization) | **POST** /api/v1/checker/organization | Check duplicate org name
[**checker_prometheus**](CheckerApi.md#checker_prometheus) | **POST** /api/v1/checker/prometheus | Check prometheus credentials
[**checker_proxmox**](CheckerApi.md#checker_proxmox) | **POST** /api/v1/checker/proxmox | Check proxmox credential
[**checker_s3**](CheckerApi.md#checker_s3) | **POST** /api/v1/checker/s3 | Check s3 credential
[**checker_ssh**](CheckerApi.md#checker_ssh) | **POST** /api/v1/checker/ssh | Check valid ssh key format
[**checker_tanzu**](CheckerApi.md#checker_tanzu) | **POST** /api/v1/checker/tanzu | Check tanzu credential
[**checker_user**](CheckerApi.md#checker_user) | **POST** /api/v1/checker/user | Check duplicate username
[**checker_yaml**](CheckerApi.md#checker_yaml) | **POST** /api/v1/checker/yaml | Check yaml file
[**checker_zadara**](CheckerApi.md#checker_zadara) | **POST** /api/v1/checker/zadara | Check zadara credential
[**checker_zededa**](CheckerApi.md#checker_zededa) | **POST** /api/v1/checker/zededa | Check zededa credential


# **checker_artifact**
> object checker_artifact(artifact_url_checker_command=artifact_url_checker_command)

Check artifact url

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.artifact_url_checker_command import ArtifactUrlCheckerCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    artifact_url_checker_command = taikunpycore.ArtifactUrlCheckerCommand() # ArtifactUrlCheckerCommand |  (optional)

    try:
        # Check artifact url
        api_response = api_instance.checker_artifact(artifact_url_checker_command=artifact_url_checker_command)
        print("The response of CheckerApi->checker_artifact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_artifact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_url_checker_command** | [**ArtifactUrlCheckerCommand**](ArtifactUrlCheckerCommand.md)|  | [optional] 

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

# **checker_aws**
> object checker_aws(check_aws_command)

Check aws credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.check_aws_command import CheckAwsCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    check_aws_command = taikunpycore.CheckAwsCommand() # CheckAwsCommand | 

    try:
        # Check aws credential
        api_response = api_instance.checker_aws(check_aws_command)
        print("The response of CheckerApi->checker_aws:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_aws: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_aws_command** | [**CheckAwsCommand**](CheckAwsCommand.md)|  | 

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

# **checker_azure**
> object checker_azure(check_azure_command)

Check azure credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.check_azure_command import CheckAzureCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    check_azure_command = taikunpycore.CheckAzureCommand() # CheckAzureCommand | 

    try:
        # Check azure credentials
        api_response = api_instance.checker_azure(check_azure_command)
        print("The response of CheckerApi->checker_azure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_azure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_azure_command** | [**CheckAzureCommand**](CheckAzureCommand.md)|  | 

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

# **checker_azure_quota**
> object checker_azure_quota(check_azure_cpu_quota_command)

Check azure cpu quota

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.check_azure_cpu_quota_command import CheckAzureCpuQuotaCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    check_azure_cpu_quota_command = taikunpycore.CheckAzureCpuQuotaCommand() # CheckAzureCpuQuotaCommand | 

    try:
        # Check azure cpu quota
        api_response = api_instance.checker_azure_quota(check_azure_cpu_quota_command)
        print("The response of CheckerApi->checker_azure_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_azure_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_azure_cpu_quota_command** | [**CheckAzureCpuQuotaCommand**](CheckAzureCpuQuotaCommand.md)|  | 

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

# **checker_cidr**
> object checker_cidr(cidr_command)

Check valid cidr format

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.cidr_command import CidrCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    cidr_command = taikunpycore.CidrCommand() # CidrCommand | 

    try:
        # Check valid cidr format
        api_response = api_instance.checker_cidr(cidr_command)
        print("The response of CheckerApi->checker_cidr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_cidr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cidr_command** | [**CidrCommand**](CidrCommand.md)|  | 

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

# **checker_cron**
> object checker_cron(cron_job_command)

Check valid cron job format

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.cron_job_command import CronJobCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    cron_job_command = taikunpycore.CronJobCommand() # CronJobCommand | 

    try:
        # Check valid cron job format
        api_response = api_instance.checker_cron(cron_job_command)
        print("The response of CheckerApi->checker_cron:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_cron: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cron_job_command** | [**CronJobCommand**](CronJobCommand.md)|  | 

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

# **checker_dns**
> object checker_dns(dns_command)

Check valid dns format

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.dns_command import DnsCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    dns_command = taikunpycore.DnsCommand() # DnsCommand | 

    try:
        # Check valid dns format
        api_response = api_instance.checker_dns(dns_command)
        print("The response of CheckerApi->checker_dns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_dns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dns_command** | [**DnsCommand**](DnsCommand.md)|  | 

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

# **checker_duplicate_name**
> bool checker_duplicate_name(duplicate_name_checker_command)

Duplicate name

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.duplicate_name_checker_command import DuplicateNameCheckerCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    duplicate_name_checker_command = taikunpycore.DuplicateNameCheckerCommand() # DuplicateNameCheckerCommand | 

    try:
        # Duplicate name
        api_response = api_instance.checker_duplicate_name(duplicate_name_checker_command)
        print("The response of CheckerApi->checker_duplicate_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_duplicate_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duplicate_name_checker_command** | [**DuplicateNameCheckerCommand**](DuplicateNameCheckerCommand.md)|  | 

### Return type

**bool**

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

# **checker_google**
> bool checker_google(config=config)

Check google credentials

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
    api_instance = taikunpycore.CheckerApi(api_client)
    config = None # bytearray |  (optional)

    try:
        # Check google credentials
        api_response = api_instance.checker_google(config=config)
        print("The response of CheckerApi->checker_google:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_google: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | **bytearray**|  | [optional] 

### Return type

**bool**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **checker_helm**
> object checker_helm(helm_credential_command=helm_credential_command)

Check helm credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.helm_credential_command import HelmCredentialCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    helm_credential_command = taikunpycore.HelmCredentialCommand() # HelmCredentialCommand |  (optional)

    try:
        # Check helm credential
        api_response = api_instance.checker_helm(helm_credential_command=helm_credential_command)
        print("The response of CheckerApi->checker_helm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_helm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_credential_command** | [**HelmCredentialCommand**](HelmCredentialCommand.md)|  | [optional] 

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

# **checker_import_cluster_kube_config**
> object checker_import_cluster_kube_config(config=config, cloud_id=cloud_id, region=region, import_cluster_name=import_cluster_name, resource_group_name=resource_group_name, import_type=import_type)

Check kube config

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.e_import_cluster_type import EImportClusterType
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
    api_instance = taikunpycore.CheckerApi(api_client)
    config = None # bytearray |  (optional)
    cloud_id = 56 # int |  (optional)
    region = 'region_example' # str |  (optional)
    import_cluster_name = 'import_cluster_name_example' # str |  (optional)
    resource_group_name = 'resource_group_name_example' # str |  (optional)
    import_type = taikunpycore.EImportClusterType() # EImportClusterType |  (optional)

    try:
        # Check kube config
        api_response = api_instance.checker_import_cluster_kube_config(config=config, cloud_id=cloud_id, region=region, import_cluster_name=import_cluster_name, resource_group_name=resource_group_name, import_type=import_type)
        print("The response of CheckerApi->checker_import_cluster_kube_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_import_cluster_kube_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | **bytearray**|  | [optional] 
 **cloud_id** | **int**|  | [optional] 
 **region** | **str**|  | [optional] 
 **import_cluster_name** | **str**|  | [optional] 
 **resource_group_name** | **str**|  | [optional] 
 **import_type** | [**EImportClusterType**](EImportClusterType.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **checker_keycloak**
> object checker_keycloak(keycloak_checker_command)

Check keycloak credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.keycloak_checker_command import KeycloakCheckerCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    keycloak_checker_command = taikunpycore.KeycloakCheckerCommand() # KeycloakCheckerCommand | 

    try:
        # Check keycloak credential
        api_response = api_instance.checker_keycloak(keycloak_checker_command)
        print("The response of CheckerApi->checker_keycloak:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_keycloak: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keycloak_checker_command** | [**KeycloakCheckerCommand**](KeycloakCheckerCommand.md)|  | 

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

# **checker_kube_config**
> bool checker_kube_config(config=config)

Check kube config

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
    api_instance = taikunpycore.CheckerApi(api_client)
    config = None # bytearray |  (optional)

    try:
        # Check kube config
        api_response = api_instance.checker_kube_config(config=config)
        print("The response of CheckerApi->checker_kube_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_kube_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | **bytearray**|  | [optional] 

### Return type

**bool**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **checker_node**
> object checker_node(node_command)

Duplicate server name checker

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.node_command import NodeCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    node_command = taikunpycore.NodeCommand() # NodeCommand | 

    try:
        # Duplicate server name checker
        api_response = api_instance.checker_node(node_command)
        print("The response of CheckerApi->checker_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_command** | [**NodeCommand**](NodeCommand.md)|  | 

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

# **checker_ntp**
> object checker_ntp(ntp_command)

Check valid ntp format

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.ntp_command import NtpCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    ntp_command = taikunpycore.NtpCommand() # NtpCommand | 

    try:
        # Check valid ntp format
        api_response = api_instance.checker_ntp(ntp_command)
        print("The response of CheckerApi->checker_ntp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_ntp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ntp_command** | [**NtpCommand**](NtpCommand.md)|  | 

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

# **checker_open_ai**
> object checker_open_ai(open_ai_checker_command)

Check open-ai token

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.open_ai_checker_command import OpenAiCheckerCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    open_ai_checker_command = taikunpycore.OpenAiCheckerCommand() # OpenAiCheckerCommand | 

    try:
        # Check open-ai token
        api_response = api_instance.checker_open_ai(open_ai_checker_command)
        print("The response of CheckerApi->checker_open_ai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_open_ai: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_ai_checker_command** | [**OpenAiCheckerCommand**](OpenAiCheckerCommand.md)|  | 

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

# **checker_openstack**
> object checker_openstack(check_openstack_command=check_openstack_command)

Check openstack credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.check_openstack_command import CheckOpenstackCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    check_openstack_command = taikunpycore.CheckOpenstackCommand() # CheckOpenstackCommand |  (optional)

    try:
        # Check openstack credential
        api_response = api_instance.checker_openstack(check_openstack_command=check_openstack_command)
        print("The response of CheckerApi->checker_openstack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_openstack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_openstack_command** | [**CheckOpenstackCommand**](CheckOpenstackCommand.md)|  | [optional] 

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

# **checker_openstack_taikun_image**
> object checker_openstack_taikun_image(id)

Check openstack taikun image

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
    api_instance = taikunpycore.CheckerApi(api_client)
    id = 56 # int | 

    try:
        # Check openstack taikun image
        api_response = api_instance.checker_openstack_taikun_image(id)
        print("The response of CheckerApi->checker_openstack_taikun_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_openstack_taikun_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **checker_openstack_taikun_lb_image**
> object checker_openstack_taikun_lb_image(id)

Check openstack taikun lb image

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
    api_instance = taikunpycore.CheckerApi(api_client)
    id = 56 # int | 

    try:
        # Check openstack taikun lb image
        api_response = api_instance.checker_openstack_taikun_lb_image(id)
        print("The response of CheckerApi->checker_openstack_taikun_lb_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_openstack_taikun_lb_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **checker_organization**
> object checker_organization(organization_name_checker_command)

Check duplicate org name

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.organization_name_checker_command import OrganizationNameCheckerCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    organization_name_checker_command = taikunpycore.OrganizationNameCheckerCommand() # OrganizationNameCheckerCommand | 

    try:
        # Check duplicate org name
        api_response = api_instance.checker_organization(organization_name_checker_command)
        print("The response of CheckerApi->checker_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name_checker_command** | [**OrganizationNameCheckerCommand**](OrganizationNameCheckerCommand.md)|  | 

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

# **checker_prometheus**
> object checker_prometheus(check_prometheus_command)

Check prometheus credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.check_prometheus_command import CheckPrometheusCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    check_prometheus_command = taikunpycore.CheckPrometheusCommand() # CheckPrometheusCommand | 

    try:
        # Check prometheus credentials
        api_response = api_instance.checker_prometheus(check_prometheus_command)
        print("The response of CheckerApi->checker_prometheus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_prometheus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_prometheus_command** | [**CheckPrometheusCommand**](CheckPrometheusCommand.md)|  | 

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

# **checker_proxmox**
> object checker_proxmox(proxmox_checker_command)

Check proxmox credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.proxmox_checker_command import ProxmoxCheckerCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    proxmox_checker_command = taikunpycore.ProxmoxCheckerCommand() # ProxmoxCheckerCommand | 

    try:
        # Check proxmox credential
        api_response = api_instance.checker_proxmox(proxmox_checker_command)
        print("The response of CheckerApi->checker_proxmox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_proxmox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxmox_checker_command** | [**ProxmoxCheckerCommand**](ProxmoxCheckerCommand.md)|  | 

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

# **checker_s3**
> object checker_s3(check_s3_command)

Check s3 credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.check_s3_command import CheckS3Command
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
    api_instance = taikunpycore.CheckerApi(api_client)
    check_s3_command = taikunpycore.CheckS3Command() # CheckS3Command | 

    try:
        # Check s3 credential
        api_response = api_instance.checker_s3(check_s3_command)
        print("The response of CheckerApi->checker_s3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_s3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_s3_command** | [**CheckS3Command**](CheckS3Command.md)|  | 

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

# **checker_ssh**
> object checker_ssh(ssh_key_command)

Check valid ssh key format

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.ssh_key_command import SshKeyCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    ssh_key_command = taikunpycore.SshKeyCommand() # SshKeyCommand | 

    try:
        # Check valid ssh key format
        api_response = api_instance.checker_ssh(ssh_key_command)
        print("The response of CheckerApi->checker_ssh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_ssh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_command** | [**SshKeyCommand**](SshKeyCommand.md)|  | 

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

# **checker_tanzu**
> object checker_tanzu(check_tanzu_command)

Check tanzu credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.check_tanzu_command import CheckTanzuCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    check_tanzu_command = taikunpycore.CheckTanzuCommand() # CheckTanzuCommand | 

    try:
        # Check tanzu credential
        api_response = api_instance.checker_tanzu(check_tanzu_command)
        print("The response of CheckerApi->checker_tanzu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_tanzu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_tanzu_command** | [**CheckTanzuCommand**](CheckTanzuCommand.md)|  | 

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

# **checker_user**
> object checker_user(user_exist_command=user_exist_command)

Check duplicate username

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.user_exist_command import UserExistCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    user_exist_command = taikunpycore.UserExistCommand() # UserExistCommand |  (optional)

    try:
        # Check duplicate username
        api_response = api_instance.checker_user(user_exist_command=user_exist_command)
        print("The response of CheckerApi->checker_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_exist_command** | [**UserExistCommand**](UserExistCommand.md)|  | [optional] 

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

# **checker_yaml**
> object checker_yaml(yaml_validator_command)

Check yaml file

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.yaml_validator_command import YamlValidatorCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    yaml_validator_command = taikunpycore.YamlValidatorCommand() # YamlValidatorCommand | 

    try:
        # Check yaml file
        api_response = api_instance.checker_yaml(yaml_validator_command)
        print("The response of CheckerApi->checker_yaml:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_yaml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **yaml_validator_command** | [**YamlValidatorCommand**](YamlValidatorCommand.md)|  | 

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

# **checker_zadara**
> object checker_zadara(check_zadara_command)

Check zadara credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.check_zadara_command import CheckZadaraCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    check_zadara_command = taikunpycore.CheckZadaraCommand() # CheckZadaraCommand | 

    try:
        # Check zadara credential
        api_response = api_instance.checker_zadara(check_zadara_command)
        print("The response of CheckerApi->checker_zadara:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_zadara: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_zadara_command** | [**CheckZadaraCommand**](CheckZadaraCommand.md)|  | 

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

# **checker_zededa**
> object checker_zededa(zededa_checker_command)

Check zededa credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.zededa_checker_command import ZededaCheckerCommand
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
    api_instance = taikunpycore.CheckerApi(api_client)
    zededa_checker_command = taikunpycore.ZededaCheckerCommand() # ZededaCheckerCommand | 

    try:
        # Check zededa credential
        api_response = api_instance.checker_zededa(zededa_checker_command)
        print("The response of CheckerApi->checker_zededa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->checker_zededa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zededa_checker_command** | [**ZededaCheckerCommand**](ZededaCheckerCommand.md)|  | 

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

