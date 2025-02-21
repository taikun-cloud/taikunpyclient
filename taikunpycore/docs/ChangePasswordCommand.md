# ChangePasswordCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**new_password** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.change_password_command import ChangePasswordCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePasswordCommand from a JSON string
change_password_command_instance = ChangePasswordCommand.from_json(json)
# print the JSON string representation of the object
print(ChangePasswordCommand.to_json())

# convert the object into a dict
change_password_command_dict = change_password_command_instance.to_dict()
# create an instance of ChangePasswordCommand from a dict
change_password_command_from_dict = ChangePasswordCommand.from_dict(change_password_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


