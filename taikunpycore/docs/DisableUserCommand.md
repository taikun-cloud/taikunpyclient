# DisableUserCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**disable** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.disable_user_command import DisableUserCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DisableUserCommand from a JSON string
disable_user_command_instance = DisableUserCommand.from_json(json)
# print the JSON string representation of the object
print(DisableUserCommand.to_json())

# convert the object into a dict
disable_user_command_dict = disable_user_command_instance.to_dict()
# create an instance of DisableUserCommand from a dict
disable_user_command_from_dict = DisableUserCommand.from_dict(disable_user_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


