# UpdateStandaloneVmDiskSizeCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.update_standalone_vm_disk_size_command import UpdateStandaloneVmDiskSizeCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStandaloneVmDiskSizeCommand from a JSON string
update_standalone_vm_disk_size_command_instance = UpdateStandaloneVmDiskSizeCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateStandaloneVmDiskSizeCommand.to_json())

# convert the object into a dict
update_standalone_vm_disk_size_command_dict = update_standalone_vm_disk_size_command_instance.to_dict()
# create an instance of UpdateStandaloneVmDiskSizeCommand from a dict
update_standalone_vm_disk_size_command_from_dict = UpdateStandaloneVmDiskSizeCommand.from_dict(update_standalone_vm_disk_size_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


