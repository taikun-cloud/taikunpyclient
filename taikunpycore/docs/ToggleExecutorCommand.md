# ToggleExecutorCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.toggle_executor_command import ToggleExecutorCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleExecutorCommand from a JSON string
toggle_executor_command_instance = ToggleExecutorCommand.from_json(json)
# print the JSON string representation of the object
print(ToggleExecutorCommand.to_json())

# convert the object into a dict
toggle_executor_command_dict = toggle_executor_command_instance.to_dict()
# create an instance of ToggleExecutorCommand from a dict
toggle_executor_command_from_dict = ToggleExecutorCommand.from_dict(toggle_executor_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


