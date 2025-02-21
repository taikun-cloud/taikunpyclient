# ResetProjectStatusCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**status** | [**ProjectStatus**](ProjectStatus.md) |  | [optional] 

## Example

```python
from taikunpycore.models.reset_project_status_command import ResetProjectStatusCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ResetProjectStatusCommand from a JSON string
reset_project_status_command_instance = ResetProjectStatusCommand.from_json(json)
# print the JSON string representation of the object
print(ResetProjectStatusCommand.to_json())

# convert the object into a dict
reset_project_status_command_dict = reset_project_status_command_instance.to_dict()
# create an instance of ResetProjectStatusCommand from a dict
reset_project_status_command_from_dict = ResetProjectStatusCommand.from_dict(reset_project_status_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


