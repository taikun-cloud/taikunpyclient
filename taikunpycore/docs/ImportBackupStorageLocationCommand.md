# ImportBackupStorageLocationCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_project_id** | **int** |  | [optional] 
**source_project_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.import_backup_storage_location_command import ImportBackupStorageLocationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ImportBackupStorageLocationCommand from a JSON string
import_backup_storage_location_command_instance = ImportBackupStorageLocationCommand.from_json(json)
# print the JSON string representation of the object
print(ImportBackupStorageLocationCommand.to_json())

# convert the object into a dict
import_backup_storage_location_command_dict = import_backup_storage_location_command_instance.to_dict()
# create an instance of ImportBackupStorageLocationCommand from a dict
import_backup_storage_location_command_from_dict = ImportBackupStorageLocationCommand.from_dict(import_backup_storage_location_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


