# taikunpycore.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_access_profiles**](SearchApi.md#search_access_profiles) | **POST** /api/v1/search/access-profiles | Global search for access-profiles
[**search_backup_credentials**](SearchApi.md#search_backup_credentials) | **POST** /api/v1/search/backup-credentials | Global search for backup-credentials
[**search_billing_credentials**](SearchApi.md#search_billing_credentials) | **POST** /api/v1/search/billing-credentials | Global search for billing-credentials
[**search_cloud_credentials**](SearchApi.md#search_cloud_credentials) | **POST** /api/v1/search/cloud-credentials | Global search for cloud-credentials
[**search_config_maps**](SearchApi.md#search_config_maps) | **POST** /api/v1/search/config-maps | Global search for config-maps
[**search_daemon_sets**](SearchApi.md#search_daemon_sets) | **POST** /api/v1/search/daemon-sets | Global search for daemon-sets
[**search_deployments**](SearchApi.md#search_deployments) | **POST** /api/v1/search/deployments | Global search for deployments
[**search_ingress**](SearchApi.md#search_ingress) | **POST** /api/v1/search/ingress | Global search for ingress
[**search_kubernetes_profiles**](SearchApi.md#search_kubernetes_profiles) | **POST** /api/v1/search/kubernetes-profiles | Global search for kubernetes-profiles
[**search_nodes**](SearchApi.md#search_nodes) | **POST** /api/v1/search/nodes | Global search for nodes
[**search_organizations**](SearchApi.md#search_organizations) | **POST** /api/v1/search/organizations | Global search for organizations
[**search_partners**](SearchApi.md#search_partners) | **POST** /api/v1/search/partners | Global search for partners
[**search_pods**](SearchApi.md#search_pods) | **POST** /api/v1/search/pods | Global search for pods
[**search_projects**](SearchApi.md#search_projects) | **POST** /api/v1/search/projects | Global search for projects
[**search_prometheus_rules**](SearchApi.md#search_prometheus_rules) | **POST** /api/v1/search/prometheus-rules | Global search for prometheus-rules
[**search_pvcs**](SearchApi.md#search_pvcs) | **POST** /api/v1/search/pvcs | Global search for pvcs
[**search_secrets**](SearchApi.md#search_secrets) | **POST** /api/v1/search/secrets | Global search for secrets
[**search_servers**](SearchApi.md#search_servers) | **POST** /api/v1/search/servers | Global search for servers
[**search_services**](SearchApi.md#search_services) | **POST** /api/v1/search/services | Global search for services
[**search_stand_alone_profiles**](SearchApi.md#search_stand_alone_profiles) | **POST** /api/v1/search/stand-alone-profiles | Global search for stand-alone-profiles
[**search_sts**](SearchApi.md#search_sts) | **POST** /api/v1/search/sts | Global search for sts
[**search_users**](SearchApi.md#search_users) | **POST** /api/v1/search/users | Global search for users


# **search_access_profiles**
> AccessProfilesSearchList search_access_profiles(access_profiles_search_command)

Global search for access-profiles

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.access_profiles_search_command import AccessProfilesSearchCommand
from taikunpycore.models.access_profiles_search_list import AccessProfilesSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    access_profiles_search_command = taikunpycore.AccessProfilesSearchCommand() # AccessProfilesSearchCommand | 

    try:
        # Global search for access-profiles
        api_response = api_instance.search_access_profiles(access_profiles_search_command)
        print("The response of SearchApi->search_access_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_access_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_profiles_search_command** | [**AccessProfilesSearchCommand**](AccessProfilesSearchCommand.md)|  | 

### Return type

[**AccessProfilesSearchList**](AccessProfilesSearchList.md)

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

# **search_backup_credentials**
> BackupCredentialsSearchList search_backup_credentials(backup_credentials_search_command)

Global search for backup-credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.backup_credentials_search_command import BackupCredentialsSearchCommand
from taikunpycore.models.backup_credentials_search_list import BackupCredentialsSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    backup_credentials_search_command = taikunpycore.BackupCredentialsSearchCommand() # BackupCredentialsSearchCommand | 

    try:
        # Global search for backup-credentials
        api_response = api_instance.search_backup_credentials(backup_credentials_search_command)
        print("The response of SearchApi->search_backup_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_backup_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_credentials_search_command** | [**BackupCredentialsSearchCommand**](BackupCredentialsSearchCommand.md)|  | 

### Return type

[**BackupCredentialsSearchList**](BackupCredentialsSearchList.md)

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

# **search_billing_credentials**
> BillingCredentialsSearchList search_billing_credentials(billing_credentials_search_command)

Global search for billing-credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.billing_credentials_search_command import BillingCredentialsSearchCommand
from taikunpycore.models.billing_credentials_search_list import BillingCredentialsSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    billing_credentials_search_command = taikunpycore.BillingCredentialsSearchCommand() # BillingCredentialsSearchCommand | 

    try:
        # Global search for billing-credentials
        api_response = api_instance.search_billing_credentials(billing_credentials_search_command)
        print("The response of SearchApi->search_billing_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_billing_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_credentials_search_command** | [**BillingCredentialsSearchCommand**](BillingCredentialsSearchCommand.md)|  | 

### Return type

[**BillingCredentialsSearchList**](BillingCredentialsSearchList.md)

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

# **search_cloud_credentials**
> CloudCredentialsSearchList search_cloud_credentials(cloud_credentials_search_command)

Global search for cloud-credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.cloud_credentials_search_command import CloudCredentialsSearchCommand
from taikunpycore.models.cloud_credentials_search_list import CloudCredentialsSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    cloud_credentials_search_command = taikunpycore.CloudCredentialsSearchCommand() # CloudCredentialsSearchCommand | 

    try:
        # Global search for cloud-credentials
        api_response = api_instance.search_cloud_credentials(cloud_credentials_search_command)
        print("The response of SearchApi->search_cloud_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_cloud_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_credentials_search_command** | [**CloudCredentialsSearchCommand**](CloudCredentialsSearchCommand.md)|  | 

### Return type

[**CloudCredentialsSearchList**](CloudCredentialsSearchList.md)

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

# **search_config_maps**
> ConfigMapSearchList search_config_maps(config_map_search_command)

Global search for config-maps

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.config_map_search_command import ConfigMapSearchCommand
from taikunpycore.models.config_map_search_list import ConfigMapSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    config_map_search_command = taikunpycore.ConfigMapSearchCommand() # ConfigMapSearchCommand | 

    try:
        # Global search for config-maps
        api_response = api_instance.search_config_maps(config_map_search_command)
        print("The response of SearchApi->search_config_maps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_config_maps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_map_search_command** | [**ConfigMapSearchCommand**](ConfigMapSearchCommand.md)|  | 

### Return type

[**ConfigMapSearchList**](ConfigMapSearchList.md)

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

# **search_daemon_sets**
> DaemonSetSearchList search_daemon_sets(daemon_set_search_command)

Global search for daemon-sets

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.daemon_set_search_command import DaemonSetSearchCommand
from taikunpycore.models.daemon_set_search_list import DaemonSetSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    daemon_set_search_command = taikunpycore.DaemonSetSearchCommand() # DaemonSetSearchCommand | 

    try:
        # Global search for daemon-sets
        api_response = api_instance.search_daemon_sets(daemon_set_search_command)
        print("The response of SearchApi->search_daemon_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_daemon_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **daemon_set_search_command** | [**DaemonSetSearchCommand**](DaemonSetSearchCommand.md)|  | 

### Return type

[**DaemonSetSearchList**](DaemonSetSearchList.md)

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

# **search_deployments**
> DeploymentSearchList search_deployments(deployment_search_command)

Global search for deployments

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.deployment_search_command import DeploymentSearchCommand
from taikunpycore.models.deployment_search_list import DeploymentSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    deployment_search_command = taikunpycore.DeploymentSearchCommand() # DeploymentSearchCommand | 

    try:
        # Global search for deployments
        api_response = api_instance.search_deployments(deployment_search_command)
        print("The response of SearchApi->search_deployments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_deployments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_search_command** | [**DeploymentSearchCommand**](DeploymentSearchCommand.md)|  | 

### Return type

[**DeploymentSearchList**](DeploymentSearchList.md)

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

# **search_ingress**
> IngressSearchList search_ingress(ingress_search_command)

Global search for ingress

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.ingress_search_command import IngressSearchCommand
from taikunpycore.models.ingress_search_list import IngressSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    ingress_search_command = taikunpycore.IngressSearchCommand() # IngressSearchCommand | 

    try:
        # Global search for ingress
        api_response = api_instance.search_ingress(ingress_search_command)
        print("The response of SearchApi->search_ingress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_ingress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingress_search_command** | [**IngressSearchCommand**](IngressSearchCommand.md)|  | 

### Return type

[**IngressSearchList**](IngressSearchList.md)

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

# **search_kubernetes_profiles**
> KubernetesProfilesSearchList search_kubernetes_profiles(kubernetes_profiles_search_command)

Global search for kubernetes-profiles

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_profiles_search_command import KubernetesProfilesSearchCommand
from taikunpycore.models.kubernetes_profiles_search_list import KubernetesProfilesSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    kubernetes_profiles_search_command = taikunpycore.KubernetesProfilesSearchCommand() # KubernetesProfilesSearchCommand | 

    try:
        # Global search for kubernetes-profiles
        api_response = api_instance.search_kubernetes_profiles(kubernetes_profiles_search_command)
        print("The response of SearchApi->search_kubernetes_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_kubernetes_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_profiles_search_command** | [**KubernetesProfilesSearchCommand**](KubernetesProfilesSearchCommand.md)|  | 

### Return type

[**KubernetesProfilesSearchList**](KubernetesProfilesSearchList.md)

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

# **search_nodes**
> NodesSearchList search_nodes(nodes_search_command)

Global search for nodes

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.nodes_search_command import NodesSearchCommand
from taikunpycore.models.nodes_search_list import NodesSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    nodes_search_command = taikunpycore.NodesSearchCommand() # NodesSearchCommand | 

    try:
        # Global search for nodes
        api_response = api_instance.search_nodes(nodes_search_command)
        print("The response of SearchApi->search_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodes_search_command** | [**NodesSearchCommand**](NodesSearchCommand.md)|  | 

### Return type

[**NodesSearchList**](NodesSearchList.md)

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

# **search_organizations**
> OrganizationSearchList search_organizations(organization_search_command)

Global search for organizations

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.organization_search_command import OrganizationSearchCommand
from taikunpycore.models.organization_search_list import OrganizationSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    organization_search_command = taikunpycore.OrganizationSearchCommand() # OrganizationSearchCommand | 

    try:
        # Global search for organizations
        api_response = api_instance.search_organizations(organization_search_command)
        print("The response of SearchApi->search_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_search_command** | [**OrganizationSearchCommand**](OrganizationSearchCommand.md)|  | 

### Return type

[**OrganizationSearchList**](OrganizationSearchList.md)

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

# **search_partners**
> PartnersSearchList search_partners(partners_search_command=partners_search_command)

Global search for partners

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.partners_search_command import PartnersSearchCommand
from taikunpycore.models.partners_search_list import PartnersSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    partners_search_command = taikunpycore.PartnersSearchCommand() # PartnersSearchCommand |  (optional)

    try:
        # Global search for partners
        api_response = api_instance.search_partners(partners_search_command=partners_search_command)
        print("The response of SearchApi->search_partners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_partners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partners_search_command** | [**PartnersSearchCommand**](PartnersSearchCommand.md)|  | [optional] 

### Return type

[**PartnersSearchList**](PartnersSearchList.md)

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

# **search_pods**
> PodsSearchList search_pods(pods_search_command)

Global search for pods

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.pods_search_command import PodsSearchCommand
from taikunpycore.models.pods_search_list import PodsSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    pods_search_command = taikunpycore.PodsSearchCommand() # PodsSearchCommand | 

    try:
        # Global search for pods
        api_response = api_instance.search_pods(pods_search_command)
        print("The response of SearchApi->search_pods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_pods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pods_search_command** | [**PodsSearchCommand**](PodsSearchCommand.md)|  | 

### Return type

[**PodsSearchList**](PodsSearchList.md)

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

# **search_projects**
> ProjectsSearchList search_projects(projects_search_command)

Global search for projects

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.projects_search_command import ProjectsSearchCommand
from taikunpycore.models.projects_search_list import ProjectsSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    projects_search_command = taikunpycore.ProjectsSearchCommand() # ProjectsSearchCommand | 

    try:
        # Global search for projects
        api_response = api_instance.search_projects(projects_search_command)
        print("The response of SearchApi->search_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_search_command** | [**ProjectsSearchCommand**](ProjectsSearchCommand.md)|  | 

### Return type

[**ProjectsSearchList**](ProjectsSearchList.md)

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

# **search_prometheus_rules**
> PrometheusRulesSearchList search_prometheus_rules(prometheus_rules_search_command)

Global search for prometheus-rules

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.prometheus_rules_search_command import PrometheusRulesSearchCommand
from taikunpycore.models.prometheus_rules_search_list import PrometheusRulesSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    prometheus_rules_search_command = taikunpycore.PrometheusRulesSearchCommand() # PrometheusRulesSearchCommand | 

    try:
        # Global search for prometheus-rules
        api_response = api_instance.search_prometheus_rules(prometheus_rules_search_command)
        print("The response of SearchApi->search_prometheus_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_prometheus_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prometheus_rules_search_command** | [**PrometheusRulesSearchCommand**](PrometheusRulesSearchCommand.md)|  | 

### Return type

[**PrometheusRulesSearchList**](PrometheusRulesSearchList.md)

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

# **search_pvcs**
> PvcSearchList search_pvcs(pvc_search_command)

Global search for pvcs

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.pvc_search_command import PvcSearchCommand
from taikunpycore.models.pvc_search_list import PvcSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    pvc_search_command = taikunpycore.PvcSearchCommand() # PvcSearchCommand | 

    try:
        # Global search for pvcs
        api_response = api_instance.search_pvcs(pvc_search_command)
        print("The response of SearchApi->search_pvcs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_pvcs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pvc_search_command** | [**PvcSearchCommand**](PvcSearchCommand.md)|  | 

### Return type

[**PvcSearchList**](PvcSearchList.md)

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

# **search_secrets**
> SecretSearchList search_secrets(secret_search_command)

Global search for secrets

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.secret_search_command import SecretSearchCommand
from taikunpycore.models.secret_search_list import SecretSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    secret_search_command = taikunpycore.SecretSearchCommand() # SecretSearchCommand | 

    try:
        # Global search for secrets
        api_response = api_instance.search_secrets(secret_search_command)
        print("The response of SearchApi->search_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_search_command** | [**SecretSearchCommand**](SecretSearchCommand.md)|  | 

### Return type

[**SecretSearchList**](SecretSearchList.md)

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

# **search_servers**
> ServersSearchList search_servers(servers_search_command)

Global search for servers

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.servers_search_command import ServersSearchCommand
from taikunpycore.models.servers_search_list import ServersSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    servers_search_command = taikunpycore.ServersSearchCommand() # ServersSearchCommand | 

    try:
        # Global search for servers
        api_response = api_instance.search_servers(servers_search_command)
        print("The response of SearchApi->search_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **servers_search_command** | [**ServersSearchCommand**](ServersSearchCommand.md)|  | 

### Return type

[**ServersSearchList**](ServersSearchList.md)

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

# **search_services**
> ServiceSearchList search_services(service_search_command)

Global search for services

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.service_search_command import ServiceSearchCommand
from taikunpycore.models.service_search_list import ServiceSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    service_search_command = taikunpycore.ServiceSearchCommand() # ServiceSearchCommand | 

    try:
        # Global search for services
        api_response = api_instance.search_services(service_search_command)
        print("The response of SearchApi->search_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_search_command** | [**ServiceSearchCommand**](ServiceSearchCommand.md)|  | 

### Return type

[**ServiceSearchList**](ServiceSearchList.md)

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

# **search_stand_alone_profiles**
> StandAloneProfilesSearchList search_stand_alone_profiles(stand_alone_profiles_search_command)

Global search for stand-alone-profiles

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.stand_alone_profiles_search_command import StandAloneProfilesSearchCommand
from taikunpycore.models.stand_alone_profiles_search_list import StandAloneProfilesSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    stand_alone_profiles_search_command = taikunpycore.StandAloneProfilesSearchCommand() # StandAloneProfilesSearchCommand | 

    try:
        # Global search for stand-alone-profiles
        api_response = api_instance.search_stand_alone_profiles(stand_alone_profiles_search_command)
        print("The response of SearchApi->search_stand_alone_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_stand_alone_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stand_alone_profiles_search_command** | [**StandAloneProfilesSearchCommand**](StandAloneProfilesSearchCommand.md)|  | 

### Return type

[**StandAloneProfilesSearchList**](StandAloneProfilesSearchList.md)

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

# **search_sts**
> StsSearchList search_sts(sts_search_command)

Global search for sts

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.sts_search_command import StsSearchCommand
from taikunpycore.models.sts_search_list import StsSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    sts_search_command = taikunpycore.StsSearchCommand() # StsSearchCommand | 

    try:
        # Global search for sts
        api_response = api_instance.search_sts(sts_search_command)
        print("The response of SearchApi->search_sts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_sts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sts_search_command** | [**StsSearchCommand**](StsSearchCommand.md)|  | 

### Return type

[**StsSearchList**](StsSearchList.md)

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

# **search_users**
> UsersSearchList search_users(users_search_command)

Global search for users

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.users_search_command import UsersSearchCommand
from taikunpycore.models.users_search_list import UsersSearchList
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
    api_instance = taikunpycore.SearchApi(api_client)
    users_search_command = taikunpycore.UsersSearchCommand() # UsersSearchCommand | 

    try:
        # Global search for users
        api_response = api_instance.search_users(users_search_command)
        print("The response of SearchApi->search_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_search_command** | [**UsersSearchCommand**](UsersSearchCommand.md)|  | 

### Return type

[**UsersSearchList**](UsersSearchList.md)

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

