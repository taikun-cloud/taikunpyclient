# CBackupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**created_at** | **datetime** |  | 
**expiration** | **datetime** |  | 
**schedule_name** | **str** |  | 
**namespace** | **str** |  | 
**location** | **str** |  | 
**phase** | **str** |  | 

## Example

```python
from taikunpycore.models.c_backup_dto import CBackupDto

# TODO update the JSON string below
json = "{}"
# create an instance of CBackupDto from a JSON string
c_backup_dto_instance = CBackupDto.from_json(json)
# print the JSON string representation of the object
print(CBackupDto.to_json())

# convert the object into a dict
c_backup_dto_dict = c_backup_dto_instance.to_dict()
# create an instance of CBackupDto from a dict
c_backup_dto_from_dict = CBackupDto.from_dict(c_backup_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


