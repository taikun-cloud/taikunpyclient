# taikunpycore.AuthManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_forgot_password**](AuthManagementApi.md#auth_forgot_password) | **POST** /api/v1/auth/forgotpassword | Generate reset password token if you forgot password
[**auth_google**](AuthManagementApi.md#auth_google) | **GET** /api/v1/auth/google | Consent to Google
[**auth_login**](AuthManagementApi.md#auth_login) | **POST** /api/v1/auth/login | Login to API
[**auth_refresh**](AuthManagementApi.md#auth_refresh) | **POST** /api/v1/auth/refresh | Refresh bearer token that generated automatically by API
[**auth_reset_password**](AuthManagementApi.md#auth_reset_password) | **POST** /api/v1/auth/resetpassword | Reset password
[**auth_trial**](AuthManagementApi.md#auth_trial) | **POST** /api/v1/auth/trial | New registration
[**auth_verify2fa**](AuthManagementApi.md#auth_verify2fa) | **POST** /api/v1/auth/verify-2fa | Verify 2FA


# **auth_forgot_password**
> object auth_forgot_password(forgot_password_command=forgot_password_command)

Generate reset password token if you forgot password

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.forgot_password_command import ForgotPasswordCommand
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
    api_instance = taikunpycore.AuthManagementApi(api_client)
    forgot_password_command = {"email":"taikun@taikun.cloud"} # ForgotPasswordCommand |  (optional)

    try:
        # Generate reset password token if you forgot password
        api_response = api_instance.auth_forgot_password(forgot_password_command=forgot_password_command)
        print("The response of AuthManagementApi->auth_forgot_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthManagementApi->auth_forgot_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forgot_password_command** | [**ForgotPasswordCommand**](ForgotPasswordCommand.md)|  | [optional] 

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

# **auth_google**
> object auth_google()

Consent to Google

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
    api_instance = taikunpycore.AuthManagementApi(api_client)

    try:
        # Consent to Google
        api_response = api_instance.auth_google()
        print("The response of AuthManagementApi->auth_google:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthManagementApi->auth_google: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **auth_login**
> GetToken auth_login(login_command=login_command)

Login to API

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.get_token import GetToken
from taikunpycore.models.login_command import LoginCommand
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
    api_instance = taikunpycore.AuthManagementApi(api_client)
    login_command = {"email":"taikun@taikun.cloud","password":"P@ssw0rd!","mode":"token|autoscaling|keycloak","accessKey":"X9BZGP8TSTB7D4K6N9U8","secretKey":"rd98DUXrLkcxI5rqcimJD2BkrsRUZmbqBSwcAcIm","local":false} # LoginCommand |  (optional)

    try:
        # Login to API
        api_response = api_instance.auth_login(login_command=login_command)
        print("The response of AuthManagementApi->auth_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthManagementApi->auth_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_command** | [**LoginCommand**](LoginCommand.md)|  | [optional] 

### Return type

[**GetToken**](GetToken.md)

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

# **auth_refresh**
> GetToken auth_refresh(refresh_token_command=refresh_token_command)

Refresh bearer token that generated automatically by API

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.get_token import GetToken
from taikunpycore.models.refresh_token_command import RefreshTokenCommand
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
    api_instance = taikunpycore.AuthManagementApi(api_client)
    refresh_token_command = {"token":"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.xxxxxx","refreshToken":"n2aofltwxksszt-hthvimg"} # RefreshTokenCommand |  (optional)

    try:
        # Refresh bearer token that generated automatically by API
        api_response = api_instance.auth_refresh(refresh_token_command=refresh_token_command)
        print("The response of AuthManagementApi->auth_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthManagementApi->auth_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_command** | [**RefreshTokenCommand**](RefreshTokenCommand.md)|  | [optional] 

### Return type

[**GetToken**](GetToken.md)

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

# **auth_reset_password**
> object auth_reset_password(reset_password_command=reset_password_command)

Reset password

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.reset_password_command import ResetPasswordCommand
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
    api_instance = taikunpycore.AuthManagementApi(api_client)
    reset_password_command = {"token":"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.xxxxxx","email":"taikun@taikun.cloud","newPassword":"P@ssw0rd!"} # ResetPasswordCommand |  (optional)

    try:
        # Reset password
        api_response = api_instance.auth_reset_password(reset_password_command=reset_password_command)
        print("The response of AuthManagementApi->auth_reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthManagementApi->auth_reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_password_command** | [**ResetPasswordCommand**](ResetPasswordCommand.md)|  | [optional] 

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

# **auth_trial**
> object auth_trial(registration_command=registration_command)

New registration

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.registration_command import RegistrationCommand
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
    api_instance = taikunpycore.AuthManagementApi(api_client)
    registration_command = {"organizationName":"taikun.cloud a.s.","username":"taikun","email":"taikun@taikun.cloud"} # RegistrationCommand |  (optional)

    try:
        # New registration
        api_response = api_instance.auth_trial(registration_command=registration_command)
        print("The response of AuthManagementApi->auth_trial:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthManagementApi->auth_trial: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_command** | [**RegistrationCommand**](RegistrationCommand.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_verify2fa**
> List[str] auth_verify2fa(verify_two_factor_token_command)

Verify 2FA

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.verify_two_factor_token_command import VerifyTwoFactorTokenCommand
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
    api_instance = taikunpycore.AuthManagementApi(api_client)
    verify_two_factor_token_command = taikunpycore.VerifyTwoFactorTokenCommand() # VerifyTwoFactorTokenCommand | 

    try:
        # Verify 2FA
        api_response = api_instance.auth_verify2fa(verify_two_factor_token_command)
        print("The response of AuthManagementApi->auth_verify2fa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthManagementApi->auth_verify2fa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_two_factor_token_command** | [**VerifyTwoFactorTokenCommand**](VerifyTwoFactorTokenCommand.md)|  | 

### Return type

**List[str]**

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

