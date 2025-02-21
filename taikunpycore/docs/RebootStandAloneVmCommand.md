# RebootStandAloneVmCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.reboot_stand_alone_vm_command import RebootStandAloneVmCommand

# TODO update the JSON string below
json = "{}"
# create an instance of RebootStandAloneVmCommand from a JSON string
reboot_stand_alone_vm_command_instance = RebootStandAloneVmCommand.from_json(json)
# print the JSON string representation of the object
print(RebootStandAloneVmCommand.to_json())

# convert the object into a dict
reboot_stand_alone_vm_command_dict = reboot_stand_alone_vm_command_instance.to_dict()
# create an instance of RebootStandAloneVmCommand from a dict
reboot_stand_alone_vm_command_from_dict = RebootStandAloneVmCommand.from_dict(reboot_stand_alone_vm_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


