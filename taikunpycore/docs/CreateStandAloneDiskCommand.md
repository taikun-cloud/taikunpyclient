# CreateStandAloneDiskCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standalone_vm_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**volume_type** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.create_stand_alone_disk_command import CreateStandAloneDiskCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStandAloneDiskCommand from a JSON string
create_stand_alone_disk_command_instance = CreateStandAloneDiskCommand.from_json(json)
# print the JSON string representation of the object
print(CreateStandAloneDiskCommand.to_json())

# convert the object into a dict
create_stand_alone_disk_command_dict = create_stand_alone_disk_command_instance.to_dict()
# create an instance of CreateStandAloneDiskCommand from a dict
create_stand_alone_disk_command_from_dict = CreateStandAloneDiskCommand.from_dict(create_stand_alone_disk_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


