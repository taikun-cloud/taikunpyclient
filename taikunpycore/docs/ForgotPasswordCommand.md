# ForgotPasswordCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.forgot_password_command import ForgotPasswordCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ForgotPasswordCommand from a JSON string
forgot_password_command_instance = ForgotPasswordCommand.from_json(json)
# print the JSON string representation of the object
print(ForgotPasswordCommand.to_json())

# convert the object into a dict
forgot_password_command_dict = forgot_password_command_instance.to_dict()
# create an instance of ForgotPasswordCommand from a dict
forgot_password_command_from_dict = ForgotPasswordCommand.from_dict(forgot_password_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


