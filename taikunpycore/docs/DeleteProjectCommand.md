# DeleteProjectCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**is_force_delete** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.delete_project_command import DeleteProjectCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteProjectCommand from a JSON string
delete_project_command_instance = DeleteProjectCommand.from_json(json)
# print the JSON string representation of the object
print(DeleteProjectCommand.to_json())

# convert the object into a dict
delete_project_command_dict = delete_project_command_instance.to_dict()
# create an instance of DeleteProjectCommand from a dict
delete_project_command_from_dict = DeleteProjectCommand.from_dict(delete_project_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


