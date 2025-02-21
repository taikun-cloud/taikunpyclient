# ConfirmEmailCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_email** | **str** |  | [optional] 
**mode** | [**EmailMode**](EmailMode.md) |  | [optional] 

## Example

```python
from taikunpycore.models.confirm_email_command import ConfirmEmailCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmEmailCommand from a JSON string
confirm_email_command_instance = ConfirmEmailCommand.from_json(json)
# print the JSON string representation of the object
print(ConfirmEmailCommand.to_json())

# convert the object into a dict
confirm_email_command_dict = confirm_email_command_instance.to_dict()
# create an instance of ConfirmEmailCommand from a dict
confirm_email_command_from_dict = ConfirmEmailCommand.from_dict(confirm_email_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


