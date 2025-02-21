# ToggleTwoFactorAuthenticationCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.toggle_two_factor_authentication_command import ToggleTwoFactorAuthenticationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleTwoFactorAuthenticationCommand from a JSON string
toggle_two_factor_authentication_command_instance = ToggleTwoFactorAuthenticationCommand.from_json(json)
# print the JSON string representation of the object
print(ToggleTwoFactorAuthenticationCommand.to_json())

# convert the object into a dict
toggle_two_factor_authentication_command_dict = toggle_two_factor_authentication_command_instance.to_dict()
# create an instance of ToggleTwoFactorAuthenticationCommand from a dict
toggle_two_factor_authentication_command_from_dict = ToggleTwoFactorAuthenticationCommand.from_dict(toggle_two_factor_authentication_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


