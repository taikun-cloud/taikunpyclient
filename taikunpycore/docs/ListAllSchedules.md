# ListAllSchedules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CScheduleDto]**](CScheduleDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.list_all_schedules import ListAllSchedules

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllSchedules from a JSON string
list_all_schedules_instance = ListAllSchedules.from_json(json)
# print the JSON string representation of the object
print(ListAllSchedules.to_json())

# convert the object into a dict
list_all_schedules_dict = list_all_schedules_instance.to_dict()
# create an instance of ListAllSchedules from a dict
list_all_schedules_from_dict = ListAllSchedules.from_dict(list_all_schedules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


