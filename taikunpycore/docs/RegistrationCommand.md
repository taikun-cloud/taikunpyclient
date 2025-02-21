# RegistrationCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.registration_command import RegistrationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationCommand from a JSON string
registration_command_instance = RegistrationCommand.from_json(json)
# print the JSON string representation of the object
print(RegistrationCommand.to_json())

# convert the object into a dict
registration_command_dict = registration_command_instance.to_dict()
# create an instance of RegistrationCommand from a dict
registration_command_from_dict = RegistrationCommand.from_dict(registration_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


