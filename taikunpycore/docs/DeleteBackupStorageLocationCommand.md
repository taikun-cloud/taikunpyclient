# DeleteBackupStorageLocationCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**storage_location** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.delete_backup_storage_location_command import DeleteBackupStorageLocationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBackupStorageLocationCommand from a JSON string
delete_backup_storage_location_command_instance = DeleteBackupStorageLocationCommand.from_json(json)
# print the JSON string representation of the object
print(DeleteBackupStorageLocationCommand.to_json())

# convert the object into a dict
delete_backup_storage_location_command_dict = delete_backup_storage_location_command_instance.to_dict()
# create an instance of DeleteBackupStorageLocationCommand from a dict
delete_backup_storage_location_command_from_dict = DeleteBackupStorageLocationCommand.from_dict(delete_backup_storage_location_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


