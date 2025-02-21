# DeleteScheduleCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.delete_schedule_command import DeleteScheduleCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteScheduleCommand from a JSON string
delete_schedule_command_instance = DeleteScheduleCommand.from_json(json)
# print the JSON string representation of the object
print(DeleteScheduleCommand.to_json())

# convert the object into a dict
delete_schedule_command_dict = delete_schedule_command_instance.to_dict()
# create an instance of DeleteScheduleCommand from a dict
delete_schedule_command_from_dict = DeleteScheduleCommand.from_dict(delete_schedule_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


