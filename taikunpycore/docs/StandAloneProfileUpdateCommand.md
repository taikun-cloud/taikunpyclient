# StandAloneProfileUpdateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.stand_alone_profile_update_command import StandAloneProfileUpdateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneProfileUpdateCommand from a JSON string
stand_alone_profile_update_command_instance = StandAloneProfileUpdateCommand.from_json(json)
# print the JSON string representation of the object
print(StandAloneProfileUpdateCommand.to_json())

# convert the object into a dict
stand_alone_profile_update_command_dict = stand_alone_profile_update_command_instance.to_dict()
# create an instance of StandAloneProfileUpdateCommand from a dict
stand_alone_profile_update_command_from_dict = StandAloneProfileUpdateCommand.from_dict(stand_alone_profile_update_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


