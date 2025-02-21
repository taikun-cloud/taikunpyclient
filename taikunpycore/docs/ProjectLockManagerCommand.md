# ProjectLockManagerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.project_lock_manager_command import ProjectLockManagerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectLockManagerCommand from a JSON string
project_lock_manager_command_instance = ProjectLockManagerCommand.from_json(json)
# print the JSON string representation of the object
print(ProjectLockManagerCommand.to_json())

# convert the object into a dict
project_lock_manager_command_dict = project_lock_manager_command_instance.to_dict()
# create an instance of ProjectLockManagerCommand from a dict
project_lock_manager_command_from_dict = ProjectLockManagerCommand.from_dict(project_lock_manager_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


