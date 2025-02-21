# ValidateVsphereCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.validate_vsphere_command import ValidateVsphereCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateVsphereCommand from a JSON string
validate_vsphere_command_instance = ValidateVsphereCommand.from_json(json)
# print the JSON string representation of the object
print(ValidateVsphereCommand.to_json())

# convert the object into a dict
validate_vsphere_command_dict = validate_vsphere_command_instance.to_dict()
# create an instance of ValidateVsphereCommand from a dict
validate_vsphere_command_from_dict = ValidateVsphereCommand.from_dict(validate_vsphere_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


