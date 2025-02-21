# ListAllBackupStorageLocations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BackupStorageLocationDto]**](BackupStorageLocationDto.md) |  | 
**total_count** | **int** |  | 
**projects** | **List[int]** |  | 

## Example

```python
from taikunpycore.models.list_all_backup_storage_locations import ListAllBackupStorageLocations

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllBackupStorageLocations from a JSON string
list_all_backup_storage_locations_instance = ListAllBackupStorageLocations.from_json(json)
# print the JSON string representation of the object
print(ListAllBackupStorageLocations.to_json())

# convert the object into a dict
list_all_backup_storage_locations_dict = list_all_backup_storage_locations_instance.to_dict()
# create an instance of ListAllBackupStorageLocations from a dict
list_all_backup_storage_locations_from_dict = ListAllBackupStorageLocations.from_dict(list_all_backup_storage_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


