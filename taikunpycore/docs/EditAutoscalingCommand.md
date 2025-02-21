# EditAutoscalingCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**min_size** | **int** |  | [optional] 
**max_size** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.edit_autoscaling_command import EditAutoscalingCommand

# TODO update the JSON string below
json = "{}"
# create an instance of EditAutoscalingCommand from a JSON string
edit_autoscaling_command_instance = EditAutoscalingCommand.from_json(json)
# print the JSON string representation of the object
print(EditAutoscalingCommand.to_json())

# convert the object into a dict
edit_autoscaling_command_dict = edit_autoscaling_command_instance.to_dict()
# create an instance of EditAutoscalingCommand from a dict
edit_autoscaling_command_from_dict = EditAutoscalingCommand.from_dict(edit_autoscaling_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


