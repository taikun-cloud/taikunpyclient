# ProjectExtendLifeTimeCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**expire_at** | **datetime** |  | [optional] 
**delete_on_expiration** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.project_extend_life_time_command import ProjectExtendLifeTimeCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectExtendLifeTimeCommand from a JSON string
project_extend_life_time_command_instance = ProjectExtendLifeTimeCommand.from_json(json)
# print the JSON string representation of the object
print(ProjectExtendLifeTimeCommand.to_json())

# convert the object into a dict
project_extend_life_time_command_dict = project_extend_life_time_command_instance.to_dict()
# create an instance of ProjectExtendLifeTimeCommand from a dict
project_extend_life_time_command_from_dict = ProjectExtendLifeTimeCommand.from_dict(project_extend_life_time_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


