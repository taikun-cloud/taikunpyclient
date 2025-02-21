# BackupStorageLocationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**provider** | **str** |  | 
**namespace** | **str** |  | 
**last_validated** | **datetime** |  | 
**created_at** | **datetime** |  | 
**access_mode** | **str** |  | 
**phase** | **str** |  | 
**backup_credential_id** | **int** |  | 

## Example

```python
from taikunpycore.models.backup_storage_location_dto import BackupStorageLocationDto

# TODO update the JSON string below
json = "{}"
# create an instance of BackupStorageLocationDto from a JSON string
backup_storage_location_dto_instance = BackupStorageLocationDto.from_json(json)
# print the JSON string representation of the object
print(BackupStorageLocationDto.to_json())

# convert the object into a dict
backup_storage_location_dto_dict = backup_storage_location_dto_instance.to_dict()
# create an instance of BackupStorageLocationDto from a dict
backup_storage_location_dto_from_dict = BackupStorageLocationDto.from_dict(backup_storage_location_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


