# StandAloneProfileCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**security_groups** | [**List[StandAloneProfileSecurityGroupDto]**](StandAloneProfileSecurityGroupDto.md) |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.stand_alone_profile_create_command import StandAloneProfileCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneProfileCreateCommand from a JSON string
stand_alone_profile_create_command_instance = StandAloneProfileCreateCommand.from_json(json)
# print the JSON string representation of the object
print(StandAloneProfileCreateCommand.to_json())

# convert the object into a dict
stand_alone_profile_create_command_dict = stand_alone_profile_create_command_instance.to_dict()
# create an instance of StandAloneProfileCreateCommand from a dict
stand_alone_profile_create_command_from_dict = StandAloneProfileCreateCommand.from_dict(stand_alone_profile_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


