# DeleteVmDiskCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standalone_vm_id** | **int** |  | [optional] 
**vm_disk_ids** | **List[int]** |  | [optional] 

## Example

```python
from taikunpycore.models.delete_vm_disk_command import DeleteVmDiskCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVmDiskCommand from a JSON string
delete_vm_disk_command_instance = DeleteVmDiskCommand.from_json(json)
# print the JSON string representation of the object
print(DeleteVmDiskCommand.to_json())

# convert the object into a dict
delete_vm_disk_command_dict = delete_vm_disk_command_instance.to_dict()
# create an instance of DeleteVmDiskCommand from a dict
delete_vm_disk_command_from_dict = DeleteVmDiskCommand.from_dict(delete_vm_disk_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


