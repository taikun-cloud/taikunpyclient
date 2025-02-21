# CloudCredentialsSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.cloud_credentials_search_command import CloudCredentialsSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CloudCredentialsSearchCommand from a JSON string
cloud_credentials_search_command_instance = CloudCredentialsSearchCommand.from_json(json)
# print the JSON string representation of the object
print(CloudCredentialsSearchCommand.to_json())

# convert the object into a dict
cloud_credentials_search_command_dict = cloud_credentials_search_command_instance.to_dict()
# create an instance of CloudCredentialsSearchCommand from a dict
cloud_credentials_search_command_from_dict = CloudCredentialsSearchCommand.from_dict(cloud_credentials_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


