# CScheduleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**metadata_name** | **str** |  | 
**namespace** | **str** |  | 
**created_at** | **datetime** |  | 
**schedule** | **str** |  | 
**ttl** | **str** |  | 
**last_backup** | **datetime** |  | 
**phase** | **str** |  | 
**excluded_namespaces** | **List[str]** |  | 
**included_namespaces** | **List[str]** |  | 

## Example

```python
from taikunpycore.models.c_schedule_dto import CScheduleDto

# TODO update the JSON string below
json = "{}"
# create an instance of CScheduleDto from a JSON string
c_schedule_dto_instance = CScheduleDto.from_json(json)
# print the JSON string representation of the object
print(CScheduleDto.to_json())

# convert the object into a dict
c_schedule_dto_dict = c_schedule_dto_instance.to_dict()
# create an instance of CScheduleDto from a dict
c_schedule_dto_from_dict = CScheduleDto.from_dict(c_schedule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


