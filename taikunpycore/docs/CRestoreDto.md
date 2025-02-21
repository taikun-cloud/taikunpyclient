# CRestoreDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**backup_name** | **str** |  | 
**schedule_name** | **str** |  | 
**namespace** | **str** |  | 
**exclude_namespaces** | **List[str]** |  | 
**include_namespaces** | **List[str]** |  | 
**completion_date_time** | **datetime** |  | 
**start_time_stamp** | **datetime** |  | 
**created_at** | **datetime** |  | 
**warnings** | **int** |  | 
**phase** | **str** |  | 

## Example

```python
from taikunpycore.models.c_restore_dto import CRestoreDto

# TODO update the JSON string below
json = "{}"
# create an instance of CRestoreDto from a JSON string
c_restore_dto_instance = CRestoreDto.from_json(json)
# print the JSON string representation of the object
print(CRestoreDto.to_json())

# convert the object into a dict
c_restore_dto_dict = c_restore_dto_instance.to_dict()
# create an instance of CRestoreDto from a dict
c_restore_dto_from_dict = CRestoreDto.from_dict(c_restore_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


