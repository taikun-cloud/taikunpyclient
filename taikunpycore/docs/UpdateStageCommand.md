# UpdateStageCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**stage** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_stage_command import UpdateStageCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStageCommand from a JSON string
update_stage_command_instance = UpdateStageCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateStageCommand.to_json())

# convert the object into a dict
update_stage_command_dict = update_stage_command_instance.to_dict()
# create an instance of UpdateStageCommand from a dict
update_stage_command_from_dict = UpdateStageCommand.from_dict(update_stage_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


