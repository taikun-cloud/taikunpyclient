# CreateAllowedHostCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_profile_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**mask_bits** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_allowed_host_command import CreateAllowedHostCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAllowedHostCommand from a JSON string
create_allowed_host_command_instance = CreateAllowedHostCommand.from_json(json)
# print the JSON string representation of the object
print(CreateAllowedHostCommand.to_json())

# convert the object into a dict
create_allowed_host_command_dict = create_allowed_host_command_instance.to_dict()
# create an instance of CreateAllowedHostCommand from a dict
create_allowed_host_command_from_dict = CreateAllowedHostCommand.from_dict(create_allowed_host_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


