# CDeleteBackupRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**created_at** | **datetime** |  | 
**backup_name** | **str** |  | 
**namespace** | **str** |  | 
**phase** | **str** |  | 

## Example

```python
from taikunpycore.models.c_delete_backup_request_dto import CDeleteBackupRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CDeleteBackupRequestDto from a JSON string
c_delete_backup_request_dto_instance = CDeleteBackupRequestDto.from_json(json)
# print the JSON string representation of the object
print(CDeleteBackupRequestDto.to_json())

# convert the object into a dict
c_delete_backup_request_dto_dict = c_delete_backup_request_dto_instance.to_dict()
# create an instance of CDeleteBackupRequestDto from a dict
c_delete_backup_request_dto_from_dict = CDeleteBackupRequestDto.from_dict(c_delete_backup_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


