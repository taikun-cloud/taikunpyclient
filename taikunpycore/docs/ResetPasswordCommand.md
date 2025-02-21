# ResetPasswordCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**new_password** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.reset_password_command import ResetPasswordCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ResetPasswordCommand from a JSON string
reset_password_command_instance = ResetPasswordCommand.from_json(json)
# print the JSON string representation of the object
print(ResetPasswordCommand.to_json())

# convert the object into a dict
reset_password_command_dict = reset_password_command_instance.to_dict()
# create an instance of ResetPasswordCommand from a dict
reset_password_command_from_dict = ResetPasswordCommand.from_dict(reset_password_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


