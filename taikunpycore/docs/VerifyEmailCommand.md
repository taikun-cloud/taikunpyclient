# VerifyEmailCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**mode** | [**EmailMode**](EmailMode.md) |  | [optional] 

## Example

```python
from taikunpycore.models.verify_email_command import VerifyEmailCommand

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEmailCommand from a JSON string
verify_email_command_instance = VerifyEmailCommand.from_json(json)
# print the JSON string representation of the object
print(VerifyEmailCommand.to_json())

# convert the object into a dict
verify_email_command_dict = verify_email_command_instance.to_dict()
# create an instance of VerifyEmailCommand from a dict
verify_email_command_from_dict = VerifyEmailCommand.from_dict(verify_email_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


