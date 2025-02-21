# UpdateStandAloneVmFlavorCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**flavor** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_stand_alone_vm_flavor_command import UpdateStandAloneVmFlavorCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStandAloneVmFlavorCommand from a JSON string
update_stand_alone_vm_flavor_command_instance = UpdateStandAloneVmFlavorCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateStandAloneVmFlavorCommand.to_json())

# convert the object into a dict
update_stand_alone_vm_flavor_command_dict = update_stand_alone_vm_flavor_command_instance.to_dict()
# create an instance of UpdateStandAloneVmFlavorCommand from a dict
update_stand_alone_vm_flavor_command_from_dict = UpdateStandAloneVmFlavorCommand.from_dict(update_stand_alone_vm_flavor_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


