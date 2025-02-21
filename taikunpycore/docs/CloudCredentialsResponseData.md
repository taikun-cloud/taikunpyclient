# CloudCredentialsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**cloud_type** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.cloud_credentials_response_data import CloudCredentialsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CloudCredentialsResponseData from a JSON string
cloud_credentials_response_data_instance = CloudCredentialsResponseData.from_json(json)
# print the JSON string representation of the object
print(CloudCredentialsResponseData.to_json())

# convert the object into a dict
cloud_credentials_response_data_dict = cloud_credentials_response_data_instance.to_dict()
# create an instance of CloudCredentialsResponseData from a dict
cloud_credentials_response_data_from_dict = CloudCredentialsResponseData.from_dict(cloud_credentials_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


